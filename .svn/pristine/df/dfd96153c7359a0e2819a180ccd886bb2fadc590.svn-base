import hashlib

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from UI import serialUtil, DButil, cacheUtil, xmlUtil
from UI.UserLogin import Ui_Form_User_Login
from UI.tree import Ui_Form_Tree_View




class Module_User_Login(Ui_Form_User_Login, QWidget):
    def __init__(self):
        super(Module_User_Login, self).__init__()
        self.setupUi(self)
        loginType = xmlUtil.getValue("login", "loginType", "value")
        if loginType is None:
            self.loginType.show()
            self.label_4.show()
        self.pushButton.clicked.connect(lambda :self.login_check(loginType))
        # 背景图片暂不添加
        # window_pale = QtGui.QPalette()
        # window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("background_img/img2.jpg")))
        # self.setPalette(window_pale)

    def login_check(self, loginType):
        cardStatusCmd = [0x00, 0x02, 0x00, 0x02, 0x31, 0x30, 0x03, 0x02, 0x01]
        result = serialUtil.getDate(cardStatusCmd)
        if not result:
            QMessageBox.warning(self, "错误", "读卡器未连接！", QMessageBox.Close)
            return
        if loginType is None:
            loginType = self.loginType.currentIndex()
        cacheUtil.setCache("loginType", loginType)
        _translate = QtCore.QCoreApplication.translate
        phone = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if phone.strip() == '' or password.strip() == '':
            QMessageBox.warning(self, "错误", "请输入账号或密码！", QMessageBox.Close)
            self.lineEdit.setFocus()
        else:
            # cur.execute("SELECT * FROM t_user_base")
            # password = password+"SeiYuan"
            # print(password)
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            c2c = DButil.conn_excu_sql("SELECT user_id,role_id FROM t_user_base WHERE phone  = '%s' AND password = '%s'" % (phone, md5.hexdigest()))
            cur = c2c[0]
            conn = c2c[1]
            result = cur.fetchall()
            cur.close()
            conn.close()
            if len(result) <= 0:
                QMessageBox.warning(self, "错误", "账号或密码错误！", QMessageBox.Close)
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit.setFocus()
            else:
                # 登录成功这里开始写缓存逻辑
                for user in result:
                    uid = user[0]
                    rid = user[1]
                    cacheUtil.setCache("uid", uid)
                    cacheUtil.setCache("rid", rid)
                xmlUtil.setValue("login", "loginType", "value", loginType)
                self.hide()
                self.dia = Ui_Form_Tree_View()
                self.dia.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Module_User_Login()
    w.show()
    sys.exit(app.exec_())