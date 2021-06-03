from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import filedialog
import tkinter as tk
#import tkinter.ttk as ttk
import pymysql.cursors
import sqlite3

#connection database 'sklad'

#functions for buttons on tab1
def click_button():
    with my_conn.cursor() as cursor:
        sql = ('''SELECT * from mom LIMIT 0,10''')
        cursor.execute(sql)
        columns = ['ID', 'Nomination', 'Boarcode', 'Quantity', 'Price']
        for i, mom in enumerate(cursor):
            for j, key in enumerate(columns):
                e = Entry(tab1, width=50, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, mom[key])

def select_sklad(event):
    try:
        global selected_item
        index = sklad_tree_view.selection()[0]
        selected_item = sklad_tree_view.item(index)['values']
        boa_entry.delete(0, END)
        boa_entry.insert(END, selected_item[1])
        nom_entry.delete(0, END)
        nom_entry.insert(END, selected_item[2])
        qua_entry.delete(0, END)
        qua_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

#decription desktop window
window = Tk()
window.title("Склад Альма Опт")
window.geometry ('1500x500')

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
#Frame - container dor values other components like buttons, labels
frame_search = Frame(tab1)
frame_search.grid(row=0, column=0)
#active tab1
#add and describe table on tab1
#the lablel text for barcode search field
lbl_search = Label(frame_search, text='Поиск по штрихкоду')
lbl_search.grid (row=0, column=0, sticky=W)
#barcode value input field for search
boa_search = StringVar()
boa_search_entry = Entry(frame_search, textvariable=boa_search)
boa_search_entry.grid (row=0, column=1)
#describe buttons on tab1
btn = Button(tab1, text="Загрузить базу данных", command=click_button)
btn.place(x=400, y=0)
btn2 = Button(tab1, text = "Приход")
btn2.place(x=550, y=0)
btn3 = Button(tab1, text="Начать поиск")
btn3.place (x=300, y=0)
frame_btn = Frame(tab1)
frame_btn.grid(row=3, column=0)
btn4 = Button (frame_btn, text='Добавить позицию')
btn4.grid(row=0, column=0, pady=20)
btn5 = Button(frame_btn, text='Изменить позицию')
btn5.grid(row=0, column=1)
btn6 = Button(frame_btn, text='Удалить позицию')
btn6.grid(row=0, column=2)

#fields needed for the database
frame_fields = Frame(tab1)
#fields boarcode
boa_text = StringVar()
boa_label = Label(frame_fields, text='Штрихкод')
boa_label.grid(row=0, column=0, sticky=E)
boa_entry = Entry(frame_fields, textvariable=boa_text)
boa_entry.grid(row=0, column=3, sticky=W)
#fields nomination
nom_text = StringVar()
nom_label = Label(frame_fields, text='Наименование')
nom_label.grid (row=0, column=2, sticky=E)
nom_entry = Entry(frame_fields, textvariable=nom_text)
nom_entry.grid(row=0, column=3, sticky=W)
#fields Quantity
qua_text = StringVar()
qua_label = Label(frame_fields, text='Количество')
qua_label.grid(row=1, column=0, sticky=E)
qua_entry = Entry(frame_fields, text=qua_text)
qua_entry.grid(row=1, column=1, sticky=W)
#fields Price
price_text = StringVar()
price_label = Label(frame_fields, text='Цена за штуку')
price_label.grid(row=1, column=2, sticky=E)
price_entry = Entry(frame_fields, textvariable=price_text)
price_entry.grid(row=1, column=3, sticky=W)

#displaying the database to the screen as a table (tree structure)
frame_sklad = Frame(tab1)
frame_sklad.grid(row=4, column=0,columnspan=4,rowspan=6, pady=20, padx=20)

columns = ['№', 'Штрихкод','Наименование','Количество','Цена за штуку']
sklad_tree_view = Treeview(frame_sklad, columns=columns, show="headings")
sklad_tree_view.column('№', width=30)
for col in columns[1:]:
    sklad_tree_view.column(col, width=120)
    sklad_tree_view.heading(col, text=col)
sklad_tree_view.bind('<<TreeviewSelect>>', select_sklad)
sklad_tree_view.pack(side="left", fill="y")
scr = Scrollbar(frame_sklad, orient='vertical')
scr.configure(command=sklad_tree_view.yview)
scr.pack(side="right", fill="y")
sklad_tree_view.config(yscrollcommand=scr.set)


#grafics window output
#populate_list()
window.mainloop()
