# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIControlCenter.ui'
#
# Created: Tue Jun 19 09:48:22 2018
#      by: PyQt4 UI code generator 4.11
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ControlPlane = QtGui.QTabWidget(self.centralwidget)
        self.ControlPlane.setGeometry(QtCore.QRect(40, 40, 721, 511))
        self.ControlPlane.setTabPosition(QtGui.QTabWidget.North)
        self.ControlPlane.setTabShape(QtGui.QTabWidget.Rounded)
        self.ControlPlane.setElideMode(QtCore.Qt.ElideLeft)
        self.ControlPlane.setObjectName(_fromUtf8("ControlPlane"))
        self.Curtain = QtGui.QWidget()
        self.Curtain.setObjectName(_fromUtf8("Curtain"))
        self.MiddleLine = QtGui.QFrame(self.Curtain)
        self.MiddleLine.setGeometry(QtCore.QRect(240, 0, 20, 491))
        self.MiddleLine.setFrameShape(QtGui.QFrame.VLine)
        self.MiddleLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.MiddleLine.setObjectName(_fromUtf8("MiddleLine"))
        self.CurtainPos = QtGui.QLabel(self.Curtain)
        self.CurtainPos.setGeometry(QtCore.QRect(230, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CurtainPos.setFont(font)
        self.CurtainPos.setObjectName(_fromUtf8("CurtainPos"))
        self.CurtainControlSlider = QtGui.QSlider(self.Curtain)
        self.CurtainControlSlider.setGeometry(QtCore.QRect(20, 78, 200, 20))
        self.CurtainControlSlider.setMaximum(16)
        self.CurtainControlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.CurtainControlSlider.setObjectName(_fromUtf8("CurtainControlSlider"))
        self.ControlCurtainTip = QtGui.QLabel(self.Curtain)
        self.ControlCurtainTip.setGeometry(QtCore.QRect(20, 13, 211, 51))
        self.ControlCurtainTip.setWordWrap(True)
        self.ControlCurtainTip.setObjectName(_fromUtf8("ControlCurtainTip"))
        self.ListWidget = QtGui.QListWidget(self.Curtain)
        self.ListWidget.setGeometry(QtCore.QRect(280, 50, 400, 251))
        self.ListWidget.setObjectName(_fromUtf8("ListWidget"))
        self.MissionTitle = QtGui.QLabel(self.Curtain)
        self.MissionTitle.setGeometry(QtCore.QRect(290, 20, 391, 16))
        self.MissionTitle.setObjectName(_fromUtf8("MissionTitle"))
        self.MissionSlider = QtGui.QSlider(self.Curtain)
        self.MissionSlider.setEnabled(False)
        self.MissionSlider.setGeometry(QtCore.QRect(470, 390, 160, 19))
        self.MissionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MissionSlider.setObjectName(_fromUtf8("MissionSlider"))
        self.ComfirmBtn = QtGui.QPushButton(self.Curtain)
        self.ComfirmBtn.setEnabled(False)
        self.ComfirmBtn.setGeometry(QtCore.QRect(530, 350, 75, 23))
        self.ComfirmBtn.setObjectName(_fromUtf8("ComfirmBtn"))
        self.AddMissionBtn = QtGui.QPushButton(self.Curtain)
        self.AddMissionBtn.setGeometry(QtCore.QRect(280, 350, 75, 23))
        self.AddMissionBtn.setObjectName(_fromUtf8("AddMissionBtn"))
        self.MissionValue = QtGui.QLabel(self.Curtain)
        self.MissionValue.setGeometry(QtCore.QRect(650, 390, 54, 12))
        self.MissionValue.setObjectName(_fromUtf8("MissionValue"))
        self.MissionDataTime = QtGui.QDateTimeEdit(self.Curtain)
        self.MissionDataTime.setEnabled(False)
        self.MissionDataTime.setGeometry(QtCore.QRect(280, 390, 171, 22))
        self.MissionDataTime.setAutoFillBackground(False)
        self.MissionDataTime.setCalendarPopup(True)
        self.MissionDataTime.setObjectName(_fromUtf8("MissionDataTime"))
        self.DeleteMissionBtn = QtGui.QPushButton(self.Curtain)
        self.DeleteMissionBtn.setGeometry(QtCore.QRect(370, 350, 75, 23))
        self.DeleteMissionBtn.setObjectName(_fromUtf8("DeleteMissionBtn"))
        self.CancelBtn = QtGui.QPushButton(self.Curtain)
        self.CancelBtn.setEnabled(False)
        self.CancelBtn.setGeometry(QtCore.QRect(610, 350, 75, 23))
        self.CancelBtn.setObjectName(_fromUtf8("CancelBtn"))
        self.CurtainState = QtGui.QLabel(self.Curtain)
        self.CurtainState.setGeometry(QtCore.QRect(20, 330, 211, 51))
        self.CurtainState.setWordWrap(True)
        self.CurtainState.setObjectName(_fromUtf8("CurtainState"))
        self.ControlPlane.addTab(self.Curtain, _fromUtf8(""))
        self.Light = QtGui.QWidget()
        self.Light.setObjectName(_fromUtf8("Light"))
        self.ControlBtnTip = QtGui.QLabel(self.Light)
        self.ControlBtnTip.setGeometry(QtCore.QRect(80, 100, 531, 24))
        self.ControlBtnTip.setAlignment(QtCore.Qt.AlignCenter)
        self.ControlBtnTip.setObjectName(_fromUtf8("ControlBtnTip"))
        self.ControlLightBtn = QtGui.QPushButton(self.Light)
        self.ControlLightBtn.setGeometry(QtCore.QRect(300, 130, 100, 100))
        self.ControlLightBtn.setObjectName(_fromUtf8("ControlLightBtn"))
        self.ControlPlane.addTab(self.Light, _fromUtf8(""))
        self.Smog = QtGui.QWidget()
        self.Smog.setObjectName(_fromUtf8("Smog"))
        self.label_2 = QtGui.QLabel(self.Smog)
        self.label_2.setGeometry(QtCore.QRect(180, 200, 391, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ControlPlane.addTab(self.Smog, _fromUtf8(""))
        self.DateLabel = QtGui.QLabel(self.centralwidget)
        self.DateLabel.setGeometry(QtCore.QRect(10, 10, 300, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName(_fromUtf8("DateLabel"))
        self.TimeLabel = QtGui.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(490, 10, 300, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TimeLabel.setObjectName(_fromUtf8("TimeLabel"))
        self.TitleLabel = QtGui.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(0, 35, 800, 12))
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.TipLabel = QtGui.QLabel(self.centralwidget)
        self.TipLabel.setGeometry(QtCore.QRect(0, 570, 800, 14))
        self.TipLabel.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.TipLabel.setText(_fromUtf8(""))
        self.TipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TipLabel.setObjectName(_fromUtf8("TipLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionReset_Curtain = QtGui.QAction(MainWindow)
        self.actionReset_Curtain.setObjectName(_fromUtf8("actionReset_Curtain"))

        self.retranslateUi(MainWindow)
        self.ControlPlane.setCurrentIndex(0)
        QtCore.QObject.connect(self.CurtainControlSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.CurtainPos.setNum)
        QtCore.QObject.connect(self.MissionSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.MissionValue.setNum)
        QtCore.QObject.connect(self.CurtainControlSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.OnCurtainSliderReleased)
        QtCore.QObject.connect(self.AddMissionBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnCurtainAddMissionClicked)
        QtCore.QObject.connect(self.DeleteMissionBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnCurtainDeleteMissionClicked)
        QtCore.QObject.connect(self.ComfirmBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnCurtainMissionComfirmClicked)
        QtCore.QObject.connect(self.CancelBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnCurtainMissionCancelClicked)
        QtCore.QObject.connect(self.ControlPlane, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.OnControlPlaneCurrentChanged)
        QtCore.QObject.connect(self.ControlLightBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.OnLightControlBtnClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ControlCenter", None))
        self.CurtainPos.setText(_translate("MainWindow", "0", None))
        self.ControlCurtainTip.setText(_translate("MainWindow", "Control Sdiler to Set Curtain", None))
        self.MissionTitle.setText(_translate("MainWindow", "MissionTitle", None))
        self.ComfirmBtn.setText(_translate("MainWindow", "Comfirm", None))
        self.AddMissionBtn.setText(_translate("MainWindow", "Add", None))
        self.MissionValue.setText(_translate("MainWindow", "0", None))
        self.DeleteMissionBtn.setText(_translate("MainWindow", "Del", None))
        self.CancelBtn.setText(_translate("MainWindow", "Cancel", None))
        self.CurtainState.setText(_translate("MainWindow", "Control Sdiler to Set Curtain", None))
        self.ControlPlane.setTabText(self.ControlPlane.indexOf(self.Curtain), _translate("MainWindow", "Curtain", None))
        self.ControlBtnTip.setText(_translate("MainWindow", "Control Light", None))
        self.ControlLightBtn.setText(_translate("MainWindow", "Close", None))
        self.ControlPlane.setTabText(self.ControlPlane.indexOf(self.Light), _translate("MainWindow", " Light ", None))
        self.label_2.setText(_translate("MainWindow", "Functionality is under development, so stay tuned...", None))
        self.ControlPlane.setTabText(self.ControlPlane.indexOf(self.Smog), _translate("MainWindow", "  Smog  ", None))
        self.DateLabel.setText(_translate("MainWindow", "Date", None))
        self.TimeLabel.setText(_translate("MainWindow", "Time", None))
        self.TitleLabel.setText(_translate("MainWindow", "Title", None))
        self.actionReset_Curtain.setText(_translate("MainWindow", "Reset Curtain", None))

