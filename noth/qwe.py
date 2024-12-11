import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(("Text files", "*.txt"), 'Все файлы'))
    text['text'] = text['text'] + filename
    print(filename)
    return filename


window = tkinter.Tk()
window.title("Проводник")
window.geometry("470x300")
window.configure(background='lightgrey')
window.resizable(False, False)
text = tkinter.Label(window, text="Файл:", height=5, width=70, background='silver', foreground='green')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=5, text="Выбрать файл", background='silver',
                               foreground='green', command=file_select)
button_select.grid(column=1, row=2)
window.mainloop()
