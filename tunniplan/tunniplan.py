from tkinter import *
root = Tk()
#Время и счет урока
Label(text="0").grid(row=0, column=1)
Label(text="1").grid(row=0, column=2)
Label(text="2").grid(row=0, column=3)
Label(text="3").grid(row=0, column=4)
Label(text="4").grid(row=0, column=5)
Label(text="5").grid(row=0, column=6)
Label(text="6").grid(row=0, column=7)
Label(text="7").grid(row=0, column=8)
Label(text="8").grid(row=0, column=9)
Label(text="9").grid(row=0, column=10)
Label(text="10").grid(row=0, column=11  )
#пустая строка в углу
Label(text="   ").grid(row=0, column=0)
#Дни
Label(text="Esmaspäev").grid(row=1, column=0)
Label(text="").grid(row=2, column=0)
Label(text="Teisipäev").grid(row=3, column=0)
Label(text="").grid(row=4, column=0)
Label(text="Kolmapäev").grid(row=5, column=0)
Label(text="").grid(row=6, column=0)
Label(text="Neljapäev").grid(row=7, column=0)
Label(text="").grid(row=8, column=0)
Label(text="Reede").grid(row=9, column=0)
Label(text="").grid(row=10, column=0)

#Нелевой урок
Label(text="   ").grid(row=2, column=2)
Label(text="   ").grid(row=3  , column=2)
Label(text="   ").grid(row=4, column=2)
Label(text="   ").grid(row=5  , column=2)
Label(text="   ").grid(row=6, column=2)
Label(text="   ").grid(row=7  , column=2)
Label(text="   ").grid(row=8, column=2)
Label(text="   ").grid(row=9  , column=2)

#Понедельник row=вниз column=право
Label(text=" ").grid(row=1, column=3)
Label(text="EK(Tugiõpe)").grid(row=2, column=2)
Label(text="Logistika").grid(row=1, column=3)
Label(text="ja varude").grid(row=2, column=3)
Label(text="teenused").grid(row=1, column=4)
Label(text="juhtmine").grid(row=2, column=4)
Label(text="Matem").grid(row=1, column=5)
Label(text="aatika").grid(row=2, column=5)
Label(text="Matem").grid(row=1, column=6)
Label(text="aatika").grid(row=2, column=6)
Label(text="   ").grid(row=2, column=7)
Label(text="   ").grid(row=1, column=7)   
Label(text="Keel ja").grid(row=1, column=8)
Label(text="kirjandus").grid(row=2, column=8)
Label(text="Keel ja").grid(row=1, column=9)
Label(text="kirjandus").grid(row=2, column=9)
Label(text="(Tugiõpe)").grid(row=1, column=10)
Label(text="Matemaatika").grid(row=2, column=10)
Label(text="   ").grid(row=1, column=11)
Label(text="   ").grid(row=2, column=11)

#Вторник
Label(text="Tugiõpe").grid(row=3, column=2)
Label(text="(Keemia)").grid(row=4, column=2)
Label(text="Progra").grid(row=3, column=3)
Label(text="mmerimise").grid(row=3, column=4)
Label(text="alused").grid(row=3, column=5)
Label(text="(").grid(row=4, column=3)
Label(text="Eesti keel").grid(row=4, column=4)
Label(text=")").grid(row=4, column=5)
Label(text="   ").grid(row=3, column=6)
Label(text="   ").grid(row=4, column=6)
Label(text="Fu").grid(row=3, column=7)
Label(text="i").grid(row=4, column=7)
Label(text="üs").grid(row=3, column=8)
Label(text="ka").grid(row=4, column=8)
Label(text="   ").grid(row=3, column=9)
Label(text="   ").grid(row=4, column=9)
Label(text="   ").grid(row=3, column=10)
Label(text="   ").grid(row=4, column=10)
Label(text="   ").grid(row=3, column=11)
Label(text="   ").grid(row=4, column=11)

#Среда
Label(text="EK(Tugiõpe)",bg="purple").grid(row=5, column=2)
Label(text="   ").grid(row=6, column=2)
Label(text="Kunsti",bg="purple").grid(row=5, column=3)
Label(text="(Eesti",bg="purple").grid(row=6, column=3)
Label(text="ained",bg="purple").grid(row=5, column=4)
Label(text="keel)",bg="purple").grid(row=6, column=4)
Label(text="   ").grid(row=5, column=5)
Label(text="   ").grid(row=6, column=5)
Label(text="Keha",bg="purple").grid(row=5, column=6)
Label(text="kasv",bg="purple").grid(row=6, column=6)
Label(text="line",bg="purple").grid(row=5, column=7)
Label(text="atus",bg="purple").grid(row=6, column=7)
Label(text="   ").grid(row=5, column=8)
Label(text="   ").grid(row=6, column=8)
Label(text="   ").grid(row=5, column=9)
Label(text="   ").grid(row=6, column=9)
Label(text="   ").grid(row=5, column=10)
Label(text="   ").grid(row=6, column=10)
Label(text="   ").grid(row=5, column=11)
Label(text="   ").grid(row=6, column=11)

#Четверг
Label(text="Logistika").grid(row=7, column=2)
Label(text="ja varude").grid(row=8, column=2)
Label(text="teenused").grid(row=7, column=3)
Label(text="juhtmine").grid(row=8, column=3)
Label(text="   ").grid(row=7, column=4)
Label(text="   ").grid(row=8, column=4)
Label(text="Programme").grid(row=7, column=5)
Label(text="alused").grid(row=8, column=5)
Label(text="erimise").grid(row=7, column=6)
Label(text="(Eesti keel)").grid(row=8, column=6)
Label(text="Ing keel").grid(row=7, column=7)
Label(text="Ing keel").grid(row=7, column=8)
Label(text="Arenduskeskkonna").grid(row=8, column=7)
Label(text="loomine").grid(row=8, column=8)
Label(text="Arenduskeskkonna").grid(row=7, column=9)
Label(text="loomine").grid(row=7, column=10)
Label(text="Eesti keel",bg="purple").grid(row=8, column=9)
Label(text="Eesti keel",bg="purple").grid(row=8, column=10)
Label(text="Rühmajuha").grid(row=7, column=11)
Label(text="taja tund").grid(row=8, column=11)

#Пятница
Label(text="Eesti keel",bg="purple",font="Arial,50",width=10,height=3,relief=RIDGE).grid(row=9, column=2)
Label(text="Eesti keel",bg="purple",font="Arial,50",width=10,height=3,relief=RIDGE).grid(row=9, column=3)
Label(text="Arenduskeskkonna loomine",bg="red",font="Arial,50",width=22,height=3,relief=RIDGE).grid(row=9, column=9,columnspan=2)
Label(text="Programmeerimise alused(Eesti keel)",bg="lightblue",font="Arial,50",width=30,height=3,relief=RIDGE).grid(row=9, column=5,columnspan=7)
Label(text="Arenduskeskkonna loomine",bg="red",font="Arial,50",width=22,height=3,relief=RIDGE).grid(row=9, column=9,columnspan=2)
Label(text="Ing keel",bg="green",font="Arial,50",width=11,height=3,relief=RIDGE).grid(row=10, column=9)
Label(text="Ing keel",bg="green",font="Arial,50",width=11,height=3,relief=RIDGE).grid(row=10, column=10)
root.mainloop()