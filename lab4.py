from tkinter import *
import random

def clicked():  #Функция активации кнопки
    #res = "Ваш ключ: {}".format(txt.get())
    #lbl.configure(text=res)


    latt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig = '1234567890'

    number = 4  # Кол-во парольных групп
    length = 4  # Кол-во символов в пароле

    for n in range(number):
        p = ''
        pas = []
        passw = []
        password = ''
        d = random.choice(dig)

        for i in range(length - 1):
            p += random.choice(latt)
            pas = list(p + d)

            random.shuffle(pas)  # Перемешиваем случайным образом

        passw += list(pas)  # Преобразуем из строки в списки

        password = ("".join(passw))

        #print(password, end='  ')  # Печатаем в строку
    res = "Ваш ключ: {}".format(password, end=" ")
    lbl.configure(text=res)
    #return



#Откроем окно
window = Tk()
window.title("ГЕНЕРАТОР КЛЮЧА") #Название окна
window.geometry('800x450')#Размер окна в пикселях
window.resizable(width=False, height=False)

bg = PhotoImage(file="ARK.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)


lbl = Label(window, text="Нажми Пуск", font=("Arial Bold", 16), fg="red")#Текстовое поле в окне, шрифт и его размер
lbl.place(x=250, y=60) #Положение надписи в окне

#txt = Entry(window, width=50)  #Текстовое поле и его размер, длина строки
#txt.place(x=140, y=120)  #Положение текстового поля
#txt.focus() #Фокус на текстовое поле

btn = Button(window, text="Пуск", font=('Arial Bold', 20), height= 1, width= 10, bg="green", command=clicked) #Кнопка и ее внешний вид
btn.place(x=250, y=225) #Положение кнопки в пикселях
btn.focus() #Фокус на кнопку


window.mainloop()
