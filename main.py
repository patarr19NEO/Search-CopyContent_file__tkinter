from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

def searchTxt():
    entry_one = entry1.get()
    try:
        messagebox.showinfo("Идет поиск", "Идет поиск файла... Это может занять некоторое время")
        for root, dirs, files in os.walk("D:\\"): # for example
            if entry_one in files:
                filePath = os.path.join(root, entry_one)
                with open(filePath, "r", encoding = "utf-8") as from_file:
                    fileContent = from_file.read()
                    with open("copied.txt", "w", encoding = "utf-8") as to_file:
                        to_file.write(fileContent)
                messagebox.showinfo("Успех!", f"Сожеримое из {entry_one} успешно скопировано в copied.txt")
                break
            else:
                messagebox.showerror("Ошибко!", f"Файл {entry_one} не найден!")
                break
    except Exception as e:
        error = str(e)
        messagebox.showerror("Ошибко!", f"Произошла ошибка: {error}")

def seacrhImgVid():
    entry_two = entry2.get()
    try:
        messagebox.showinfo("Идет поиск", "Идет поиск файла...")
        for root, dirs, files in os.walk("D:\\"): # for example
            if entry_two in files:
                filePath = os.path.join(root, entry_two)
                with open(filePath, "r") as from_file:
                    fileContent = from_file.read()
                    with open("copiedImgVid.png", "w") as to_file:
                        to_file.write(fileContent)
                messagebox.showinfo("Успех!", f"Содержимое png картинки {entry_two} успешно скопировано в copiedImgVid.png")
                break
            else:
                messagebox.showerror("Ошибко!", f"Файл {entry_two} не найден!  ")
                break
    except Exception as e:
        error = str(e)
        messagebox.showerror("Ошибко!" ,f"Произошла ошибка: {error}")

window = Tk()
window.title("Search File")
window.geometry("470x200")

text1 = ttk.Label(text = "Поиск и просмотр содержимого txt файла:", font = ("Arial", 15))
text1.place(x = 10, y = 10)

entry1 = ttk.Entry()
entry1.place(x = 10, y = 40)

btn1 = ttk.Button(text = "Найти", command = searchTxt)
btn1.place(x = 150, y = 40)

text2 = ttk.Label(text = "Поиск и просмотр содержимого png файла:", font = ("Arial", 15))
text2.place(x = 10, y = 90)

entry2 = ttk.Entry()
entry2.place(x = 10, y = 120)

btn2 = ttk.Button(text = "Найти", command = seacrhImgVid)
btn2.place(x = 150, y = 120)

text3 = ttk.Label(text = "Создатель: patarr19")
text3.place(x = 10, y = 170)

text3 = ttk.Label(text = "v1.1")
text3.place(x = 10, y = 150)

window.mainloop()
