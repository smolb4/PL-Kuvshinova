from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
from tkinter import filedialog as fd


window = Tk()  #база
window.title("Кувшинова Анастасия Алексеевна")
window.geometry('400x250')

tab_control = ttk.Notebook(window)   #добавлять
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)


tab_control.add(tab1, text='Первая')   # 1 вкладка
tab_control.pack(fill="both", expand=True)

def kalkulator():
    a = int(txt1.get())
    b = int(txt2.get())
    if combo.get() == '+':
        messagebox.showinfo('Готово:',a + b)
    elif combo.get() == '-':
        messagebox.showinfo('Готово:',a - b)
    elif combo.get() == '*':
        messagebox.showinfo('Готово:',a * b)
    else:
        messagebox.showinfo('Готово:',a / b)

txt1 = Entry(tab1)  #число
txt1.pack()
combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')  #знак
combo.pack()
txt2 = Entry(tab1) #число
txt2.pack()

Button(tab1, text='Проверить', command=kalkulator).pack()

tab_control.add(tab2, text='Вторая')   # 2 вкладка
tab_control.pack(fill="both", expand=True)

def proverka():
    if (p1_value.get())==True and (v2_value.get())!=True and (t3_value.get())!=True:
        messagebox.showinfo('Сектор приз на барабане', 'Был выбран только первый вариант.\n\nВладимир Владимирович,\nя буду ходить к вам, пока у меня не будет 85')
    elif (v2_value.get())==True and (p1_value.get())!=True and (t3_value.get())!=True:
        messagebox.showinfo('Калинки-малинки','Был выбран только второй вариант.\n\nВладимир Владимирович,\nдавайте! С барского \nплеча! Как умеете!!!')
    elif (t3_value.get())==True and (v2_value.get())!=True and (p1_value.get())!=True:
        messagebox.showinfo('Ты знаешь, так хочется жить...','Был выбран только третий вариант.\n\nВладимир Владимирович,\nя не хочу на экзамен')
    elif (p1_value.get())==True and (v2_value.get())==True and (t3_value.get())!=True:
        messagebox.showinfo('Сектор приз на барабане', 'Были выбраны первый и второй варианты.\n\nВладимир Владимирович,\nя буду ходить к вам, пока у меня не будет 85')
    elif (p1_value.get())==True and (v2_value.get())!=True and (t3_value.get())==True:
        messagebox.showinfo('Сектор приз на барабане', 'Были выбраны первый и третий варианты.\n\nВладимир Владимирович,\nну я реально стараюсь')
    elif (p1_value.get())!=True and (v2_value.get())==True and (t3_value.get())==True:
        messagebox.showinfo('Hande Hoh!','Были выбраны второй и третий варианты.\n\nВладимир Владимирович,\nруки вверх! Вы попались.\nЧтобы освободиться, нужно поставить зачет!')
    elif (p1_value.get())==True and (v2_value.get())==True and (t3_value.get())==True:
        messagebox.showinfo('Сектор приз на барабане', 'Были выбраны первый, второй и третий варианты.\n\nВладимир Владимирович,\nя пишу это в 02:43')
    else:
        messagebox.showinfo('Повторите попытку','Вы ничего не выбрали :(\n\nВладимир Владимирович,\nне буяньте')


p1_value = BooleanVar()
p1 = Checkbutton(tab2, text='Первый', variable=p1_value)
p1.pack()

v2_value = BooleanVar()
v2 = Checkbutton(tab2, text='Второй', variable=v2_value)
v2.pack()

t3_value = BooleanVar()
t3 = Checkbutton(tab2, text='Третий', variable=t3_value)
t3.pack()

Button(tab2, text='Проверить', command=proverka).pack()

tab_control.add(tab3, text='Третья')   # 3 вкладка
tab_control.pack(fill="both", expand=True)

text = Text(tab3, height=12)
text.pack()

def open():
    filetypes1 = (('text files', '*.txt'),('All files', '*.*'))
    f = fd.askopenfile(filetypes=filetypes1)
    f1 = codecs.open(f, encoding='utf-8')
    f2 = f1.read()
    text.insert('1.0', f2)

Button(tab3, text='Загрузить...', command=open).pack()

window.mainloop()
