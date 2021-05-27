from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
import pymysql.cursors
import sqlite3

#connection database 'sklad'
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='almaopt',
                             db='sklad',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#function for button1
def click_button():
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT ID, Nomination, Boarcode, Quantity, Price FROM mom "

        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)
    cursor.close ()

#function for button2 (upolad file coming for database mom)
def coming_mom(event=None):
    filename = filedialog.askopenfilename()
    print('Secected:', filename)




#decription desktop window
window = Tk()
window.title("Склад Альма Опт")
window.geometry ('500x500')

#declaring tabs
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

#description of tabs
tab_control.add(tab1, text='MOM')
tab_control.add(tab2, text='MDP')
tab_control.add(tab3, text='Elisia')
tab_control.add(tab4, text='LAB')
tab_control.add(tab5, text='KM')
tab_control.pack(expand=1, fill='both')

#active tab1
#add and describe table on tab1


#describe button on tab1
btn = Button(tab1, text="Загрузить базу данных", command=click_button)
btn.place(x=10, y=10)
btn2 = Button(tab1, text = "Приход", command=coming_mom)
btn2.place(x=150, y=10)


#grafics window output
window.mainloop()
