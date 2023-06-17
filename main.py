import tkinter
import random

def tab(x,y):
    buttons[x,y]['text'] = button_kart[x,y]



# переменные для игры
step = 0 #кол-во шагов
kart = ['🐍', '🐍','🎄','🎄','🐌','🐌','🐯','🐯']
buttons = {}
button_kart = {}
random.shuffle(kart)
#print(kart)
root = tkinter.Tk()
root.title("Memory")
root.resizable(width=False,height=False)
c = tkinter.Canvas(root, width=10, height=10, background='blue')
c.grid(column=0,row=1)
tkinter.Label(text="Игра Memory").grid(column=0,row=0)
tkinter.Label(text='Найдите одинаковые карточки').grid(column=0 , row=2)
mows_text = "Шаги :" + str(step)
tkinter.Label(text=mows_text).grid(column=0 , row=3)
for i in range(1, 5):
    for j in range(1,3):
        button = tkinter.Button(width=3, height=3, bg = 'yellow', text='',command= lambda x=i , y=j: tab(x,y))
        button.grid(column=i,row=j)
        buttons[i,j] = button
        button_kart[i,j] = kart.pop()
print(buttons)
print(button_kart)
root.mainloop()