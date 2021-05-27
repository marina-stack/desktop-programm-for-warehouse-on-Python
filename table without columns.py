import sqlite3
import pymysql.cursors
import tkinter  as tk
from tkinter import *
my_conn =  pymysql.connect(host='localhost',
                             user='root',
                             password='almaopt',
                             db='sklad',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
###### end of connection ####

##### tkinter window ######

my_w = tk.Tk()
my_w.geometry("400x250")

with my_conn.cursor() as cursor:
    sql = ('''SELECT * from mom LIMIT 0,10''')
    cursor.execute(sql)
    i = 0  # row value inside the loop
    for mom in cursor:
        for j in range(len(mom)):
            e = Entry(my_w, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, mom[j])
        i = i + 1


cursor.close()
my_w.mainloop()
