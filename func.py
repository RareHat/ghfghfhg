from PIL import Image, ImageFilter, ImageEnhance
#from PyQt5.QtWidgets import
#from PyQt6.QtWidgets import *
#from PyQt5 import *


img = Image.open("644a55c7d04e3ac40564955994151de0-removebg-preview.png")



while True:
    print("1. Показати зображення")
    print("2. Зберегти зображення")
    print("3. Зробити ч/б")
    print("4. Розмивання")
    print("5. Віддзеркалення по горизонталі")
    print("6. збільшення яскравості на 50%")
    print("7. збільшення контрастності на 50%")
    print("8. збільшення насиченості на 50%")
    operation = input("Введіть операцію")
    if operation == "1":
        img.show()
    elif operation == "2":
        name = input("Введіть назву файлу")
        img.save(name)
    elif operation == "3":
        img = img.convert("L")
    elif operation == "4":
        img = img.filter(ImageFilter.BLUR)
    elif operation == "8":
        img = ImageEnhance.Color(img).enhance(1.5)
    elif operation == "5":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif operation == "6":
        img = ImageEnhance.Brightness(img).enhance(1.5)
    elif operation == "7":
        img = ImageEnhance.Contrast(img).enhance(1.5)

