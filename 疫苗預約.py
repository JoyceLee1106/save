# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:44:55 2021

@author: 179cl
"""

print("請輸入start開始程式")
import time
X=input()
s=[]

while X == 'start':
    print("請輸入 a 建立模擬資料 b 查詢資料 c 資料統計 d 輸出資料 e寫入資料 f讀取資料 g更改資料 或其他離開程式")
    A=input()
    if A == 'a' :
        print("請輸入模擬筆數")
        while True:
            try:                
                num=input()
                num=int(num)
                break
            except ValueError:
                print('That is not a valid number! Try again!')
        start = time.time()
        while len(s) < num :
            import random
            x=2022
            y=random.randint(1,12)
            list_y=[4,6,9,11]
            if y in list_y:
                z=random.randint(1,30)
            elif y==2:
                z=random.randint(1,28)
            else:
                z=random.randint(1,31)
            if y < 10:
                y=str(0)+str(y)
            else:
                y=str(y)
            if z < 10:
                z=str(0)+str(z)
            else:
                z=str(z)
                times=str(x)+'-'+str(y)+'-'+str(z)
                p=random.choices(("台北","新北","桃園","台中","台南","高雄"))
                p=str(p)
                p=p[2:4]
                i=str(len(s)+1)+','+str(times)+','+str(p)
                s.append(i)
            end = time.time()
        print(end - start)
            
    elif A =='b':
           print("請輸入搜尋目標 a城市 b日期 其他返回")
           B=input()
           if B=='a':
               print("請輸入城市(台北,新北,桃園,台中,台南,高雄)或其他返回")
               city=input()
               for i in s:
                   if i[-2:]==city:
                       print(i)
           elif B=='b':
                print("請輸入時間(YYYY-MM-DD)或其他返回")
                t=input()
                t=str(t)
                for i in s:
                    if i[-13:-3]==t:
                        print(i)
    elif A=='c':
            start = time.time()
            taipei=[]
            newtaipei=[]
            taoyuan=[]
            taichung=[]
            tainan=[]
            kaohsiung=[]
            jan=[]
            feb=[]
            mar=[]
            apr=[]
            may=[]
            jun=[]
            jul=[]
            aug=[]
            sep=[]
            octo=[]
            nov=[]
            dec=[]
            Taipei=("台北")
            Newtaipei=("新北")
            Taoyuan=("桃園")
            Taichung=("台中")
            Tainan=("台南")
            Kaohsiung=("高雄")
            
            for i in s:
                if i[-2:]==Taipei:
                    taipei.append(i)
                elif i[-2:]==Newtaipei:
                    newtaipei.append(i)
                elif i[-2:]==Taoyuan:
                    taoyuan.append(i)
                elif i[-2:]==Taichung:
                    taichung.append(i)
                elif i[-2:]==Tainan:
                    tainan.append(i)
                elif i[-2:]==Kaohsiung:
                    kaohsiung.append(i)
                if i[-8:-6]=='01':
                    jan.append(i)
                elif i[-8:-6]=='02':
                    feb.append(i)
                elif i[-8:-6]=='03':
                    mar.append(i)
                elif i[-8:-6]=='04':
                    apr.append(i)
                elif i[-8:-6]=='05':
                    may.append(i)
                elif i[-8:-6]=='06':
                    jun.append(i)
                elif i[-8:-6]=='07':
                    jul.append(i)
                elif i[-8:-6]=='08':
                    aug.append(i)
                elif i[-8:-6]=='09':
                    sep.append(i)
                elif i[-8:-6]=='10':
                    octo.append(i)
                elif i[-8:-6]=='11':
                    nov.append(i)
                elif i[-8:-6]=='12':
                    dec.append(i)
            print("台北 共有",len(taipei),"位 預約施打")
            print("新北 共有",len(newtaipei),"位 預約施打")
            print("桃園 共有",len(taoyuan),"位 預約施打")
            print("台中 共有",len(taichung),"位 預約施打")
            print("台南 共有",len(tainan),"位 預約施打")
            print("高雄 共有",len(kaohsiung),"位 預約施打")
            print("2022-01 共有",len(jan),"位 預約施打")
            print("2022-02 共有",len(feb),"位 預約施打")
            print("2022-03 共有",len(mar),"位 預約施打")
            print("2022-04 共有",len(apr),"位 預約施打")
            print("2022-05 共有",len(may),"位 預約施打")
            print("2022-06 共有",len(jun),"位 預約施打")
            print("2022-07 共有",len(jul),"位 預約施打")
            print("2022-08 共有",len(aug),"位 預約施打")
            print("2022-09 共有",len(sep),"位 預約施打")
            print("2022-10 共有",len(octo),"位 預約施打")
            print("2022-11 共有",len(nov),"位 預約施打")
            print("2022-12 共有",len(dec),"位 預約施打")
            end = time.time()
            print(end - start)
    elif A=='d':
            print(s)
    elif A=='e':
        print("請輸入欲寫入的檔名:")
        name1=input()
        file=open(str(name1),'w')
        for i in s:
            file.write(str(i)+'\n')
        file.close()
    elif A=='f':
        print("請輸入欲讀取的檔名:")
        while True:
            try:
                name2=input()
                file=open(str(name2),'r')
                break
            except:
                print('That is not a File! Try again!')

        text=file.read()
        print(text)
        file.close()
    elif A=='g':
        n=[]
        print("請輸入欲讀取的檔名:")
        while True:
            try:
                name3=input()
                file=open(str(name3),'r')
                break
            except:
                print('That is not a File! Try again!')

        for line in file:
            n.append(line)
        file.close()
        print("請輸入欲修改的資料序號")
        while True:
            try:
                num=input()
                num=str(num)
                break
            except ValueError:
                print('That is not a valid number! Try again!')
        if len(n)>(int(num)-1):
            for i in n:
                if i[:-15]==num:
                    print("原始資料為",i)
                    print("請輸入欲施打的城市:")
                    city2=input()                
                    print("請輸入欲施打的時間(YYYY-MM-DD):")
                    time2=input()
                    i=str(num)+','+str(time2)+','+str(city2)+'\n'
                    n.pop(int(num)-1)
                    n.insert(int(num)-1,i)
            file=open(str(name3),'w')
            for i in n:
                  file.write(str(i))
            file.close()      
                    
        else:
            print("查無此資料")
    else:
            break
print("程式結束")
