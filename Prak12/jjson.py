from tkinter import *
import tkinter as tk
from tkinter import Checkbutton
####
import requests
import json

window = Tk()
window.title('Кувшинова Анастасия Алексеевна')
window.geometry('400x100')

label_rep = Label(window, text='Введите в поле имя репозитория: ')
label_rep.pack()
txt = Entry(window)
txt.pack()

def jjson():
    username = txt.get()
    url = f'https://api.github.com/apache/{username}'
    user_data = requests.get(url).json()
    data = {}
    kkey = ['company',
            'created_at',
            'email',
            'id',
            'name',
            'url']
    for i in kkey:
        data[i] = user_data[i]
    with open('Kuvshinova_Anastasia_Alekseevna_UB-31_jjson.json', 'w') as repoz:
        json.dump(data, repoz, indent=4)
    print('Данные о репозитории получены и записаны в файл!')

Button(window, text='Получить результат', command=jjson).pack()

window.mainloop()

#даны самые популярные репозитории на github
#https://habr.com/ru/post/453444/, по последней цифре зачетки получить JSON   (2, spark)
#для вашего варианта .
#Программа с графическим интерфейсом вводим в поле имя репозитория и по
#нажатию кнопки получаем результат.
#Необходимо получить в новый файл следующую информацию:
#   'company': None,
#   'created_at': '2015-08-03T17:55:43Z',
#   'email': None,
#   'id': 13629408,
#   'name': 'Kubernetes',
#   'url': 'https://api.github.com/users/kubernetes'}
