from PyQt6.QtWidgets import *





app = QApplication([])
window = QWidget()

menu_btn = QPushButton("Меню")

line_lbl = QLabel("Картинка")
list_widg = QListWidget()
button_btn = QPushButton("Вліво")
button2_btn = QPushButton("Вправо")
button3_btn = QPushButton("Дзеркало")
button4_btn = QPushButton("Рідкість")
button5_btn = QPushButton("Ч/Б")
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

