# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 21:28:47 2018

@author: USER
"""

def menu():
    os.system('cls')
    print("帳密系統 : ")
    print("-----------")
    print("1. 輸入帳密.")
    print("2. 顯示帳密.")
    print("3. 修改密碼.")
    print("4. 刪除帳密.")
    print("0. 離開系統.")
    print("-----------")
    
             
def DispData():
    cursor=conn.execute('select *from password')
    
    print("帳號\t密碼")
    print("---------------")
    for row in cursor:
        print("{}\t{}".format(row[0], row[1]))
    input ("按任意鍵回選單")
    
    
def InputData():
    while True:
        name=input("請輸入帳號(Enter==>停止輸入)")
        if name=="": break
        sqlstr="select *from password where name='{}'".format(name)
        cursor=conn.execute(sqlstr)
        row=cursor.fetchone()
        if not row==None:
            print("{} Account existed!".format(name))
            continue
        password = input("Input Password")
        sqlstr="insert into password  values('{}','{}');".format(name,password)
        cursor=conn.execute(sqlstr)
        conn.commit()
        print("{} 儲存完畢 任意鍵繼續".format(name))
        break
        
def EditData():
    while True:
        name = input("輸入修改的帳號(Enter==>停止輸入)")
        if name=="": break
        sqlstr="select * from password where name='{}'" .format(name)
        cursor=conn.execute(sqlstr)
        row=cursor.fetchone()
        print(row)
        
        if row==None:
            print("{} Account not existed!".format(name))
            continue
        print("原來密碼: {}".format(row[1]))
        password = input("Input New Password:")
        sqlstr="update password set pass='{}'  where name='{}'" .format(password, name)
        conn.execute(sqlstr)
        conn.commit()
        input("修改完畢 請按任意鍵繼續回主選單!")
        break

def DeleteData():
    while True:
        name = input("請輸入要刪除帳號(Enter==>停止輸入)")
        if input=="": break
        sqlstr="select *from password where name='{}'".format(name)
        cursor=conn.execute(sqlstr)
        row=cursor.fetchone()
        print(row)
        
        if row==None:
            print("{} Account not existed!".format(name))
            continue
        print("是否刪除 {} 資料?".format(name))
        yn=input ("Y/N?")
        if (yn=='Y' or yn=='y'):
            sqlstr="delete from password  where name='{}'".format(name)
            conn.execute(sqlstr)
            conn.commit()
            input("刪除完畢 請按任意鍵回主選單!")
            break
        
### 主程式 ###
import os,sqlite3
#connect Sqlite
conn=sqlite3.connect('Sqlite01.db')


while True:
    menu()
    choice = int(input("輸入選項:"))
    print()
    if choice==1:
        InputData()
    elif choice==2:
        DispData()
    elif choice==3:
        EditData()
    elif choice==4:
        DeleteData()
    else:
        conn.close()
        print("system break.") 
        break
    
    
    
    #print("system done.")