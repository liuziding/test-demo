from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Widget")

        # 创建 QStandardItemModel 模型
        self.model = QStandardItemModel(self)

        # 向模型中添加数据
        for i in range(10):
            item = QStandardItem(f"Item {i}")
            item.setCheckable(True)
            self.model.appendRow(item)

        # 创建 QListView 组件并将模型设置为其数据源
        self.list_view = QListView(self)
        self.list_view.setModel(self.model)

        # 创建用于批量删除的按钮
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.delete_items)

        # 创建用于显示选中项的标签
        self.label = QLabel(self)

        # 将组件添加到布局中
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_view)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.label)

        # 连接项选择事件
        self.list_view.selectionModel().selectionChanged.connect(self.show_selected_item)

    def delete_items(self):
        # 获取所有选中项的索引
        indexes = self.list_view.selectedIndexes()

        # 从模型中删除选中项
        for index in reversed(indexes):
            self.model.removeRow(index.row())

    def show_selected_item(self):
        # 获取当前选中项的索引
        index = self.list_view.currentIndex()

        # 如果有选中项，显示其文本
        if index.isValid():
            item = self.model.itemFromIndex(index)
            self.label.setText(item.text())
        else:
            self.label.setText("No item selected")

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
