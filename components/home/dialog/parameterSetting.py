import sys

from PySide6.QtWidgets import (QDialog, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit,
    QFormLayout, QGroupBox, QMessageBox)
from PySide6.QtGui import Qt
from PySide6.QtCore import QFile

from utils.commonhelper import CommonHelper

class ParameterSetting(QDialog):
    def __init__(self, parent = None):
        super(ParameterSetting, self).__init__(parent)
        self.setFixedSize(600, 400)
        self.setWindowTitle("参数配置")
        # 设置样式
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))

        # 加载样式表文件
        # file = QFile("qss/app.qss")
        # file.open(QFile.ReadOnly | QFile.Text)
        # stylesheet = file.readAll().data().decode('utf-8')

        # 设置主窗口布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # 创建输入框和按钮
        self.connection_name_input = QLineEdit(self) # 连接名
        self.host_input = QLineEdit(self) # 主机
        self.port_input = QLineEdit(self) # 端口
        self.username_input = QLineEdit(self) # 用户名
        self.password_input = QLineEdit(self) # 密码
        self.database_name_input = QLineEdit(self) # 数据库名
        add_button = QPushButton("确定", self) # 确认按钮
        cancel_button = QPushButton("取消", self) # 取消按钮

        # 设置属性
        self.connection_name_input.setObjectName("paramSetting")
        self.host_input.setObjectName("paramSetting")
        self.port_input.setObjectName("paramSetting")
        self.username_input.setObjectName("paramSetting")
        self.password_input.setObjectName("paramSetting")
        self.database_name_input.setObjectName("paramSetting")
        add_button.setObjectName("paramSetting")
        add_button.setProperty("button", "submit")
        cancel_button.setObjectName("paramSetting")
        cancel_button.setProperty("button", "cancel")

        # 设置按钮手状样式
        add_button.setCursor(Qt.PointingHandCursor)
        cancel_button.setCursor(Qt.PointingHandCursor)

        # 将输入框和按钮添加到表单布局中
        form_layout = QFormLayout()
        form_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        form_layout.addRow(QLabel('<b>连接名:</b>'), self.connection_name_input)
        form_layout.addRow(QLabel('<b>主机:</b>'), self.host_input)
        form_layout.addRow(QLabel('<b>端口:</b>'), self.port_input)
        form_layout.addRow(QLabel('<b>用户名:</b>'), self.username_input)
        form_layout.addRow(QLabel('<b>密码:</b>'), self.password_input)
        form_layout.addRow(QLabel('<b>数据库名:</b>'), self.database_name_input)

        # 设置输入框与输入框之间的间距
        form_layout.setVerticalSpacing(20)

        # 创建一个组框，并将表单布局添加到组框中
        group_box = QGroupBox('', self)
        group_box.setLayout(form_layout)

        # 创建一个水平布局，并将注册按钮添加到其中
        button_layout = QHBoxLayout()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(add_button)
        button_layout.setAlignment(Qt.AlignRight)

        # 将组框和按钮布局添加到主窗口布局中
        main_layout.addWidget(group_box)
        main_layout.addLayout(button_layout)

        # 点击添加按钮 信号到槽函数
        add_button.clicked.connect(self.add_button_clicked)

        # 点击取消按钮关闭Dialog窗口 信号到槽函数
        cancel_button.clicked.connect(self.reject)

    def add_button_clicked(self): # 点击添加按钮 显示消息框
        if not self.connection_name_input.text():
            QMessageBox.warning(self, "警告", "连接名不能为空")
        elif not self.host_input.text():
            QMessageBox.warning(self, "警告", "主机不能为空")
        elif not self.port_input.text():
            QMessageBox.warning(self, "警告", "端口不能为空")
        elif not self.username_input.text():
            QMessageBox.warning(self, "警告", "用户名不能为空")
        elif not self.password_input.text():
            QMessageBox.warning(self, "警告", "密码不能为空")
        elif not self.database_name_input.text():
            QMessageBox.warning(self, "警告", "数据库名不能为空")    
        else:
            QMessageBox().information(self, "提示", 'submit successful!')
            self.clearInput()

    def clearInput(self): # 清空输入框
        self.connection_name_input.clear()
        self.host_input.clear()
        self.port_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.database_name_input.clear()