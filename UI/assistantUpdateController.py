import hashlib

from PyQt5.QtWidgets import QLineEdit, QMessageBox

from UI import DButil


def updatePassword(self):
    lineEdit = self.form9.findChild(QLineEdit, "lineEdit")
    operatorId = lineEdit.text()
    lineEdit_2 = self.form9.findChild(QLineEdit, "lineEdit_2")
    operator_Name = lineEdit_2.text()
    lineEdit_3 = self.form9.findChild(QLineEdit, "lineEdit_3")
    old_Password = lineEdit_3.text()
    lineEdit_4 = self.form9.findChild(QLineEdit, "lineEdit_4")
    new_Password = lineEdit_4.text()
    lineEdit_5 = self.form9.findChild(QLineEdit, "lineEdit_5")
    real_Password = lineEdit_5.text()

    if operatorId.strip() == '' or operator_Name.strip() == '' or old_Password.strip() == '' or new_Password.strip() == '' or  real_Password.strip() == '':
        if operatorId.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "用户编号不能为空！")
            return

        if operator_Name.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "用户名不能为空！")
            return

        if old_Password.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "原密码不能为空！")
            return

        if new_Password.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "新密码不能为空！")
            return

        if real_Password.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "确认密码不能为空！")
            return
    else:

        selectByoperatorIdSql = "SELECT * from `t_user_base` where operator_id='%s' and role_id = %d" % (operatorId, 5)
        print("SELECT * from `t_user_base` where operator_id='%s'" % operatorId)
        selectByoperatorIdResult = DButil.conn_excu_sql(selectByoperatorIdSql)
        cur = selectByoperatorIdResult[0]
        conn = selectByoperatorIdResult[1]
        result = cur.fetchall()

        if cur.rowcount > 0:
            for user in result:
                #operatorId = user[0]
                operatorName = user[1] #用户user_name
                operatorPassword = user[2]
            md5 = hashlib.md5()
            md5.update(old_Password.encode('utf-8'))
            old_Passwords = md5.hexdigest()
            print(md5.hexdigest())

            if operatorName != operator_Name:
                QMessageBox.warning(self, "警示信息",
                                    "用户名输入错误！")
                return

            if operatorPassword != old_Passwords:
                QMessageBox.warning(self, "警示信息",
                                    "原密码输入错误！")
                return

            if new_Password != real_Password:
                QMessageBox.information(self, "提示信息",
                                        "请确保两次输入密码相同！")
                return

            # if new_Password.count() !=6 or real_Password.count() !=6:
            #     QMessageBox.information(self, "提示信息",
            #                             "输入密码不能少于6位！")
            #     return

            md5 = hashlib.md5()
            md5.update(real_Password.encode('utf-8'))
            real_Passwords = md5.hexdigest()

            if old_Passwords == real_Passwords:
                QMessageBox.information(self, "提示信息",
                                        "原密码与新密码相同！")
                return

            updateByoperatorIdSql = "UPDATE `t_user_base` SET password='%s' WHERE operator_id= '%s'" %(real_Passwords, operatorId)

            c2c = DButil.conn_excu_sql(updateByoperatorIdSql)

            c2c[0].close()
            c2c[1].close()
            refush(self)
            QMessageBox.information(self, "更改", "更改成功")

        else:
            QMessageBox.warning(self, "警示信息",
                                    "没有该用户编号或不是营业员编号")
            return

        cur.close()
        conn.close()


def refush(self):
    self.form9.findChild(QLineEdit, "lineEdit").clear()
    self.form9.findChild(QLineEdit, "lineEdit_2").clear()
    self.form9.findChild(QLineEdit, "lineEdit_3").clear()
    self.form9.findChild(QLineEdit, "lineEdit_4").clear()
    self.form9.findChild(QLineEdit, "lineEdit_5").clear()