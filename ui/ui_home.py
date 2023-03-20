# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(800, 749)
        home.setWindowOpacity(7.000000000000000)
        self.centralwidget = QWidget(home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 48))
        self.frame.setMaximumSize(QSize(16777215, 48))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.SplitHCursor))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.w_grid = QWidget(self.centralwidget)
        self.w_grid.setObjectName(u"w_grid")
        self.w_grid.setMinimumSize(QSize(800, 600))
        self.w_grid.setMaximumSize(QSize(16777215, 16777215))
        self.w_grid.setStyleSheet(u"QWidget#w_grid {\n"
"	border: 1px solid #BEBEBE;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.w_grid)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gl_video_content = QGridLayout()
        self.gl_video_content.setSpacing(0)
        self.gl_video_content.setObjectName(u"gl_video_content")

        self.verticalLayout.addLayout(self.gl_video_content)


        self.verticalLayout_2.addWidget(self.w_grid)

        home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        home.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(home)
        self.statusbar.setObjectName(u"statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)
        self.pushButton.clicked.connect(home.paramSettingClicked)
        self.pushButton_5.clicked.connect(home.increaseVideoClicked)
        self.pushButton_4.clicked.connect(home.decreaseVideoClicked)
        self.pushButton_3.clicked.connect(home.flushedClicked)
        self.pushButton_2.clicked.connect(home.quitClicked)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"\u4e3b\u7a97\u53e3", None))
        self.pushButton.setText(QCoreApplication.translate("home", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.pushButton_5.setText(QCoreApplication.translate("home", u"\u52a0\u9891", None))
        self.pushButton_4.setText(QCoreApplication.translate("home", u"\u51cf\u9891", None))
        self.pushButton_3.setText(QCoreApplication.translate("home", u"\u5237\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("home", u"\u9000\u51fa", None))
    # retranslateUi

