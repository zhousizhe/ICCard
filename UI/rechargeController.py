import decimal
import time

from PyQt5.QtWidgets import QLineEdit, QMessageBox

from UI import cacheUtil, DButil, serialUtil
import binascii



def submit(self):
    lineEdit_1 = self.form2.findChild(QLineEdit, "lineEdit_1")  # 卡号
    lineEdit_2 = self.form2.findChild(QLineEdit, "lineEdit_2")  # 余额
    lineEdit_3 = self.form2.findChild(QLineEdit, "lineEdit_3")  # 金额
    lineEdit_5 = self.form2.findChild(QLineEdit, "lineEdit_5")  # 卡类型
    # 非空判断
    if lineEdit_1.text().strip() == '' or lineEdit_2.text().strip() == '' or lineEdit_3.text().strip() == '' or lineEdit_5.text().strip() == '':
        QMessageBox.warning(self, "错误", "以上信息必须填写！", QMessageBox.Close)
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
        branchNo = result[0]
        branchDesc = result[1]
        operatorId = result[2]
        operatorName = result[3]
    else:
        QMessageBox.warning(self, "错误", "没有找到对应的网点信息！", QMessageBox.Close)
        return
    if lineEdit_3.text().strip() == '' and lineEdit_2.text().strip() == '':
        ic_money_charge = 0
        ic_money_sur = 0
    else:
        ic_money_charge = decimal.Decimal(lineEdit_3.text())
        ic_money_sur = decimal.Decimal(lineEdit_2.text())
    ic_money = ic_money_sur+ic_money_charge
    # 更新card余额
    reChargeIcCardSql = "UPDATE t_iccard set ic_money=%.2f where card_no='%s'" % (ic_money, lineEdit_1.text())
    # 插入充值记录
    queryuidByCardNoSql = "SELECT user_name FROM t_user_base WHERE user_id in " \
                          "(SELECT user_id from t_iccard where card_no='%s')" % lineEdit_1.text()
    queryuidByCardNoSqlResult = DButil.conn_excu_sql(queryuidByCardNoSql)
    cur = queryuidByCardNoSqlResult[0]
    conn = queryuidByCardNoSqlResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) > 0:
        for queryuidByCardNo in result:
            userName = queryuidByCardNo[0]
    inChargeIcCardSql = "INSERT INTO t_iccard_charge_record(user_name,card_no,charge_amount,charge_time," \
                        "branch_no,branch_desc,operator_id,operator_name) values ('%s','%s','%.2f','%s','%s','%s','%s','%s')" \
                        % (userName, lineEdit_1.text(), ic_money_charge, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                           branchNo, branchDesc, operatorId, operatorName)
    # 检测读卡器是否插卡，并写入卡数据
    cardReadCmd = [0x00, 0x02, 0x00, 0x02, 0x35, 0x30, 0x03, 0x06, 0x01]
    result = serialUtil.getDate(cardReadCmd)
    if result[5] == "59":
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x03, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
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
        reChargeIcCardSqlResult = DButil.conn_excu_sql(reChargeIcCardSql)
        reChargeIcCardSqlResult[0].close()
        reChargeIcCardSqlResult[1].close()
        # 这里要添加事务以后再说吧
        inChargeIcCardSqlResult = DButil.conn_excu_sql(inChargeIcCardSql)
        inChargeIcCardSqlResult[0].close()
        inChargeIcCardSqlResult[1].close()
        QMessageBox.information(self, "成功", "充值成功！", QMessageBox.Close)

    else:
        QMessageBox.warning(self, "错误", "寻卡不成功或卡机内无卡！", QMessageBox.Close)
        return

def pushInput(self):
    cardReadCmd = [0x00, 0x02, 0x00, 0x02, 0x35, 0x30, 0x03, 0x06, 0x01]
    result = serialUtil.getDate(cardReadCmd)
    if result[5] == "59":
        lineEdit_1 = self.form2.findChild(QLineEdit, "lineEdit_1")  # 卡号
        lineEdit_2 = self.form2.findChild(QLineEdit, "lineEdit_2")  # 余额
        lineEdit_5 = self.form2.findChild(QLineEdit, "lineEdit_5")  # 卡类型
        lineEdit_3 = self.form2.findChild(QLineEdit, "lineEdit_3")  # 金额
        lineEdit_3.setText("")
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x05, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
            # --卡号
            findCmdTitle = [0x02, 0x00, 0x04, 0x35, 0x33, 0x05, 0x00, 0x03]
            result = serialUtil.getDate(serialUtil.BCCCheck(findCmdTitle))
            if result[7] == "59":
                cardNoHex = result[8]+result[9]+result[10]+result[11] + \
                             result[12]+result[13]+result[14]+result[15]+ \
                             result[16]+ result[17]+ result[18]+ result[19]+ \
                             result[20]+ result[21]+ result[22]+ result[23]
                cardNo = serialUtil.cmdResultResolve(cardNoHex)
                lineEdit_1.setText(cardNo)
        else:
            QMessageBox.warning(self, "错误", "密码校验失败！", QMessageBox.Close)
            return
        checkCardPasswordCmd = [0x02, 0x00, 0x09, 0x35, 0x32, 0x03, 0x13, 0x08, 0x18, 0x14, 0x00, 0x0D, 0x03]
        result = serialUtil.getDate(serialUtil.BCCCheck(checkCardPasswordCmd))
        if result[6] == "59":
            #   --卡类型
            findCmdTitle = [0x02, 0x00, 0x04, 0x35, 0x33, 0x03, 0x01, 0x03]
            result = serialUtil.getDate(serialUtil.BCCCheck(findCmdTitle))
            if result[7] == "59":
                cardTypeHex = result[8]+result[9]+result[10]+result[11] + \
                             result[12]+result[13]+result[14]+result[15] + \
                             result[16] + result[17] + result[18] + result[19] + \
                             result[20] + result[21] + result[22] + result[23]
                cardType = serialUtil.cmdResultResolve(cardTypeHex)
                if cardType == "0":
                    cardType = "在线卡"
                else:
                    cardType = "离线卡"
                lineEdit_5.setText(cardType)
            #  --余额
            findCmdTitle = [0x02, 0x00, 0x04, 0x35, 0x33, 0x03, 0x00, 0x03]
            result = serialUtil.getDate(serialUtil.BCCCheck(findCmdTitle))
            if result[7] == "59":
                moneyHex = result[8]+result[9]+result[10]+result[11] + \
                             result[12]+result[13]+result[14]+result[15]+ \
                             result[16]+ result[17]+ result[18]+ result[19]+ \
                             result[20]+ result[21]+ result[22]+ result[23]
                money = serialUtil.cmdResultResolve(moneyHex)
                lineEdit_2.setText(money)
        else:
            QMessageBox.warning(self, "错误", "密码校验失败！", QMessageBox.Close)
            return
    else:
        QMessageBox.warning(self, "错误", "寻卡不成功或卡机内无卡！", QMessageBox.Close)
        return
    pass