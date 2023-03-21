import sys

from PySide6.QtWidgets import (QGraphicsView, QDialog, QGraphicsScene, QGraphicsPixmapItem, QHBoxLayout,
    QPushButton, QLabel, QVBoxLayout, QGraphicsPolygonItem, QMessageBox)
from PySide6.QtGui import Qt, QPen, QBrush, QPixmap
from PySide6.QtCore import Signal

from components.model.polygon_ui import Ui_SubWindow
from utils.commonhelper import CommonHelper

area_point = [] # 将点的坐标储存进此数组中

class SubAreaView(QDialog, Ui_SubWindow):
    area_signal = Signal(str)       # 子窗信号，用于传递用户名
    def __init__(self,parent = None):
        super(SubAreaView, self).__init__(parent)
        # 设置样式
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))
        self.setWindowTitle('画线')
        self.resize(1030,650)
        layout = QHBoxLayout()
        self.cancel_btn = QPushButton("取消")
        self.commit_btn = QPushButton('提交')
        self.cancel_btn.setObjectName("lineSetting")
        self.commit_btn.setObjectName("lineSetting")
        self.cancel_btn.setProperty("button", "cancel")
        self.commit_btn.setProperty("button", "submit")
        # 设置按钮手状
        self.cancel_btn.setCursor(Qt.PointingHandCursor)
        self.commit_btn.setCursor(Qt.PointingHandCursor)

        # 设置弹簧
        layout.addStretch()
        layout.addWidget(self.cancel_btn)
        layout.addWidget(self.commit_btn)
        layout.addStretch()

        self.area_label = QLabel()

        self.graphicsview = GraphicsView()
        self.graphicsview.setFixedSize(970, 550)
        self.graphicsview.setContentsMargins(0,0,0,0)
        self.graphicsview.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        lay = QVBoxLayout(self.area_label)
        lay.addWidget(self.graphicsview)

        pixmap = QPixmap("./images/inside.jpg")
        new_pixmap = pixmap.scaled(pixmap.width() // 2, pixmap.height() // 2)
        self.graphicsview.setPixmap(new_pixmap)


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.area_label)
        main_layout.addLayout(layout)
        self.setLayout(main_layout)

        self.commit_btn.clicked.connect(self.get_coordinate)      # 取消按钮 关连信号发信槽函数
        self.cancel_btn.clicked.connect(self.click_cancel_btn)    # 提交按钮 关连信号发信槽函数
 
    # 定义槽函数，用于获取线的坐标参数
    def get_coordinate(self):
        if len(area_point) < 3:
            QMessageBox.warning(self, "警告", "您还没有画区域")
        else:
            str = repr(area_point)
            self.area_signal.emit(str)        # 发射信号
            self.close()    # 发射完信号后关闭窗口

    def click_cancel_btn(self):
        self.close() # 关闭窗口

    def closeEvent(self, QCloseEvent):
        area_point.clear() # 将点的坐标储存进此数组中

class GraphicsView(QGraphicsView):
    def __init__(self, parent = None):
        super().__init__(parent)
        scene = QGraphicsScene(self)
        self.setScene(scene)
        self._pixmap_item = QGraphicsPixmapItem()
        scene.addItem(self.pixmap_item)

        layout = QVBoxLayout() # 垂直布局
        self.label = QLabel() # 标签类
        layout.addWidget(self.label)

        self._polygon_item = QGraphicsPolygonItem(self.pixmap_item)
        self.polygon_item.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        self.polygon_item.setBrush(QBrush(Qt.red, Qt.VerPattern))

    @property
    def pixmap_item(self):
        return self._pixmap_item

    @property
    def polygon_item(self):
        return self._polygon_item

    def setPixmap(self, pixmap):
        self.pixmap_item.setPixmap(pixmap)

    def resizeEvent(self, event):
        self.fitInView(self.pixmap_item, Qt.KeepAspectRatio)
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        sp = self.mapToScene(event.pos())
        lp = self.pixmap_item.mapFromScene(sp)
        area_point.append([x, y])
        poly = self.polygon_item.polygon()
        poly.append(lp)
        self.polygon_item.setPolygon(poly)

    
