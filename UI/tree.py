# coding=utf-8
import random
import sys
import tkinter as tk

import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

from UI import cardController, cacheUtil, rechargeController, manageInformationsController, manageICCardController, \
    rechargeSearchController, assistantInformationsController, assistantInsertController, manageCreateController, \
    assistantUpdateController, chooseBranchController, xmlUtil
from UI.Top import Top_Form
from UI.assistant_information import Assistant_Information_Form
from UI.assistant_insert import Assistant_insert_Form
from UI.assistant_update_password import Assistant_Upassword_Form
from UI.card import Card_Form
from UI.chooseBranch import ChooseBranch_Form
from UI.create_brancch import Create_Brancch_Form
from UI.manageICCard import ManageICCard_Form
from UI.manage_informations import Manage_Informations_Form
from UI.recharge import Recharge_Form
from cacheout import Cache

from UI.rechargeSearch import rechargeSearch_Form


class Ui_Form_Tree_View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QVBoxLayout(self)
        top = QFrame(self)

        # top.setFrameShape(QFrame.StyledPanel)
        left = QFrame(self)
        # left.setFrameShape(QFrame.StyledPanel)
        right = QFrame(self)
        # right.setFrameShape(QFrame.StyledPanel)
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(top)
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(left)
        splitter2.setSizes([25, 0])
        splitter2.addWidget(right)
        splitter.addWidget(splitter2)
        hbox.addWidget(splitter)
        self.setLayout(hbox)

        top.setFixedSize(tk.Tk().winfo_screenwidth()*0.75, 80)
        left.setFixedSize(250, tk.Tk().winfo_screenheight()*0.8-80)
        right.setFixedSize(tk.Tk().winfo_screenwidth()*0.75-252, tk.Tk().winfo_screenheight()*0.8-80)



        #头
        self.top = QWidget(top)
        self.top.setAutoFillBackground(True)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./logo.png")))
        self.top.setPalette(window_pale)
        # 背景图片暂不添加

        ui = Top_Form()
        ui.setupUi(self.top)
        ui.quit.clicked.connect(lambda: self.quitClick())
        ui.cancel.clicked.connect(lambda: self.cancelClick())

        # 树
##
        self.tree = QTreeWidget(left)
        self.tree.setStyleSheet("background-color:#ffffff;border: 1px;border-style: solid;border-color: #BDBDBD")
        # self.tree.setAutoScroll(True)
        # self.tree.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
        # self.tree.setTextElideMode(Qt.ElideMiddle)
        #self.tree.setIndentation(30)
        # self.tree.setRootIsDecorated(True)
        # self.tree.setUniformRowHeights(False)
        # self.tree.setItemsExpandable(True)
        # self.tree.setAnimated(False)
        self.tree.setHeaderHidden(True)
        # self.tree.setExpandsOnDoubleClick(True)
        self.tree.setObjectName("tree")

        roleId = cacheUtil.getCache("rid")
        roleIds = xmlUtil.getValue("ICCard", "roleType", "value")
        roleIdsArr = roleIds.split(",")
        if str(roleId) not in roleIdsArr:  # 管理员权限-配置文件读
            root = QTreeWidgetItem(self.tree)
            root.setText(0, 'IC卡')
            # 设置树形控件的列的宽度
            self.tree.setColumnWidth(0, 150)
            # 设置子节点1
            child1 = QTreeWidgetItem()
            child1.setText(0, '办卡')
            root.addChild(child1)
            # 设置子节点2
            child2 = QTreeWidgetItem(root)
            child2.setText(0, '充值')
            # 设置子节点3
            child3 = QTreeWidgetItem(root)
            child3.setText(0, 'IC卡信息管理')
            # 设置子节点4
            child4 = QTreeWidgetItem(root)
            child4.setText(0, '充值信息查询')
            # 跟节点1
            root = QTreeWidgetItem(self.tree)
            root.setText(0, '营业员')
            # 设置子节点2
            child3 = QTreeWidgetItem(root)
            child3.setText(0, '营业员密码修改')
            # 加载根节点的所有属性与子控件
            self.tree.addTopLevelItem(root)
        else:
            # 设置根节点
            root = QTreeWidgetItem(self.tree)
            root.setText(0, 'IC卡')
            # 设置树形控件的列的宽度
            self.tree.setColumnWidth(0, 150)
            # 设置子节点1
            child1 = QTreeWidgetItem()
            child1.setText(0, '办卡')
            root.addChild(child1)
            # 设置子节点2
            child2 = QTreeWidgetItem(root)
            child2.setText(0, '充值')
            # 设置子节点3
            child3 = QTreeWidgetItem(root)
            child3.setText(0, 'IC卡信息管理')
            # 设置子节点4
            child4 = QTreeWidgetItem(root)
            child4.setText(0, '充值信息查询')
            # 跟节点1
            root = QTreeWidgetItem(self.tree)
            root.setText(0, '网点')
            # 设置子节点1
            child1 = QTreeWidgetItem()
            child1.setText(0, '创建网点')
            root.addChild(child1)
            # 设置子节点2
            child2 = QTreeWidgetItem(root)
            child2.setText(0, '网点信息管理')
            # 跟节点2
            root = QTreeWidgetItem(self.tree)
            root.setText(0, '营业员')
            # 设置子节点1
            child1 = QTreeWidgetItem()
            child1.setText(0, '添加营业员')
            root.addChild(child1)
            # 设置子节点2
            child2 = QTreeWidgetItem(root)
            child2.setText(0, '营业员信息管理')
            # 设置子节点2
            child3 = QTreeWidgetItem(root)
            child3.setText(0, '营业员密码修改')
            # 加载根节点的所有属性与子控件
            self.tree.addTopLevelItem(root)


        # 设置stackedWidget
        self.stackedWidget = QStackedWidget(right)
        self.top.setFixedSize(tk.Tk().winfo_screenwidth() * 0.75, 80)
        self.tree.setFixedSize(250, tk.Tk().winfo_screenheight() * 0.8 - 80)
        self.stackedWidget.setFixedSize(tk.Tk().winfo_screenwidth() * 0.75 - 252, tk.Tk().winfo_screenheight() * 0.8 - 80)
        # self.stackedWidget.setFixedSize(tk.Tk().winfo_screenwidth() * 0.75 - 250, tk.Tk().winfo_screenheight() * 0.8 - 80)

        # 设置第一个面板
        widget = QtWidgets.QWidget()
        ui = Card_Form()
        ui.setupUi(widget)
        ui.pushButton.clicked.connect(lambda: cardController.submit(self))
        ui.pushButton_2.clicked.connect(lambda: cardController.pushInput(self))
        # widget.setMinimumSize(tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight()*2)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        # self.form1 = self.scroll
        self.form1 = widget
        cardController.pushInput(self)


        # 设置第二个面板
        widget = QtWidgets.QWidget()
        ui = Recharge_Form()
        ui.setupUi(widget)
        ui.pushButton.clicked.connect(lambda: rechargeController.submit(self))
        ui.pushButton_2.clicked.connect(lambda: rechargeController.pushInput(self))
        # widget.setMinimumSize(tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight() * 2)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        # self.form2 = self.scroll
        self.form2 = widget

        # 设置第三个面板
        widget = QtWidgets.QWidget()
        ui = ManageICCard_Form()
        ui.setupUi(widget)
        ui.search.clicked.connect(lambda: manageICCardController.iniquery(self))  # 搜索
        ui.cardPin.clicked.connect(lambda: manageICCardController.cardPin(self))  # 销卡
        ui.transfer.clicked.connect(lambda: manageICCardController.transfer(self))  # 过户
        ui.removeException.clicked.connect(lambda: manageICCardController.removeException(self))  # 解除异常
        # ui = ()
        # ui.setupUi(widget)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.form3 = widget

        # 设置第四个面板
        widget = QtWidgets.QWidget()
        ui = rechargeSearch_Form()
        ui.setupUi(widget)
        ui.search.clicked.connect(lambda: rechargeSearchController.iniquery(self))
        # ui = Card_Form()
        # ui.setupUi(widget)
        self.form4 = widget

        # 设置第五个面板
        widget = QtWidgets.QWidget()
        ui = Create_Brancch_Form()
        ui.setupUi(widget)
        ui.pushButton_3.clicked.connect(lambda: manageCreateController.save_click(self)) #保存
        ui.pushButton_2.clicked.connect(lambda: manageCreateController.refush(self)) #重置
        ui.comboBox_3.currentIndexChanged.connect(lambda: manageCreateController.province_clicked(self)) #省被点击
        ui.comboBox_2.currentIndexChanged.connect(lambda: manageCreateController.city_cilcked(self)) #市被点击
        self.form5 = widget
        manageCreateController.loading_branch(self) #加载页面
        manageCreateController.loading_province(self) #加载省

        # 设置第六个面板
        widget = QtWidgets.QWidget()
        ui = Manage_Informations_Form()
        ui.setupUi(widget)
        ui.comboBox.currentIndexChanged.connect(lambda:manageInformationsController.comboBox_clicked(self)) #省被点击
        ui.comboBox_2.currentIndexChanged.connect(lambda:manageInformationsController.combox2_clicked(self)) #市被点击
        ui.pushButton_5.clicked.connect(lambda: manageInformationsController.serach_branch(self)) #搜索网点
        ui.pushButton_4.clicked.connect(lambda: manageInformationsController.modify_branch(self)) #修改网点
        ui.pushButton_3.clicked.connect(lambda: manageInformationsController.revoke_branch(self)) #撤销网点
        # widget.setMinimumSize(tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight() * 2)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        # self.form6 = self.scroll
        self.form6 = widget
        manageInformationsController.loading(self) #加载页面


        # 设置第七个面板
        widget = QtWidgets.QWidget()
        ui = Assistant_insert_Form()
        ui.setupUi(widget)
        ui.pushButton.clicked.connect(lambda: assistantInsertController.save_click(self)) #保存
        ui.pushButton_2.clicked.connect(lambda: assistantInsertController.refush(self)) #重置
        ui.pushButton_3.clicked.connect(lambda:assistantInsertController.choose_branch(self)) #选择网点
        # widget.setMinimumSize(tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight() * 2)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        # self.form7 = self.scroll
        self.form7 = widget

        # 设置第八个面板
        widget = QtWidgets.QWidget()
        ui = Assistant_Information_Form()
        ui.setupUi(widget)
        ui.pushButton_5.clicked.connect(lambda: assistantInformationsController.serach_assistant(self)) #搜索营业员
        ui.pushButton_3.clicked.connect(lambda: assistantInformationsController.remove_assistant(self)) #删除营业员
        ui.pushButton_4.clicked.connect(lambda: assistantInformationsController.update_assistant(self)) #修改营业员
        # widget.setMinimumSize(tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight() * 2)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        # self.form8 = self.scroll
        self.form8 = widget
        assistantInformationsController.loading_assistant(self) #初始化加载营业员页面

        # 设置第九个面板
        widget = QtWidgets.QWidget()
        ui = Assistant_Upassword_Form()
        ui.setupUi(widget)
        ui.pushButton.clicked.connect(lambda: assistantUpdateController.updatePassword(self))
        # widget.setMinimumSize(tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight() * 2)
        # self.scroll = QScrollArea()
        # self.scroll.setWidget(widget)
        # self.form9 = self.scroll
        self.form9 = widget

        # 将面板，加入stackedWidget
        self.stackedWidget.addWidget(self.form1)
        self.stackedWidget.addWidget(self.form2)
        self.stackedWidget.addWidget(self.form3)
        self.stackedWidget.addWidget(self.form4)
        self.stackedWidget.addWidget(self.form5)
        self.stackedWidget.addWidget(self.form6)
        self.stackedWidget.addWidget(self.form7)
        self.stackedWidget.addWidget(self.form8)
        self.stackedWidget.addWidget(self.form9)

        # 树节点监听事件
        self.tree.clicked.connect(self.onClicked)

        # 窗口最大化
        # self.showMaximized()
        self.setFixedSize(tk.Tk().winfo_screenwidth()*0.75, tk.Tk().winfo_screenheight()*0.8)
        # self.setMaximumSize(1920, 1024)
        self.setWindowTitle('电动IC卡管理系统')
        # self.setFixedWidth(tk.Tk().winfo_screenwidth()*0.75)
        self.show()


        # # 窗口初始化
        # self.setWindowTitle('电动车IC卡管理系统')
        # self.resize(800, 600)
        # self.setMinimumWidth(800)
        # self.setMinimumHeight(600)
        # self.show()

    def onClicked(self,qmodeLindex):
        item = self.tree.currentItem()
        # print('Key=%s,value=%s'%(item.text(0),item.text(1)))
        itemName = item.text(0)
        if itemName == "办卡":
            self.on_pushButton1_clicked()
        elif itemName == "充值":
            self.on_pushButton2_clicked()
        elif itemName == "IC卡信息管理":
            self.on_pushButton3_clicked()
        elif itemName == "充值信息查询":
            self.on_pushButton4_clicked()
        elif itemName == "创建网点":
            self.on_pushButton5_clicked()
        elif itemName == "网点信息管理":
            self.on_pushButton6_clicked()
        elif itemName == "添加营业员":
            self.on_pushButton7_clicked()
        elif itemName == "营业员信息管理":
            self.on_pushButton8_clicked()
        elif itemName == "营业员密码修改":
            self.on_pushButton9_clicked()
        else:
            print('返回主界面')


    # 按钮一：打开第一个面板
    def on_pushButton1_clicked(self):
        cardController.pushInput(self)
        self.stackedWidget.setCurrentIndex(0)

    # 按钮二：打开第二个面板
    def on_pushButton2_clicked(self):
        rechargeController.pushInput(self)
        self.stackedWidget.setCurrentIndex(1)

    # 按钮三：打开第三个面板
    def on_pushButton3_clicked(self):
        manageICCardController.iniquery(self)
        manageICCardController.queryOpenBranchName(self)
        self.stackedWidget.setCurrentIndex(2)

    # 按钮四：打开第四个面板
    def on_pushButton4_clicked(self):
        rechargeSearchController.iniquery(self)
        rechargeSearchController.queryOpenBranchName(self)
        self.stackedWidget.setCurrentIndex(3)

    # 按钮五：打开第五个面板
    def on_pushButton5_clicked(self):
        self.stackedWidget.setCurrentIndex(4)

    # 按钮六：打开第六个面板
    def on_pushButton6_clicked(self):
        manageInformationsController.serach_branch(self)
        self.stackedWidget.setCurrentIndex(5)

    # 按钮七：打开第七个面板
    def on_pushButton7_clicked(self):
        self.stackedWidget.setCurrentIndex(6)

    # 按钮八：打开第八个面板
    def on_pushButton8_clicked(self):
        assistantInformationsController.serach_assistant(self)
        self.stackedWidget.setCurrentIndex(7)

    # 按钮九：打开第九个面板
    def on_pushButton9_clicked(self):
        self.stackedWidget.setCurrentIndex(8)

    def closeEvent(self, event):
        """
                重写closeEvent方法，实现dialog窗体关闭时执行一些代码
                :param event: close()触发的事件
                :return: None
                """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            cacheUtil.deleteCash("uid")
            cacheUtil.deleteCash("rid")
            cacheUtil.deleteCash("loginType")
            event.accept()
        else:
            event.ignore()

    def quitClick(self):
        self.close()

    def cancelClick(self):
        from UI.main import Module_User_Login
        self.dia = Module_User_Login()
        self.close()
        self.dia.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Form_Tree_View()
    sys.exit(app.exec_())