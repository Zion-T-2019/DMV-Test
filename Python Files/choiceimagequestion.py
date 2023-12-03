from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class ChoiceImageQuestion:
    def init(self):
        self._image = None
        self._pic_label = None

    def set_image(self, img_path):
        img_bytes = open(img_path, "rb").read()
        self._image = QImage()
        self._image.loadFromData(img_bytes)

    def display(self, layout, w, h):
        if self._image is not None:
            if self._pic_label is None:
                self._pic_label = QLabel()
                layout.addWidget(self._pic_label)

            pixmap = QPixmap.fromImage(self._image)
            scaled_img = pixmap.scaled(w, h, Qt.KeepAspectRatio)
            self._pic_label.setPixmap(scaled_img)
            self._pic_label.setAlignment(Qt.AlignCenter)