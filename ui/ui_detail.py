# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_detail(object):
    def setupUi(self, detail):
        if not detail.objectName():
            detail.setObjectName(u"detail")
        detail.resize(1328, 1002)
        detail.setStyleSheet(u"QWidget#MainWindow {\n"
"	background: #FFF;\n"
"}")
        self.w_detail_window = QWidget(detail)
        self.w_detail_window.setObjectName(u"w_detail_window")
        self.verticalLayout_4 = QVBoxLayout(self.w_detail_window)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.w_detail_window)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 48))
        self.frame.setMaximumSize(QSize(16777215, 48))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.horizontalSpacer = QSpacerItem(690, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.frame)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lw_video_list = QListWidget(self.w_detail_window)
        self.lw_video_list.setObjectName(u"lw_video_list")
        self.lw_video_list.setMinimumSize(QSize(210, 0))
        self.lw_video_list.setMaximumSize(QSize(210, 16777215))
        self.lw_video_list.setAutoScrollMargin(16)

        self.horizontalLayout_9.addWidget(self.lw_video_list)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.l_actual_video = QLabel(self.w_detail_window)
        self.l_actual_video.setObjectName(u"l_actual_video")
        self.l_actual_video.setStyleSheet(u"QWidget#l_actual_video {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.verticalLayout.addWidget(self.l_actual_video)

        self.frame_2 = QFrame(self.w_detail_window)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 48))
        self.frame_2.setMaximumSize(QSize(16777215, 48))
        self.frame_2.setStyleSheet(u"QWidget#frame_2 {\n"
"	border-left: 0;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.l_original_video = QLabel(self.w_detail_window)
        self.l_original_video.setObjectName(u"l_original_video")
        self.l_original_video.setStyleSheet(u"QWidget#l_original_video {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.verticalLayout.addWidget(self.l_original_video)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.l_identify_image = QLabel(self.w_detail_window)
        self.l_identify_image.setObjectName(u"l_identify_image")
        self.l_identify_image.setMinimumSize(QSize(400, 225))
        self.l_identify_image.setMaximumSize(QSize(400, 225))
        self.l_identify_image.setStyleSheet(u"QWidget#l_identify_image {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.verticalLayout_3.addWidget(self.l_identify_image)

        self.w_identify_result = QWidget(self.w_detail_window)
        self.w_identify_result.setObjectName(u"w_identify_result")
        self.w_identify_result.setMinimumSize(QSize(400, 500))
        self.w_identify_result.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayoutWidget_2 = QWidget(self.w_identify_result)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-1, 30, 401, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.l_wharf_name = QLabel(self.horizontalLayoutWidget_2)
        self.l_wharf_name.setObjectName(u"l_wharf_name")

        self.horizontalLayout_4.addWidget(self.l_wharf_name)

        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.layoutWidget = QWidget(self.w_identify_result)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 150, 356, 161))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.l_goods_car_above_count = QLabel(self.layoutWidget)
        self.l_goods_car_above_count.setObjectName(u"l_goods_car_above_count")
        self.l_goods_car_above_count.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_5.addWidget(self.l_goods_car_above_count)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.l_goods_car_under_count = QLabel(self.layoutWidget)
        self.l_goods_car_under_count.setObjectName(u"l_goods_car_under_count")
        self.l_goods_car_under_count.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_8.addWidget(self.l_goods_car_under_count)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.l_project_car_above_count = QLabel(self.layoutWidget)
        self.l_project_car_above_count.setObjectName(u"l_project_car_above_count")
        self.l_project_car_above_count.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_7.addWidget(self.l_project_car_above_count)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.l_project_car_under_count = QLabel(self.layoutWidget)
        self.l_project_car_under_count.setObjectName(u"l_project_car_under_count")
        self.l_project_car_under_count.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_6.addWidget(self.l_project_car_under_count)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addWidget(self.w_identify_result)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        detail.setCentralWidget(self.w_detail_window)
        self.menubar = QMenuBar(detail)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1328, 24))
        detail.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(detail)
        self.statusbar.setObjectName(u"statusbar")
        detail.setStatusBar(self.statusbar)

        self.retranslateUi(detail)
        self.pushButton.clicked.connect(detail.paramSettingClicked)
        self.pushButton_6.clicked.connect(detail.importVideoClicked)
        self.pushButton_5.clicked.connect(detail.startIdentifyClicked)
        self.pushButton_4.clicked.connect(detail.exportResultClicked)
        self.pushButton_3.clicked.connect(detail.deleteVideoClicked)
        self.pushButton_2.clicked.connect(detail.flushedClicked)
        self.pushButton_7.clicked.connect(detail.returnClicked)
        self.pushButton_13.clicked.connect(detail.stopClicked)
        self.pushButton_12.clicked.connect(detail.setLinesClicked)
        self.pushButton_11.clicked.connect(detail.setAreaClicked)
        self.pushButton_10.clicked.connect(detail.startClicked)
        self.pushButton_9.clicked.connect(detail.exportClicked)

        QMetaObject.connectSlotsByName(detail)
    # setupUi

    def retranslateUi(self, detail):
        detail.setWindowTitle(QCoreApplication.translate("detail", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("detail", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.pushButton_6.setText(QCoreApplication.translate("detail", u"\u5bfc\u5165\u89c6\u9891", None))
        self.pushButton_5.setText(QCoreApplication.translate("detail", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.pushButton_4.setText(QCoreApplication.translate("detail", u"\u5bfc\u51fa\u7ed3\u679c", None))
        self.pushButton_3.setText(QCoreApplication.translate("detail", u"\u5220\u9664\u89c6\u9891", None))
        self.pushButton_2.setText(QCoreApplication.translate("detail", u"\u5237\u65b0", None))
        self.pushButton_7.setText(QCoreApplication.translate("detail", u"\u8fd4\u56de", None))
        self.l_actual_video.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("detail", u"Stop", None))
        self.pushButton_12.setText(QCoreApplication.translate("detail", u"Set Lines", None))
        self.pushButton_11.setText(QCoreApplication.translate("detail", u"Set Area", None))
        self.pushButton_10.setText(QCoreApplication.translate("detail", u"Start", None))
        self.pushButton_9.setText(QCoreApplication.translate("detail", u"Export", None))
        self.l_original_video.setText("")
        self.l_identify_image.setText("")
        self.l_wharf_name.setText("")
        self.label.setText(QCoreApplication.translate("detail", u"\u7801\u5934\u8bc6\u522b\u7ed3\u679c\u5b9e\u65f6\u5c55\u793a\u533a", None))
        self.label_2.setText(QCoreApplication.translate("detail", u"\u5546\u54c1\u8f66\u4e0a\u8239\u8ba1\u6570\uff1a", None))
        self.l_goods_car_above_count.setText("")
        self.label_8.setText(QCoreApplication.translate("detail", u"\u5546\u54c1\u8f66\u4e0a\u8239\u8ba1\u6570\uff1a", None))
        self.l_goods_car_under_count.setText("")
        self.label_6.setText(QCoreApplication.translate("detail", u"\u5546\u54c1\u8f66\u4e0a\u8239\u8ba1\u6570\uff1a", None))
        self.l_project_car_above_count.setText("")
        self.label_4.setText(QCoreApplication.translate("detail", u"\u5546\u54c1\u8f66\u4e0a\u8239\u8ba1\u6570\uff1a", None))
        self.l_project_car_under_count.setText("")
    # retranslateUi

