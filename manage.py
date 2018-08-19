# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:11:29 2018

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
    
def ReadData():
    with open('password.txt','r',encoding='UTF-8-sig') as f:
             filedata=f.read()
             if filedata !="":
                 data= ast.literal_eval(filedata)
                 return data
             else: return dict()
        
def DispData():
    print("帳號 \t 密碼")
    print("----------")
    for key in data:
        print("{}\t{}".format(key,data[key]))
    input ("按任意鍵回選單")
    
def InputData():
    while True:
        name=input("請輸入帳號(Enter==>停止輸入)")
        if name=="":break
        if name in data:
            print("{} 帳號存在!".format(name))
            continue
        password = input("請輸入密碼:")
        data[name]=password
        with open('password.txt','w',encoding='UTF-8-sig') as f:
            f.write(str(data))
        print("{} 儲存完畢 任意鍵繼續".format(name))
def EditData():
    while True:
        name = input("輸入修改的帳號(Enter==>停止輸入)")
        if name=="":break
        if name not in data:
            print("{} 帳號不存在!".format(name))
            continue
        print("原來密碼: {}".format(data[name]))
        
        password = input("請輸入新密碼:")
        data[name] = password
        with open ('password.txt','w',encoding='UTF-8-sig') as f:
            f.write(str(data))
            input("修改完畢 請按任意鍵繼續回主選單!")
            break

def DeleteData():
    while True:
        name = input("請輸入要刪除帳號(Enter==>停止輸入)")
        if input=="": break
        if name not in data:
            print ("{} 帳密不存在!".format(name))
            continue
        print("是否刪除 {} 資料?".format(name))
        yn=input ("Y/N?")
        if (yn=='Y' or yn=='y'):
            del data[name]
            with open('password.txt','w',encoding='UTF-8-sig') as f:
                f.write(str(data))
                input("刪除完畢 請按任意鍵回主選單!")
                break
        
### 主程式 ###
import os,ast
data = dict()

data = ReadData()   #讀取轉dict
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
        print("system break.") 
        break

    print("system done.")





            
            
        
    