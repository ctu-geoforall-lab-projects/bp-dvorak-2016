# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainApp.ui'
#
# Created: Fri Apr 17 22:01:49 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainApp(object):
    def setupUi(self, MainApp):
        MainApp.setObjectName(_fromUtf8("MainApp"))
        MainApp.resize(601, 493)
        MainApp.setMinimumSize(QtCore.QSize(601, 493))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainApp.setWindowIcon(icon)
        self.verticalLayout_4 = QtGui.QVBoxLayout(MainApp)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.driver_lbl = QtGui.QLabel(MainApp)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.driver_lbl.setFont(font)
        self.driver_lbl.setObjectName(_fromUtf8("driver_lbl"))
        self.horizontalLayout.addWidget(self.driver_lbl)
        self.driverBox = QtGui.QComboBox(MainApp)
        self.driverBox.setMinimumSize(QtCore.QSize(150, 0))
        self.driverBox.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.driverBox.setFont(font)
        self.driverBox.setFrame(True)
        self.driverBox.setObjectName(_fromUtf8("driverBox"))
        self.horizontalLayout.addWidget(self.driverBox)
        spacerItem = QtGui.QSpacerItem(368, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.check = QtGui.QToolButton(MainApp)
        self.check.setMaximumSize(QtCore.QSize(20, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check.setIcon(icon1)
        self.check.setIconSize(QtCore.QSize(20, 20))
        self.check.setAutoExclusive(False)
        self.check.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.check.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.check.setAutoRaise(True)
        self.check.setObjectName(_fromUtf8("check"))
        self.horizontalLayout_3.addWidget(self.check)
        self.uncheck = QtGui.QToolButton(MainApp)
        self.uncheck.setMaximumSize(QtCore.QSize(20, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uncheck.setIcon(icon2)
        self.uncheck.setIconSize(QtCore.QSize(20, 20))
        self.uncheck.setCheckable(False)
        self.uncheck.setChecked(False)
        self.uncheck.setAutoExclusive(False)
        self.uncheck.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.uncheck.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.uncheck.setAutoRaise(True)
        self.uncheck.setArrowType(QtCore.Qt.NoArrow)
        self.uncheck.setObjectName(_fromUtf8("uncheck"))
        self.horizontalLayout_3.addWidget(self.uncheck)
        self.search = QtGui.QComboBox(MainApp)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.search.setFont(font)
        self.search.setEditable(False)
        self.search.setDuplicatesEnabled(False)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout_3.addWidget(self.search)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.view = QtGui.QTableView(MainApp)
        self.view.setMinimumSize(QtCore.QSize(0, 25))
        self.view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(10)
        font.setItalic(False)
        self.view.setFont(font)
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout_4.addWidget(self.view)
        self.advanced_btn = QtGui.QToolButton(MainApp)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.advanced_btn.setFont(font)
        self.advanced_btn.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.advanced_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.advanced_btn.setAutoRaise(True)
        self.advanced_btn.setArrowType(QtCore.Qt.RightArrow)
        self.advanced_btn.setObjectName(_fromUtf8("advanced_btn"))
        self.verticalLayout_4.addWidget(self.advanced_btn)
        self.advanced = QtGui.QWidget(MainApp)
        self.advanced.setMinimumSize(QtCore.QSize(0, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.advanced.setFont(font)
        self.advanced.setObjectName(_fromUtf8("advanced"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.advanced)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(self.advanced)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.advanced)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonBox = QtGui.QDialogButtonBox(MainApp)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.import_btn = QtGui.QPushButton(MainApp)
        self.import_btn.setObjectName(_fromUtf8("import_btn"))
        self.horizontalLayout_2.addWidget(self.import_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        MainApp.setWindowTitle(_translate("MainApp", "Import dat RÚIAN", None))
        self.driver_lbl.setText(_translate("MainApp", "Výstup ", None))
        self.check.setToolTip(_translate("MainApp", "<html><head/><body><p>Přidat vše</p></body></html>", None))
        self.check.setText(_translate("MainApp", "...", None))
        self.uncheck.setToolTip(_translate("MainApp", "<html><head/><body><p>Odebrat vše</p></body></html>", None))
        self.uncheck.setText(_translate("MainApp", "...", None))
        self.advanced_btn.setText(_translate("MainApp", "Pokročilé", None))
        self.label.setText(_translate("MainApp", "Od verze pluginu 1.0 zde bude možnost volit importovaná data dle modelu RUIAN", None))
        self.import_btn.setText(_translate("MainApp", "Importovat", None))

import resources_rc

