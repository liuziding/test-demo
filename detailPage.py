from PySide6.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QGridLayout, QLabel, QVBoxLayout, QSplitter,
                               QMainWindow, QApplication, QListWidgetItem)
from PySide6.QtCore import Signal, QFile, QSize, QTimer
from PySide6.QtGui import Qt, QPixmap, QFont

from utils.commonhelper import CommonHelper
from components.parameterSetting import ParameterSetting
from components.subLineView import SubLineView
from components.subAreaView import SubAreaView

from ui.ui_detail import Ui_detail

class DetailPage(QMainWindow):
    detail_signal = Signal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_detail()
        self.ui.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        # 展示窗口左边视频列表数据
        video_list = [{"name": "1.上海简辰网络高科技有限公司"}, {"name": "2简辰科技网络有限公司"}, {"name": "3简辰科技网络有限公司"}, {"name": "4简辰科技网络有限公司"}, {"name": "简辰"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}, {"name": "简辰科技网络有限公司"}]
        self.ui.lw_video_list.clear()
        for i in range(0, len(video_list)):
            text = video_list[i]["name"]
            item = QListWidgetItem(text)
            item.setSizeHint(QSize(0, 40))
            item.setFont(QFont("Arial", 14))
            item.setToolTip(text)
            self.ui.lw_video_list.addItem(item)

        # 展示识别图片区域
        self.identify_image()

        # 展示码头识别结果区域
        self.identify_result()     

    def paramSettingClicked(self): # 点击“参数设置”按钮  信号与槽函数
        parameter_setting = ParameterSetting()
        parameter_setting.exec()
    
    def importVideoClicked(self): # 点击“导入视频”按钮  信号与槽函数
        print("你点击了导入视频按钮")
    
    def startIdentifyClicked(self): # 点击“开始识别”按钮  信号与槽函数
        print("你点击了开始识别按钮")
    
    def exportResultClicked(self): # 点击“导出结果”按钮  信号与槽函数
        print("你点击了导出结果按钮")
    
    def deleteVideoClicked(self): # 点击“删除视频”按钮  信号与槽函数
        # 删除选定的项
        selected_items = self.ui.lw_video_list.selectedItems()
        for item in selected_items:
            self.ui.lw_video_list.takeItem(self.ui.lw_video_list.row(item))

    def flushedClicked(self): # 点击“刷新”按钮  信号与槽函数
        self.setup_ui()
        self.update()
    
    def returnClicked(self): # 点击“返回”按钮  信号与槽函数
        self.detail_signal.emit("homePage")
    
    def stopClicked(self): # 点击“Stop”按钮  信号与槽函数
        print("你点击了Stop按钮")
    
    def setLinesClicked(self): # 点击“Set Lines”按钮  信号与槽函数
        line_win = SubLineView()
        # line_win.line_signal.connect(self.setLine_text)
        line_win.exec()

    def setAreaClicked(self): # 点击“Set Area”按钮  信号与槽函数
        area_win = SubAreaView()
        # area_win.area_signal.connect(self.setArea_text)
        area_win.exec()
    
    def startClicked(self): # 点击“Start”按钮  信号与槽函数
        print("你点击了Start按钮")
    
    def exportClicked(self): # 点击“Export”按钮  信号与槽函数
        print("你点击了Export按钮")
    
    def identify_image(self): # 展示识别图片区域
        self.ui.l_identify_image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("images/inside.jpg")
        pixmap_w = pixmap.width()
        pixmap_h = pixmap.height()
        label_w = self.ui.l_identify_image.width()
        label_h = self.ui.l_identify_image.height()
        ratio_w = pixmap_w / label_w
        ratio_h = pixmap_h / label_h
        if ratio_w > ratio_h:
            new_pixmap = pixmap.scaled((pixmap_w / ratio_w), (pixmap_h / ratio_w))
        else:
            new_pixmap = pixmap.scaled((pixmap_w / ratio_h), (pixmap_h / ratio_h))
        self.ui.l_identify_image.setPixmap(new_pixmap)

    def identify_result(self): # 展示码头识别结果区域
        self.ui.l_wharf_name.setText("洋山港")
        self.ui.l_goods_car_above_count.setText("18")
        self.ui.l_goods_car_under_count.setText("28")
        self.ui.l_project_car_above_count.setText("38")
        self.ui.l_project_car_under_count.setText("48")

    def resizeEvent(self, evt):
        if self.ui.l_actual_video:
            timer = QTimer(self)
            timer.setSingleShot(True)  # 设置为单次触发
            timer.timeout.connect(self.showImage)
            timer.start(100)  # 0.1秒后触发

        super().resizeEvent(evt)

    def showImage(self): # 展示图片
        self.ui.l_actual_video.setAlignment(Qt.AlignCenter)
        self.ui.l_original_video.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("images/inside.jpg")
        pixmap_w = pixmap.width()
        pixmap_h = pixmap.height()
        label_w = self.ui.l_actual_video.width() - 10
        label_h = self.ui.l_actual_video.height() - 10
        ratio_w = pixmap_w / label_w
        ratio_h = pixmap_h / label_h
        if ratio_w > ratio_h:
            new_pixmap = pixmap.scaled((pixmap_w / ratio_w), (pixmap_h / ratio_w))
        else:
            new_pixmap = pixmap.scaled((pixmap_w / ratio_h), (pixmap_h / ratio_h))
            
        self.ui.l_actual_video.setPixmap(new_pixmap)
        self.ui.l_original_video.setPixmap(new_pixmap)
        
