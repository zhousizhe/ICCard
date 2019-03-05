import time

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QMessageBox

from UI import DButil, cacheUtil, serialUtil
import decimal
from cacheout import Cache

def submit(self):
    lineEdit_9 = self.form1.findChild(QLineEdit, "lineEdit_9")  # 发卡网点
    lineEdit_8 = self.form1.findChild(QLineEdit, "lineEdit_8")  # 操作员姓名
    lineEdit_7 = self.form1.findChild(QLineEdit, "lineEdit_7")  # 卡号
    lineEdit_6 = self.form1.findChild(QLineEdit, "lineEdit_6")  # 密码 n
    lineEdit_5 = self.form1.findChild(QLineEdit, "lineEdit_5")  # 确认密码 n
    dateEdit = self.form1.findChild(QDateEdit, "dateEdit")  # 有效日期
    lineEdit_4 = self.form1.findChild(QLineEdit, "lineEdit_4")  # 余额
    comboBox = self.form1.findChild(QComboBox, "comboBox")  # 启用密码 n
    comboBox_2 = self.form1.findChild(QComboBox, "comboBox_2")  # 付费类型 n
    comboBox_3 = self.form1.findChild(QComboBox, "comboBox_3")  # IC卡类型
    comboBox_4 = self.form1.findChild(QComboBox, "comboBox_4")  # 证件类型
    lineEdit_2 = self.form1.findChild(QLineEdit, "lineEdit_2")  # 证件号码
    lineEdit_3 = self.form1.findChild(QLineEdit, "lineEdit_3")  # 手机号码
    # 非空判断
    if lineEdit_6.text().strip() == '' or lineEdit_5.text().strip() == '' or lineEdit_7.text().strip() == '' or lineEdit_7.text().strip() == '':
        QMessageBox.warning(self, "错误", "密码，卡号，余额必须填写！", QMessageBox.Close)
        return
    if lineEdit_6.text() != lineEdit_5.text():
        QMessageBox.warning(self, "错误", "两次密码输入不一致！", QMessageBox.Close)
        return
    # 判断卡号是否存在
    checkCardNoSql ="SELECT * FROM t_iccard WHERE card_no ='%s'" % lineEdit_7.text()
    checkCardNoSqlResult = DButil.conn_excu_sql(checkCardNoSql)
    cur = checkCardNoSqlResult[0]
    conn = checkCardNoSqlResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) > 0:
        QMessageBox.warning(self, "错误", "卡号已存在！", QMessageBox.Close)
        return
    uid = cacheUtil.getCache('uid')
    if uid is None:
        QMessageBox.warning(self, "错误", "登录信息已过期，请重新登录！", QMessageBox.Close)
        return

    # 查询网点
    branchSql = "SELECT tib.branch_no,tub.user_name,tib.user_id,tib.`name` " \
                "FROM t_user_base tub LEFT JOIN t_iccard_branch tib " \
                "ON tub.branch_no=tib.branch_no WHERE tub.user_id ='%s'" % uid
    branchResult = DButil.conn_excu_sql(branchSql)
    cur = branchResult[0]
    conn = branchResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) > 0:
        for branch in result:
            branchNo = branch[0]
            description = branch[1]
            operatorId = branch[2]
            operatorName = branch[3]
    else:
        QMessageBox.warning(self, "错误", "没有找到对应的网点信息！", QMessageBox.Close)
        return
    if lineEdit_4.text().strip() == '':
        ic_money = 0
    else:
        ic_money = decimal.Decimal(lineEdit_4.text())
    insertIcCardSql = "INSERT INTO t_iccard(open_branch_id, open_branch_name, open_operator_id, open_operator_name, card_no, valid_time," \
          " ic_money, card_type, papers_type, papers_num, phone, open_card_time, blacklist_f, deleted, error_f) values " \
          "('%s','%s', '%s', '%s', '%s', '%s', %.2f, %d, %d, '%s','%s','%s', %d, %d, %d)" \
          % (branchNo, lineEdit_9.text(), operatorId, lineEdit_8.text(), lineEdit_7.text(), dateEdit.text(),
             ic_money, comboBox_3.currentIndex(), comboBox_4.currentIndex(),
             lineEdit_2.text(), lineEdit_3.text(), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 0, 0, 0)
    # 检测读卡器是否插卡，并写入卡数据
    cardReadCmd = [0x00, 0x02, 0x00, 0x02, 0x35, 0x30, 0x03, 0x06, 0x01]
    result = serialUtil.getDate(cardReadCmd)
    if result[5] == "59":
        # 寻卡成功，写卡
        # 验证扇区密码,checkCardPassword[5]扇区号后面6字节密码
        #     第一区
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x01, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
            #     --密码启用标志01, 00
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x01, 0x00]
            dateHex = serialUtil.inputToHex(comboBox.currentIndex())
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入启用标志数据失败！", QMessageBox.Close)
                return
            # #   --用户密码01,01
            # addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x01, 0x01]
            # dateHex = serialUtil.inputToHex(lineEdit_6.text())
            # result = serialUtil.writeDisk(addCmdTitle, dateHex)
            # if result[7] != "59":
            #     QMessageBox.warning(self, "错误", "写入用户密码数据失败！", QMessageBox.Close)
            #     return
        else:
            QMessageBox.warning(self, "错误", "密码校验失败！", QMessageBox.Close)
            return
        #     第三区
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x03, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
            #   --在线结算03, 01
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x03, 0x01]
            dateHex = serialUtil.inputToHex(comboBox_3.currentIndex())
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入IC卡类型数据失败！", QMessageBox.Close)
                return
            #   --运营商和网点编号03, 02
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x03, 0x02]
            dateHex = serialUtil.inputToHex(branchNo)
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入运营商和网点数据失败！", QMessageBox.Close)
                return
            #   --余额03, 00
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x03, 0x00]
            dateHex = serialUtil.inputToHex(ic_money)
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入余额数据失败！", QMessageBox.Close)
                return
        else:
            QMessageBox.warning(self, "错误", "密码校验失败！", QMessageBox.Close)
            return
        #     第二区
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x02, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
            #  --用户编号 02, 00
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x02, 0x00]
            dateHex = serialUtil.inputToHex(uid)
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入用户编号数据失败！", QMessageBox.Close)
                return
            #  --付费类型 02, 01
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x02, 0x01]
            dateHex = serialUtil.inputToHex(comboBox_2.currentIndex())
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入付费类型数据失败！", QMessageBox.Close)
                return
            #  --有效日期 02, 02
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x02, 0x02]
            dateHex = serialUtil.inputToHex(dateEdit.text())
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入有效日期数据失败！", QMessageBox.Close)
                return
        else:
            QMessageBox.warning(self, "错误", "密码校验失败！", QMessageBox.Close)
            return
        # 第五区
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x05, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
            #  --卡号 05, 00
            addCmdTitle = [0x02, 0x00, 0x14, 0x35, 0x34, 0x05, 0x00]
            dateHex = serialUtil.inputToHex(lineEdit_7.text())
            result = serialUtil.writeDisk(addCmdTitle, dateHex)
            if result[7] != "59":
                QMessageBox.warning(self, "错误", "写入卡号数据失败！", QMessageBox.Close)
                return
        else:
            QMessageBox.warning(self, "错误", "密码校验失败！", QMessageBox.Close)
            return
    # 检测完成后插入数据
        insertIcCardSqlResult = DButil.conn_excu_sql(insertIcCardSql)
        cur = insertIcCardSqlResult[0]
        conn = insertIcCardSqlResult[1]
        result = cur
        cur.close()
        conn.close()
        if result.rowcount > 0:
            QMessageBox.information(self, "成功", "办卡成功！", QMessageBox.Close)
    else:
        QMessageBox.warning(self, "错误", "寻卡不成功或卡机内无卡！", QMessageBox.Close)
        return

def pushInput(self):
    uid = cacheUtil.getCache('uid')
    if uid is None:
        QMessageBox.warning(self, "错误", "登录信息已过期，请重新登录！", QMessageBox.Close)
        return
    lineEdit_9 = self.form1.findChild(QLineEdit, "lineEdit_9")  # 发卡网点
    lineEdit_8 = self.form1.findChild(QLineEdit, "lineEdit_8")  # 操作员姓名
    lineEdit_7 = self.form1.findChild(QLineEdit, "lineEdit_7")  # 卡号
    lineEdit_6 = self.form1.findChild(QLineEdit, "lineEdit_6")  # 密码 n
    lineEdit_5 = self.form1.findChild(QLineEdit, "lineEdit_5")  # 确认密码 n
    dateEdit = self.form1.findChild(QDateEdit, "dateEdit")  # 有效日期
    lineEdit_4 = self.form1.findChild(QLineEdit, "lineEdit_4")  # 余额
    comboBox = self.form1.findChild(QComboBox, "comboBox")  # 启用密码 n
    comboBox_2 = self.form1.findChild(QComboBox, "comboBox_2")  # 付费类型 n
    comboBox_3 = self.form1.findChild(QComboBox, "comboBox_3")  # IC卡类型
    comboBox_4 = self.form1.findChild(QComboBox, "comboBox_4")  # 证件类型
    lineEdit_2 = self.form1.findChild(QLineEdit, "lineEdit_2")  # 证件号码
    lineEdit_3 = self.form1.findChild(QLineEdit, "lineEdit_3")  # 手机号码
    lineEdit_6.setText("")
    lineEdit_5.setText("")
    lineEdit_4.setText("")
    comboBox.setCurrentIndex(0)
    comboBox_2.setCurrentIndex(0)
    comboBox_3.setCurrentIndex(0)
    comboBox_4.setCurrentIndex(0)
    lineEdit_2.setText("")
    lineEdit_3.setText("")
    dateEdit.setDate(QtCore.QDate(2019, 1, 1))
    _translate = QtCore.QCoreApplication.translate
    dateEdit.setDisplayFormat(_translate("Form", "yyyyMMdd"))

    # 查询网点和运营商
    branchSql = "SELECT tib.branch_no,tub.user_name,tib.user_id,tib.`name` " \
                "FROM t_user_base tub LEFT JOIN t_iccard_branch tib " \
                "ON tub.branch_no=tib.branch_no WHERE tub.user_id ='%s'" % uid
    branchResult = DButil.conn_excu_sql(branchSql)
    cur = branchResult[0]
    conn = branchResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) > 0:
        for branch in result:
            description = branch[1]
            operatorId = branch[2]
            operatorName = branch[3]
            carNoBase = "28" + str(operatorId)[-4:]
            lineEdit_7.setText(carNoBase)
            lineEdit_9.setText(operatorName)
            lineEdit_8.setText(description)
    else:
        QMessageBox.warning(self, "错误", "没有找到对应的网点信息！", QMessageBox.Close)
        return

    # ------------------------------------
    #
    # currentText()
    # 获得文本
    # currentIndex()
    # 获得下标
    # self.comboBox.currentIndexChanged.connect()
    # comboBox的事件选中函数