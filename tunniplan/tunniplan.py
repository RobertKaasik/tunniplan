from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox as mb
from random import *
import time, sys
from Fail import *
users=[]
password=[]
users=loe_failist_listisse("users.txt",users)
password=loe_failist_listisse("pass.txt",password)
root = Tk()
def fail():
    global login
    global pas
    global users
    global password
    Label(aken1,text="Придумайте\nЛогин:").grid(row=0, column=0)
    login = Entry(aken1,width=15)
    login.grid(row=0, column=1)
    Label(aken1,text="Придумайте\nПароль:").grid(row=1, column=0)
    pas = Entry(aken1,width=15)
    pas.grid(row=1, column=1)
    Label(aken1,text=" ").grid(row=2, column=4)
    Label(aken1,text=" ").grid(row=2, column=5)
    users.append(login.get())
    password.append(pas.get())  

def log():
    if (login not in users) or (login in users):
	Label(aken1,text="Вы зарегестрировали логин!").grid(row=1,column=1)
	users=rida_salvestamine("users.txt",login)
	Label(aken1,text="Такой логин существует!").grid(row=1,column=2)

def reg():
    root.destroy()
    global login
    global pas
    global users
    global password
    aken1=Tk()
    Label(aken1,text="Придумайте\nЛогин:").grid(row=0, column=0)
    login = Entry(aken1,width=15)
    login.grid(row=0, column=1)
    Label(aken1,text="Придумайте\nПароль:").grid(row=1, column=0)
    pas = Entry(aken1,width=15)
    pas.grid(row=1, column=1)
    Label(aken1,text=" ").grid(row=2, column=4)
    Label(aken1,text=" ").grid(row=2, column=5)
    users.append(login.get())
    password.append(pas.get())  
    Button(text="Выйте",command=exit1).grid(row=2,column=1)
    Button(text="Породолжить",command=fail).grid(row=2,column=1)

def avt():
    root.destroy()  
    aken2=Tk(   )
    Label(aken2,text="Впишите\nЛогин:").grid(row=0, column=0)
    login = Entry(aken2,width=15)
    login.grid(row=0, column=1)
    Label(aken2,text="Впишите\nПароль:").grid(row=1, column=0)
    pas = Entry(aken2,width=15  )
    pas.grid(row=1, column=1)
    Button(aken2,text="Продолжить").grid(row=2, column=1)
    Label(aken2,text=" ").grid(row=2, column=4)
    Label(aken2,text=" ").grid(row=2, column=5)
    Button(text="Выйте",command=exit3).grid(row=2,column=1)
    Button(text="Породолжить",command=fail).grid(row=2,column=1)

def exit():
    if askyesno("Вопрос","Хотите вы выйти?"):
         reg.destroy()
def exit2():
    if askyesno("Вопрос" ,"Хотите ли вы выйти?"):
        root.destroy()
def exit3():
    if askyesno("Вопрос","Хотите вы выйти?"):
         avt.destroy()

def clas():
	showinfo(title="Классный час",message="Доп.урок\n Учитель - Laaneväli-Toots Alina\n Кабинет в 236")
def estõ():
	showinfo(title="Доп.Эстонский",message="Доп.урок\n Учитель - Laaneväli-Toots Alina\n Кабинет B 236")
def log():
	showinfo(title="Логистика",message="Основной урок\n Учитель - Inessa Klemanskaja\n Кабинет B 002")
def mat():
	showinfo(title="Математика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет B 133")
def matõ():
	showinfo(title="Доп.Математика",message="Доп.урок\n Учитель - Nadewda Voronova\n Кабинет B 133")
def rus():
	showinfo(title="Русский",message="Основной урок\n Учитель - Ljudmila Mikhailova\n Кабинет B 221")
def kem():
	showinfo(title="Доп.Химия",message="Основной урок\n Учитель - Svetlana Pesestkaja\n Кабинет B 144")
def pro():
	showinfo(title="Програмирование",message="Основной урок\n Учитель - Marina Oleinik\n Кабинет E 07")
def fuüsik():
	showinfo(title="Физика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет B 133")
def kunst():
	showinfo(title="Исскуство",message="Основной урок\n Учитель - Aleksandrova\n Кабинет B 232")
def sport():
	showinfo(title="Физкультура",message="Основной урок\n Учитель - Maksim\n Кабинет Zal A")
def merkulova():
	showinfo(title="Ракендусттарквара",message="Основной урок\n Учитель - Merkulova\n Кабинет E 10")
def est():
	showinfo(title="Эстонский",message="Основной урок\n Учитель - Laaneväli-Toots Alina\n Кабинет B 236")
def angõ():
	showinfo(title="Доп.Английский",message="Доп.урок\n Учитель - Olga Borodina\n Кабинет B 227")
def eng():
	showinfo(title="Английский",message="Основной урок\n Учитель - Olga Borodina\n Кабинет B 227")

def plan():
    #Описание уроков
    #Время и счет урока
    Label(text="0",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=1)
    Label(text="1",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=2)
    Label(text="2",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=3)
    Label(text="3",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=4)
    Label(text="4",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=5)
    Label(text="5",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=6)
    Label(text="6",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=7)
    Label(text="7",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=8)
    Label(text="8",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=9)
    Label(text="9",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=10)
    Label(text="10",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=0, column=11)
    #пустая строка в углу
    Label(text=" ",font="Arial 13",width=10,height=3,relief=RIDGE).grid(row=0, column=0)
    #Дни
    Label(text="Esmaspäev",font="Arial 13",width=10,height=7,relief=RIDGE).grid(row=1, column=0, rowspan=2)
    Label(text="Teisipäev",font="Arial 13",width=10,height=7,relief=RIDGE).grid(row=3, column=0, rowspan=2)
    Label(text="Kolmapäev",font="Arial 13",width=10,height=7,relief=RIDGE).grid(row=5, column=0, rowspan=2)
    Label(text="Neljapäev",font="Arial 13",width=10,height=7,relief=RIDGE).grid(row=7, column=0, rowspan=2)
    Label(text="Reede",font="Arial 13",width=10,height=7,relief=RIDGE).grid(row=9, column=0, rowspan=2)

    #Нулевой урок
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=1, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=2, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=3, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=4, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=5, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=7, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=8, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=9, column=1)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=10, column=1)

    #Понедельник row=вниз column=право
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=1, column=2)
    Button(text="Eesti Keel\n(Tugiõpe)",bg="pink",font="Arial 13",width=11,height=3,relief=RIDGE,command=estõ).grid(row=2, column=2)
    Button(text="Logistikateenused\n ja varude juhtmine",bg="green",font="Arial 13",width=23,height=6,relief=RIDGE,command=log).grid(row=1, column=3,columnspan=2,rowspan=2)
    Button(text="Matemaatika",bg="pink",font="Arial 13",width=11,height=6,relief=RIDGE,command=mat).grid(row=1, column=5,rowspan=2)
    Button(text="Matemaatika",bg="pink",font="Arial 13",width=11,height=6,relief=RIDGE,command=mat).grid(row=1, column=6,rowspan=2)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=2, column=7)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=1, column=7)   
    Button(text="Keel ja\n kirjandus",bg="green",font="Arial 13",width=11,height=6,relief=RIDGE,command=rus).grid(row=1, column=8,rowspan=2)
    Button(text="Keel ja\n kirjandus",bg="green",font="Arial 13",width=11,height=6,relief=RIDGE,command=rus).grid(row=1, column=9,rowspan=2)
    Button(text="Matemaatika\n(Tugiõpe)",bg="pink",font="Arial 13",width=11,height=6,relief=RIDGE,command=matõ).grid(row=1, column=10,rowspan=2)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=2, column=11)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=1, column=11) 

    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=1, column=11)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=2, column=11)

    #Вторник
    Button(text="Tugiõpe\n(Keemia)",bg="pink",font="Arial 13",width=11,height=6,relief=RIDGE,command=kem).grid(row=3, column=2,rowspan=2)
    Button(text="Programmeerimise alused(Eesti keel)",bg="lightblue",font="Arial 13",width=35,height=6,relief=RIDGE,command=pro).grid(row=3, column=3,columnspan=3,rowspan=2)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=3, column=6)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=4, column=6)
    Button(text="Fuüsika",bg="pink",font="Arial 13",width=23,height=6,relief=RIDGE,command=fuüsik).grid(row=3, column=7,columnspan=2,rowspan=2)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=3, column=9)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=4, column=9)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=3, column=10)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=4, column=10)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=3, column=11)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=4, column=11)

    #Среда
    Button(text="Eesti Keel\n(Tugiõpe)",bg="pink",font="Arial 13",width=11,height=3,relief=RIDGE,command=estõ).grid(row=5, column=2)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=2)
    Button(text="Kunstiained\n(Eesti keel)",bg="purple",font="Arial 13",width=23,height=6,relief=RIDGE,command=kunst).grid(row=5, column=3,columnspan=2,rowspan=2)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=5, column=5)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=5)
    Button(text="Kehaline kasvatus",bg="purple",font="Arial 13",width=23,height=6,relief=RIDGE,command=sport).grid(row=5, column=6,columnspan=2,rowspan=2)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=5, column=8)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=8)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=5, column=9)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=9)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=5, column=10)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=10)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=5, column=11)
    Label(text="   ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=6, column=11)

    #Четверг
    Button(text="Logistikateenused ja\n varude juhtmine",bg="green",font="Arial 13",width=23,height=6,relief=RIDGE,command=log).grid(row=7, column=2,columnspan=2,rowspan=2)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=7, column=4)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=8, column=4)
    Button(text="Programmeerimise alused\n(Eesti keel)",bg="lightblue",font="Arial 13",width=23,height=6,relief=RIDGE,command=pro).grid(row=7, column=5,columnspan=2,rowspan=2)
    Button(text="Inglese\nkeel",bg="beige",font="Arial 13",width=11,height=3,relief=RIDGE,command=eng).grid(row=7, column=7)
    Button(text="Inglese\nkeel",bg="beige",font="Arial 13",width=11,height=3,relief=RIDGE,command=eng).grid(row=7, column=8)
    Button(text="Arenduskeskkonna\nloomine",bg="red",font="Arial 13",width=23,height=3,relief=RIDGE,command=merkulova).grid(row=8, column=7,columnspan=2)
    Button(text="Arenduskeskkonna\nloomine",bg="red",font="Arial 13",width=23,height=3,relief=RIDGE,command=merkulova).grid(row=7, column=9,columnspan=2)
    Button(text="Eesti keel",bg="grey",font="Arial 13",width=11,height=3,relief=RIDGE,command=est).grid(row=8, column=9)
    Button(text="Eesti keel",bg="grey",font="Arial 13",width=11,height=3,relief=RIDGE,command=est).grid(row=8, column=10)
    Button(text="Rühmajuha\ntund",bg="pink",font="Arial 13",width=11,height=3,relief=RIDGE,command=clas).grid(row=7, column=11)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=8, column=11)

    #Пятница
    Button(text="Eesti keel",bg="purple",font="Arial 13",width=11,height=3,relief=RIDGE,command=est).grid(row=9, column=2)
    Button(text="Eesti keel",bg="purple",font="Arial 13",width=11,height=3,relief=RIDGE,command=est).grid(row=9, column=3)
    Button(text="Arenduskeskkonna\nloomine",bg="red",font="Arial 13",width=23,height=3,relief=RIDGE,command=merkulova).grid(row=9, column=9,columnspan=2)
    Button(text="Programmeerimise alused(Eesti keel)",bg="lightblue",font="Arial 13",width=58,height=6,relief=RIDGE,command=pro).grid(row=9, column=2,columnspan=9,rowspan=2)
    Button(text="Inglese\nkeel",bg="green",font="Arial 13",width=11,height=3,relief=RIDGE,command=eng).grid(row=10, column=9)
    Button(text="Inglese\nkeel",bg="green",font="Arial 13",width=11,height=3,relief=RIDGE,command=eng).grid(row=10, column=10)
    Button(text="Arenduskeskkonna\nloomine",bg="red",font="Arial 13",width=23,height=3,relief=RIDGE,command=merkulova).grid(row=10, column=2,columnspan=2)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=9, column=11)
    Label(text=" ",bg="white",font="Arial 13",width=11,height=3,relief=RIDGE).grid(row=10, column=11)

Button(text="Расписание", command=plan).grid(row=1, column=3)
Button(text="Регистрация", command=reg).grid(row=2, column=3)
Button(text="Авторизоваться", command=avt).grid(row=3, column=3)
Button(text="Выйти из программы", command=exit).grid(row=4, column=3)
Label(text=" ").grid(row=2, column=0)
Label(text=" ").grid(row=3, column=0)
Label(text=" ").grid(row=4, column=0)
Label(text=" ").grid(row=1, column=0)
Label(text=" ").grid(row=1, column=5)
Label(text=" ").grid(row=2, column=5)
Label(text=" ").grid(row=3, column=5)
Label(text=" ").grid(row=4, column=5)

root.mainloop()