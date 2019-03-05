from PyQt5.QtWidgets import QLineEdit, QComboBox, QMessageBox

from UI import DButil, manageInformationsController


def save(self, dateList):
    lineEdit = self.updateBanch.findChild(QLineEdit, "branchNum")
    branchNum = lineEdit.text()
    lineEdit_2 = self.updateBanch.findChild(QLineEdit, 'names')
    names = lineEdit_2.text()
    lineEdit_3 = self.updateBanch.findChild(QLineEdit, 'phone')
    phone = lineEdit_3.text()
    lineEdit_4 = self.updateBanch.findChild(QLineEdit, 'person')
    person = lineEdit_4.text()
    lineEdit_5 = self.updateBanch.findChild(QLineEdit, 'lineEdit_9')
    branchName = lineEdit_5.text()

    comBox = self.updateBanch.findChild(QComboBox, 'provinces')
    provinces = comBox.currentText()
    comBox_2 = self.updateBanch.findChild(QComboBox, 'citys')
    citys = comBox_2.currentText()
    comBox_3 = self.updateBanch.findChild(QComboBox, 'districts')
    districts = comBox_3.currentText()

    updaBranchSql = "UPDATE `t_iccard_branch` SET branch_no='%s', name='%s', telephone='%s', person='%s', province='%s', " \
                   "city='%s', district='%s', description='%s' where branch_no = '%s'" % (branchNum, names, phone, person, provinces, citys, districts,branchName, dateList[0])

    c2c = DButil.conn_excu_sql(updaBranchSql)
    c2c[0].close()
    c2c[1].close()

    QMessageBox.information(self, "成功", "更改成功！", QMessageBox.Close)
    self.updateBanch.hide()
    manageInformationsController.serach_branch(self)


def cancel(self):
    self.updateBanch.hide()
    manageInformationsController.serach_branch(self)