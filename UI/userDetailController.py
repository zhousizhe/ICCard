from PyQt5.QtWidgets import QLineEdit, QTableWidget, QAbstractItemView, QTableWidgetItem, QMessageBox

from UI import DButil, manageICCardController


def serch_userDetail(self):
    userNameInput = self.userDetail.findChild(QLineEdit, "userNameInput")
    phoneInput = self.userDetail.findChild(QLineEdit, "phoneInput")
    cardNoInput = self.userDetail.findChild(QLineEdit, "cardNoInput")
    serchUserDetailSql = "select ub.user_id,ub.user_name,ub.phone,ub.ic_money,ub.blacklist_f,ub.nick_name," \
                         "ub.gender,ub.real_name,ub.car_owned,ub.card_type,ub.id_number," \
                         "ub.reg_source,ub.user_class,uo.province,uo.city,uo.district," \
                         "uo.address,uo.remark,ub.email " \
                         "from t_user_base ub " \
                         "left join t_user_operator uo " \
                         "on ub.user_id=uo.user_id " \
                         "left join t_iccard i " \
                         "on ub.user_id=i.user_id " \
                         "where ub.deleted = 0"

    paralist = []
    if userNameInput.text().strip() != '':
        serchUserDetailSql = serchUserDetailSql + " and ub.user_name like '%%%s%%'"
        paralist.append(userNameInput.text())
    if phoneInput.text().strip() != '':
        serchUserDetailSql = serchUserDetailSql + " and ub.phone like '%%%s%%'"
        paralist.append(phoneInput.text())
    if cardNoInput.text().strip() != '':
        serchUserDetailSql = serchUserDetailSql + " and i.card_no like '%%%s%%'"
        paralist.append(cardNoInput.text())
    if len(paralist) > 1:
        serchUserDetailSql = serchUserDetailSql % tuple(paralist)
    elif len(paralist) > 0:
        serchUserDetailSql = serchUserDetailSql % paralist[0]

    serchUserDetailSqlResult = DButil.conn_excu_sql(serchUserDetailSql)
    cur = serchUserDetailSqlResult[0]
    conn = serchUserDetailSqlResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    table = self.userDetail.findChild(QTableWidget, 'tableWidget')
    rows = result
    row = len(result)  # 取得记录个数，用于设置表格的行数
    if row < 1:
        table.clearContents()
        return
    vol = len(rows[0])  # 取得字段数，用于设置表格的列数
    table.setRowCount(row)
    table.setColumnCount(vol)
    # table = QtWidgets.QTableWidget
    # 初始化加载页面时表格内容不可修改
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
    table.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
    table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中
    table.clearSelection()  # 取消选中

    for i in range(row):
        for j in range(vol):
            temp_data = rows[i][j]  # 临时记录，不能直接插入表格
            if temp_data is None:
                temp_data = ""
            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
            table.setItem(i, j, data)

def commit_userDetail(self, idCardNoList, cardNosString):
    userTable = self.userDetail.findChild(QTableWidget, 'tableWidget')
    selectedRangesUser = userTable.selectedRanges()
    userInfoList = []
    for range in selectedRangesUser:
        row = range.topRow()
        modle = userTable.model()
        indexId = modle.index(row, 0)  # 列数据:user_id
        dataId = modle.data(indexId)
        userInfoList.append(dataId)
        indexId = modle.index(row, 1)  # 列数据:user_name
        dataId = modle.data(indexId)
        userInfoList.append(dataId)
        indexId = modle.index(row, 2)  # 列数据:phone
        dataId = modle.data(indexId)
        userInfoList.append(dataId)
        indexId = modle.index(row, 9)  # 列数据:papers_type
        dataId = modle.data(indexId)
        userInfoList.append(dataId)
        indexId = modle.index(row, 10)  # 列数据:papers_num
        dataId = modle.data(indexId)
        userInfoList.append(dataId)

    if len(selectedRangesUser) <= 0:
        QMessageBox.warning(self, "错误", "未选中行！", QMessageBox.Close)
        return

        # 获得选中行的id
    reply = QMessageBox.question(self, '警告', "是否要把卡号：" + cardNosString + "过户给：" + userInfoList[0] + "？", QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
    if reply == QMessageBox.Yes:
        for no in idCardNoList:
            updateIcCardSql = "UPDATE t_iccard SET user_id = %d,user_name= '%s',phone='%s',papers_type=%d,papers_num='%s' where card_no='%s'" \
                              % (int(userInfoList[0]), userInfoList[1], userInfoList[2], int(userInfoList[3]),userInfoList[4], no)
            try:
                c2c = DButil.conn_excu_sql(updateIcCardSql)
                c2c[0].close()
                c2c[1].close()
            except BaseException:
                QMessageBox.warning(self, "错误", "过户失败！", QMessageBox.Close)
                return
        QMessageBox.information(self, "成功", "过户成功！", QMessageBox.Close)
        self.userDetail.hide()
        manageICCardController.iniquery(self)

# def cancel_userDetail(self):
#     self.userDetail.hide()