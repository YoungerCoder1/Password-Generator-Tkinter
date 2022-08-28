from tkinter import *
import random

AL_LLETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#№$%^&*()-_=+/\?~1234567890'

def generate(leng):
    password=''
    for i in range(leng):
        symbol = random.randint(0, len(AL_LLETTERS)-1)
        password += AL_LLETTERS[symbol]

    return password

def txt_insert(leng):
    a=str(generate(leng))
    global txt
    txt.delete(0.0, END)
    txt.insert(0.0, a)

root=Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 250  # смещение от середины
h = h - 330
root.resizable(False, False)  # делаю чтоб окно нельзя было изменять в размере
root.geometry(f'500x500+{w}+{h}')  # Устанавливаю размер окна
root.configure(bg='gray')
root.title('Generate Password')
Label(text='ГЕНЕРАТОР ПАРОЛЕЙ',font=('ArialBlack', 20, 'bold'),bg='gray').place(x=35, y=0)

Label(text='Длинна пароля:',font=('ArialBlack', 9, 'bold'),bg='gray').place(x=0, y=40)
leng_ent=Entry()
leng_ent.place(x=110,y=40)
Button(text='Генерировать',font=('ArialBlack', 10, 'bold'),command=lambda: txt_insert(int(leng_ent.get()))).place(x=0, y=90)

txt=Text(width=55, height=16,font=('ArialBlack', 10, 'bold'))
txt.place(x=0, y=140)

root.mainloop()
