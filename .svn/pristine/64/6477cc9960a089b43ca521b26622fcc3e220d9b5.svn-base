from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QMessageBox, QLineEdit, QAbstractItemView, QTableWidgetItem

from UI import DButil
from PyQt5.QtCore import Qt

from UI.chooseBranch import ChooseBranch_Form


def serch_branch(self):
    branchName = self.chooseBranch.findChild(QLineEdit, "branchNameInput")
    branchNameInput = branchName.text()
    searchBranchSql = "SELECT id, branch_no, description, telephone, person, open_time, close_time, user_id, name" \
                      " FROM t_iccard_branch WHERE deleted = 0"

    paralist = []
    branchNameInput = '%' + branchNameInput + '%'

    if branchNameInput.strip() != '':
        searchBranchSql = searchBranchSql + " and description like '%s'"
        paralist.append(branchNameInput)
    if len(paralist) > 1:
        searchBranchSql = searchBranchSql % tuple(paralist)
    elif len(paralist) > 0:
        searchBranchSql = searchBranchSql % paralist[0]

    searchBranchSqlResult = DButil.conn_excu_sql(searchBranchSql)
    cur = searchBranchSqlResult[0]
    conn = searchBranchSqlResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    table = self.chooseBranch.findChild(QTableWidget, 'tableWidget')
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



def commit_branch(self):
    table = self.chooseBranch.findChild(QTableWidget, 'tableWidget')
    selectedRanges = table.selectedRanges()
    for range in selectedRanges:
        dateList = []
        dateIndex = 0
        while dateIndex < table.columnCount():
            row = range.topRow()
            modle = table.model()
            dateIndexModel = modle.index(row, dateIndex)
            dateList.append(modle.data(dateIndexModel))
            print(dateList)
            dateIndex = dateIndex + 1
    print(dateList)

    if len(selectedRanges) <= 0:
        QMessageBox.warning(self, "错误", "未选中行！", QMessageBox.Close)
        return

     # 获得选中行的id

    self.form7.findChild(QLineEdit, "lineEdit_7").setText(dateList[1])
    self.form7.findChild(QLineEdit, "lineEdit_8").setText(dateList[2])

    self.chooseBranch.hide()


def cancel(self):
    self.chooseBranch.hide()




























