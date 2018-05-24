# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmartLib_LibrarianUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1538, 1026)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setStatusTip("")
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(48, 48))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tabOverview = QtWidgets.QWidget()
        self.tabOverview.setObjectName("tabOverview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabOverview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelOverview_Image = QtWidgets.QLabel(self.tabOverview)
        self.labelOverview_Image.setObjectName("labelOverview_Image")
        self.horizontalLayout.addWidget(self.labelOverview_Image)
        self.labelOverview_Welcome = QtWidgets.QLabel(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelOverview_Welcome.setFont(font)
        self.labelOverview_Welcome.setTextFormat(QtCore.Qt.PlainText)
        self.labelOverview_Welcome.setObjectName("labelOverview_Welcome")
        self.horizontalLayout.addWidget(self.labelOverview_Welcome)
        self.label = QtWidgets.QLabel(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonOverview_Books = QtWidgets.QPushButton(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOverview_Books.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/IMG/167756.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOverview_Books.setIcon(icon)
        self.buttonOverview_Books.setIconSize(QtCore.QSize(128, 128))
        self.buttonOverview_Books.setObjectName("buttonOverview_Books")
        self.horizontalLayout_2.addWidget(self.buttonOverview_Books)
        self.buttonOverview_Users = QtWidgets.QPushButton(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOverview_Users.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/IMG/149071.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOverview_Users.setIcon(icon1)
        self.buttonOverview_Users.setIconSize(QtCore.QSize(128, 128))
        self.buttonOverview_Users.setObjectName("buttonOverview_Users")
        self.horizontalLayout_2.addWidget(self.buttonOverview_Users)
        self.buttonOverview_Issue = QtWidgets.QPushButton(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOverview_Issue.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/IMG/clock-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOverview_Issue.setIcon(icon2)
        self.buttonOverview_Issue.setIconSize(QtCore.QSize(128, 128))
        self.buttonOverview_Issue.setObjectName("buttonOverview_Issue")
        self.horizontalLayout_2.addWidget(self.buttonOverview_Issue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonOverview_4 = QtWidgets.QPushButton(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOverview_4.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/IMG/167755.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOverview_4.setIcon(icon3)
        self.buttonOverview_4.setIconSize(QtCore.QSize(128, 128))
        self.buttonOverview_4.setObjectName("buttonOverview_4")
        self.horizontalLayout_3.addWidget(self.buttonOverview_4)
        self.buttonOverview_5 = QtWidgets.QPushButton(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOverview_5.setFont(font)
        self.buttonOverview_5.setIcon(icon3)
        self.buttonOverview_5.setIconSize(QtCore.QSize(128, 128))
        self.buttonOverview_5.setObjectName("buttonOverview_5")
        self.horizontalLayout_3.addWidget(self.buttonOverview_5)
        self.buttonOverview_6 = QtWidgets.QPushButton(self.tabOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOverview_6.setFont(font)
        self.buttonOverview_6.setIcon(icon3)
        self.buttonOverview_6.setIconSize(QtCore.QSize(128, 128))
        self.buttonOverview_6.setObjectName("buttonOverview_6")
        self.horizontalLayout_3.addWidget(self.buttonOverview_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabOverview, icon4, "")
        self.tabBooks = QtWidgets.QWidget()
        self.tabBooks.setStatusTip("")
        self.tabBooks.setObjectName("tabBooks")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabBooks)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonBooks_Add = QtWidgets.QToolButton(self.tabBooks)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon_tool/Modern UI Icons Light/appbar.add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBooks_Add.setIcon(icon5)
        self.buttonBooks_Add.setIconSize(QtCore.QSize(48, 48))
        self.buttonBooks_Add.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonBooks_Add.setObjectName("buttonBooks_Add")
        self.horizontalLayout_5.addWidget(self.buttonBooks_Add)
        self.buttonBooks_Edit = QtWidgets.QToolButton(self.tabBooks)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon_tool/Modern UI Icons Light/appbar.edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBooks_Edit.setIcon(icon6)
        self.buttonBooks_Edit.setIconSize(QtCore.QSize(48, 48))
        self.buttonBooks_Edit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonBooks_Edit.setObjectName("buttonBooks_Edit")
        self.horizontalLayout_5.addWidget(self.buttonBooks_Edit)
        self.buttonBooks_Delete = QtWidgets.QToolButton(self.tabBooks)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon_tool/Modern UI Icons Light/appbar.delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBooks_Delete.setIcon(icon7)
        self.buttonBooks_Delete.setIconSize(QtCore.QSize(48, 48))
        self.buttonBooks_Delete.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonBooks_Delete.setObjectName("buttonBooks_Delete")
        self.horizontalLayout_5.addWidget(self.buttonBooks_Delete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.labelBooks_Search = QtWidgets.QLabel(self.tabBooks)
        self.labelBooks_Search.setObjectName("labelBooks_Search")
        self.horizontalLayout_5.addWidget(self.labelBooks_Search)
        self.lineEditBooks_SearchBox = QtWidgets.QLineEdit(self.tabBooks)
        self.lineEditBooks_SearchBox.setObjectName("lineEditBooks_SearchBox")
        self.horizontalLayout_5.addWidget(self.lineEditBooks_SearchBox)
        self.buttonBooks_Go = QtWidgets.QToolButton(self.tabBooks)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.arrow.right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBooks_Go.setIcon(icon8)
        self.buttonBooks_Go.setObjectName("buttonBooks_Go")
        self.horizontalLayout_5.addWidget(self.buttonBooks_Go)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tableBooks = QtWidgets.QTableWidget(self.tabBooks)
        self.tableBooks.setObjectName("tableBooks")
        self.tableBooks.setColumnCount(6)
        self.tableBooks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooks.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooks.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooks.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBooks.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableBooks)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon_book/Modern UI Icons Light/appbar.book.list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabBooks, icon9, "")
        self.tabUsers = QtWidgets.QWidget()
        self.tabUsers.setObjectName("tabUsers")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabUsers)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.buttonUsers_Add = QtWidgets.QToolButton(self.tabUsers)
        self.buttonUsers_Add.setIcon(icon5)
        self.buttonUsers_Add.setIconSize(QtCore.QSize(48, 48))
        self.buttonUsers_Add.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonUsers_Add.setObjectName("buttonUsers_Add")
        self.horizontalLayout_6.addWidget(self.buttonUsers_Add)
        self.buttonUsers_Edit = QtWidgets.QToolButton(self.tabUsers)
        self.buttonUsers_Edit.setIcon(icon6)
        self.buttonUsers_Edit.setIconSize(QtCore.QSize(48, 48))
        self.buttonUsers_Edit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonUsers_Edit.setObjectName("buttonUsers_Edit")
        self.horizontalLayout_6.addWidget(self.buttonUsers_Edit)
        self.buttonUsers_Delete = QtWidgets.QToolButton(self.tabUsers)
        self.buttonUsers_Delete.setIcon(icon7)
        self.buttonUsers_Delete.setIconSize(QtCore.QSize(48, 48))
        self.buttonUsers_Delete.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonUsers_Delete.setObjectName("buttonUsers_Delete")
        self.horizontalLayout_6.addWidget(self.buttonUsers_Delete)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.labelUsers_Search = QtWidgets.QLabel(self.tabUsers)
        self.labelUsers_Search.setObjectName("labelUsers_Search")
        self.horizontalLayout_6.addWidget(self.labelUsers_Search)
        self.lineEditUsers_SearchBox = QtWidgets.QLineEdit(self.tabUsers)
        self.lineEditUsers_SearchBox.setObjectName("lineEditUsers_SearchBox")
        self.horizontalLayout_6.addWidget(self.lineEditUsers_SearchBox)
        self.buttonUsers_Go = QtWidgets.QToolButton(self.tabUsers)
        self.buttonUsers_Go.setIcon(icon8)
        self.buttonUsers_Go.setObjectName("buttonUsers_Go")
        self.horizontalLayout_6.addWidget(self.buttonUsers_Go)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.tableUsers = QtWidgets.QTableWidget(self.tabUsers)
        self.tableUsers.setObjectName("tableUsers")
        self.tableUsers.setColumnCount(6)
        self.tableUsers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.tableUsers)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.people.multiple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabUsers, icon10, "")
        self.tabHistory = QtWidgets.QWidget()
        self.tabHistory.setObjectName("tabHistory")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabHistory)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.buttonHistory_Refresh = QtWidgets.QToolButton(self.tabHistory)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHistory_Refresh.setIcon(icon11)
        self.buttonHistory_Refresh.setIconSize(QtCore.QSize(48, 48))
        self.buttonHistory_Refresh.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonHistory_Refresh.setObjectName("buttonHistory_Refresh")
        self.horizontalLayout_7.addWidget(self.buttonHistory_Refresh)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.labelHistory_Search = QtWidgets.QLabel(self.tabHistory)
        self.labelHistory_Search.setObjectName("labelHistory_Search")
        self.horizontalLayout_7.addWidget(self.labelHistory_Search)
        self.lineEditHistory_SearchBox = QtWidgets.QLineEdit(self.tabHistory)
        self.lineEditHistory_SearchBox.setObjectName("lineEditHistory_SearchBox")
        self.horizontalLayout_7.addWidget(self.lineEditHistory_SearchBox)
        self.buttonHistory_Go = QtWidgets.QToolButton(self.tabHistory)
        self.buttonHistory_Go.setIcon(icon8)
        self.buttonHistory_Go.setObjectName("buttonHistory_Go")
        self.horizontalLayout_7.addWidget(self.buttonHistory_Go)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.tableHistory = QtWidgets.QTableWidget(self.tabHistory)
        self.tableHistory.setObjectName("tableHistory")
        self.tableHistory.setColumnCount(6)
        self.tableHistory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableHistory.setHorizontalHeaderItem(5, item)
        self.verticalLayout_5.addWidget(self.tableHistory)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.timer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabHistory, icon12, "")
        self.tabIssue = QtWidgets.QWidget()
        self.tabIssue.setObjectName("tabIssue")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabIssue)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.buttonIssue_ReturnBook = QtWidgets.QToolButton(self.tabIssue)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIssue_ReturnBook.setIcon(icon13)
        self.buttonIssue_ReturnBook.setIconSize(QtCore.QSize(48, 48))
        self.buttonIssue_ReturnBook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.buttonIssue_ReturnBook.setObjectName("buttonIssue_ReturnBook")
        self.horizontalLayout_8.addWidget(self.buttonIssue_ReturnBook)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.labelIssue_Search = QtWidgets.QLabel(self.tabIssue)
        self.labelIssue_Search.setObjectName("labelIssue_Search")
        self.horizontalLayout_8.addWidget(self.labelIssue_Search)
        self.lineEditIssue_SearchBox = QtWidgets.QLineEdit(self.tabIssue)
        self.lineEditIssue_SearchBox.setObjectName("lineEditIssue_SearchBox")
        self.horizontalLayout_8.addWidget(self.lineEditIssue_SearchBox)
        self.buttonIssue_Go = QtWidgets.QToolButton(self.tabIssue)
        self.buttonIssue_Go.setIcon(icon8)
        self.buttonIssue_Go.setObjectName("buttonIssue_Go")
        self.horizontalLayout_8.addWidget(self.buttonIssue_Go)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableIssue = QtWidgets.QTableWidget(self.tabIssue)
        self.tableIssue.setObjectName("tableIssue")
        self.tableIssue.setColumnCount(6)
        self.tableIssue.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableIssue.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIssue.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIssue.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIssue.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIssue.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIssue.setHorizontalHeaderItem(5, item)
        self.verticalLayout_6.addWidget(self.tableIssue)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.information.circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabIssue, icon14, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStatusTip("")
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setIconSize(QtCore.QSize(76, 76))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionMain_Menu = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.tiles.nine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMain_Menu.setIcon(icon15)
        self.actionMain_Menu.setVisible(True)
        self.actionMain_Menu.setIconVisibleInMenu(True)
        self.actionMain_Menu.setObjectName("actionMain_Menu")
        self.actionAdd_Book = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icon_book/Modern UI Icons Light/appbar.book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Book.setIcon(icon16)
        self.actionAdd_Book.setObjectName("actionAdd_Book")
        self.actionAdd_User = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.user.add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_User.setIcon(icon17)
        self.actionAdd_User.setObjectName("actionAdd_User")
        self.actionReturnBook = QtWidgets.QAction(MainWindow)
        self.actionReturnBook.setEnabled(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icon_book/Modern UI Icons Light/appbar.book.open.information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReturnBook.setIcon(icon18)
        self.actionReturnBook.setVisible(True)
        self.actionReturnBook.setObjectName("actionReturnBook")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon19)
        self.actionExit.setStatusTip("")
        self.actionExit.setObjectName("actionExit")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setIcon(icon11)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionPython = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icon_app/Modern UI Icons Light/appbar.language.python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPython.setIcon(icon20)
        self.actionPython.setObjectName("actionPython")
        self.toolBar.addAction(self.actionMain_Menu)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Book)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_User)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReturnBook)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPython)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyLibrary - Librarian Console"))
        self.labelOverview_Image.setStatusTip(_translate("MainWindow", "Profile picture"))
        self.labelOverview_Image.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/avatar/IMG/Susan_big.png\"/></p></body></html>"))
        self.labelOverview_Welcome.setText(_translate("MainWindow", "  Welcome,    "))
        self.label.setText(_translate("MainWindow", "Mrs. Susan | 190389344"))
        self.buttonOverview_Books.setStatusTip(_translate("MainWindow", "View all books"))
        self.buttonOverview_Books.setText(_translate("MainWindow", "  ___ Books"))
        self.buttonOverview_Users.setStatusTip(_translate("MainWindow", "View all users"))
        self.buttonOverview_Users.setText(_translate("MainWindow", "  ___ Users"))
        self.buttonOverview_Issue.setStatusTip(_translate("MainWindow", "View all issue books"))
        self.buttonOverview_Issue.setText(_translate("MainWindow", " ___ Issue Books"))
        self.buttonOverview_4.setStatusTip(_translate("MainWindow", "Add a new book"))
        self.buttonOverview_4.setText(_translate("MainWindow", "  Add Book"))
        self.buttonOverview_5.setStatusTip(_translate("MainWindow", "Add a new user"))
        self.buttonOverview_5.setText(_translate("MainWindow", "  Add User"))
        self.buttonOverview_6.setStatusTip(_translate("MainWindow", "Return a book"))
        self.buttonOverview_6.setText(_translate("MainWindow", "  Return Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOverview), _translate("MainWindow", "Overview"))
        self.buttonBooks_Add.setStatusTip(_translate("MainWindow", "Add a new book"))
        self.buttonBooks_Add.setText(_translate("MainWindow", "Add Book"))
        self.buttonBooks_Edit.setStatusTip(_translate("MainWindow", "Edit selected book"))
        self.buttonBooks_Edit.setText(_translate("MainWindow", "Edit Book"))
        self.buttonBooks_Delete.setStatusTip(_translate("MainWindow", "Delete selected book"))
        self.buttonBooks_Delete.setText(_translate("MainWindow", "Delete Book"))
        self.labelBooks_Search.setStatusTip(_translate("MainWindow", "Enter a book title"))
        self.labelBooks_Search.setText(_translate("MainWindow", "Search:"))
        self.lineEditBooks_SearchBox.setStatusTip(_translate("MainWindow", "Enter a book title"))
        self.buttonBooks_Go.setStatusTip(_translate("MainWindow", "Enter a book title"))
        self.buttonBooks_Go.setText(_translate("MainWindow", "Go"))
        self.tableBooks.setStatusTip(_translate("MainWindow", "Double click to edit a book"))
        item = self.tableBooks.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableBooks.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableBooks.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableBooks.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Publisher"))
        item = self.tableBooks.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.tableBooks.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "RFID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBooks), _translate("MainWindow", "All Books"))
        self.buttonUsers_Add.setStatusTip(_translate("MainWindow", "Add a new user"))
        self.buttonUsers_Add.setText(_translate("MainWindow", "Add User"))
        self.buttonUsers_Edit.setStatusTip(_translate("MainWindow", "Edit selected user"))
        self.buttonUsers_Edit.setText(_translate("MainWindow", "Edit User"))
        self.buttonUsers_Delete.setStatusTip(_translate("MainWindow", "Delete selected user"))
        self.buttonUsers_Delete.setText(_translate("MainWindow", "Delete User"))
        self.labelUsers_Search.setStatusTip(_translate("MainWindow", "Enter student name"))
        self.labelUsers_Search.setText(_translate("MainWindow", "Search:"))
        self.lineEditUsers_SearchBox.setStatusTip(_translate("MainWindow", "Enter student name"))
        self.buttonUsers_Go.setStatusTip(_translate("MainWindow", "Enter student name"))
        self.buttonUsers_Go.setText(_translate("MainWindow", "Go"))
        self.tableUsers.setStatusTip(_translate("MainWindow", "Double click to edit a user"))
        item = self.tableUsers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableUsers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableUsers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableUsers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Registered On"))
        item = self.tableUsers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "LINE Token"))
        item = self.tableUsers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "RFID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUsers), _translate("MainWindow", "All Users"))
        self.buttonHistory_Refresh.setStatusTip(_translate("MainWindow", "Click to refresh"))
        self.buttonHistory_Refresh.setText(_translate("MainWindow", "  Refresh  "))
        self.labelHistory_Search.setStatusTip(_translate("MainWindow", "Enter book title or student name"))
        self.labelHistory_Search.setText(_translate("MainWindow", "Search:"))
        self.lineEditHistory_SearchBox.setStatusTip(_translate("MainWindow", "Enter book title or student name"))
        self.buttonHistory_Go.setStatusTip(_translate("MainWindow", "Enter book title or student name"))
        self.buttonHistory_Go.setText(_translate("MainWindow", "Go"))
        item = self.tableHistory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableHistory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book"))
        item = self.tableHistory.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableHistory.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Borrow Time"))
        item = self.tableHistory.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Due Time"))
        item = self.tableHistory.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Return Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHistory), _translate("MainWindow", "History"))
        self.buttonIssue_ReturnBook.setStatusTip(_translate("MainWindow", "Return a book"))
        self.buttonIssue_ReturnBook.setText(_translate("MainWindow", "Return Book"))
        self.labelIssue_Search.setStatusTip(_translate("MainWindow", "Enter "))
        self.labelIssue_Search.setText(_translate("MainWindow", "Search:"))
        self.buttonIssue_Go.setText(_translate("MainWindow", "Go"))
        item = self.tableIssue.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableIssue.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book"))
        item = self.tableIssue.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableIssue.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Borrow Time"))
        item = self.tableIssue.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Due Time"))
        item = self.tableIssue.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Return Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIssue), _translate("MainWindow", "Issue Books"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionMain_Menu.setText(_translate("MainWindow", "Main Menu"))
        self.actionMain_Menu.setStatusTip(_translate("MainWindow", "Display All Menu"))
        self.actionAdd_Book.setText(_translate("MainWindow", "Add Book"))
        self.actionAdd_User.setText(_translate("MainWindow", "Add User"))
        self.actionReturnBook.setText(_translate("MainWindow", "Return Book"))
        self.actionReturnBook.setIconText(_translate("MainWindow", "Return Book"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionPython.setText(_translate("MainWindow", "Python"))

import SmartLib_LibrarianRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

