from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

app = QApplication([])

label = QLabel()
pixmap = QPixmap("images/inside.jpg")

# 计算图片的宽高比和边框的宽高比
image_ratio = pixmap.width() / pixmap.height()
label_ratio = label.width() / label.height()

# 如果图片的宽高比大于边框的宽高比，则使用边框的宽度作为图片的宽度
if image_ratio > label_ratio:
    pixmap = pixmap.scaledToWidth(label.width())
# 否则使用边框的高度作为图片的高度
else:
    pixmap = pixmap.scaledToHeight(label.height())

label.setPixmap(pixmap)
label.setAlignment(Qt.AlignCenter)

label.setFixedSize(200, 200)  # 设置固定大小

label.show()
app.exec()
