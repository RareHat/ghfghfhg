import os
from PIL import Image, ImageFilter
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import *


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap





class PhotoManager:
    def  __init__(self):
        self.photo = None
        self.folder = None
        self.filename = None

    def load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)
    def show_show(self,image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)


    def bw(self):
        self.photo = self.photo.convert("L")
        self.show_image(self.image_lbl)

    def sharp(self):
        self.photo = self.filter(ImageFilter.SHARPEN)
        self.show_image(self.image_lbl)

    def right(self):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.show_image(self.image_lbl)

    def kontur(self):
        self.photo = self.filter(ImageFilter.CONTOUR)
        self.show_image(self.image_lbl)

    def flip(self):
        self.photo = self.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_image(self.image_lbl)

    def Edge(self):
        self.photo = self.filter(ImageFilter.EDGE_ENHANCE)
        self.show_image(self.image_lbl)

    def Bright(self):
        self.photo = self.ImageEnhance.Brightness(image_lbl).enhance(1.5)
        self.show_image(self.image_lbl)

    def blur(self):
        self.photo = self.ImageEnhance.Brightness().enhance(1.5)
        self.show_image(self.image_lbl)




app = QApplication([])
window = QWidget()

menu_btn = QPushButton("Меню")

line_lbl = QLabel("Картинка")
list_widg = QListWidget()
button_btn = QPushButton("Яскравість 50%")
button2_btn = QPushButton("Розмивання")
button3_btn = QPushButton("Дзеркало")
button4_btn = QPushButton("Яскравість 50%")
button5_btn = QPushButton("Ч/Б")
button6_btn = QPushButton("Накладання контурів")
button7_btn = QPushButton("Збільшення різкості")
button8_btn = QPushButton("Покращення ребер")
buttonv2_btn = QPushButton("Папка")

main_line = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(buttonv2_btn)
v1.addWidget(list_widg)
main_line.addLayout(v1)


v3 = QVBoxLayout()
v3.addWidget(line_lbl)

v2 = QHBoxLayout()
v2.addWidget(button_btn)
v2.addWidget(button2_btn)
v2.addWidget(button3_btn)
v2.addWidget(button4_btn)
v2.addWidget(button5_btn)
v3.addLayout(v2)

photo_manager = PhotoManager()
photo_manager.image_lbl = line_lbl

def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(photo_manager.folder)
    list_widg.clear()
    list_widg.addItems(files)

def show_chosen_image():
    photo_manager.filename = list_widg.currentItem().text()
    photo_manager.load()
    photo_manager.show_image(line_lbl)

list_widg.currentRowChanged.connect(show_chosen_image)


buttonv2_btn.clicked.connect(open_folder)
button5_btn.clicked.connect(photo_manager.bw)
button7_btn.clicked.connect(photo_manager.sharp())
button8_btn.clicked.connect(photo_manager.Edge)
button4_btn.clicked.connect(photo_manager.Bright())
button5_btn.clicked.connect(photo_manager.blur())
button3_btn.clicked.connect(photo_manager.flip)
button6_btn.clicked.connect(photo_manager.kontur)
button5_btn.clicked.connect(photo_manager.right)

main_line.addLayout(v3)

app.setStyleSheet("""
        QWidget{
            background: #3C3D37;
        }
            
        QPushButton
        {      
            background-color: #697565;
            border-style: dashed;
            font-family: Gadugi;
            min-width: 6em;
            padding: 6px
        }
    """)

















window.setLayout(main_line)
window.show()
app.exec()

