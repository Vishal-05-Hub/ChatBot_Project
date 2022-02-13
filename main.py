from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

bot = ChatBot('My Bot')
trainer = ListTrainer(bot)
for file in os.listdir(r"C:/Users/acer/PycharmProjects/ChatBot/Dataset/"):
    data = open(r"C:/Users/acer/PycharmProjects/ChatBot/Dataset/" + file, "r").readline()
    trainer.train(data)


def askbot():
    query = questionfield.get()
    answer = bot.get_response(query)
    textarea.insert(END, 'You:'+query+'\n\n')
    textarea.insert(END, 'Tuba:'+str(answer)+'\n\n')
    engine.say(answer)
    engine.runAndWait()
    questionfield.delete(0, END)
    textarea.yview(END)




root = Tk()
root.geometry('500x570+100+30')
root.resizable(0,0)

root.title('ChatBot created by Vishal Chaudhary')
root.config(bg = '#98ccfd')

pic = PhotoImage(file = 'pic.png')

picture_Label = Label(root,image= pic, bg = '#98ccfd')
picture_Label.pack(pady=5)

center_Frame= Frame(root)
center_Frame.pack()

scrollbar = Scrollbar(center_Frame)
scrollbar.pack(side= RIGHT, fill= Y)

textarea = Text(center_Frame, font=('Arial', 20, 'bold'), width=80, height=10, yscrollcommand=scrollbar.set)
textarea.pack(side=LEFT, fill=BOTH)

questionfield = Entry(root, font=('Arial', 25, 'bold'))
questionfield.pack(fill=X,pady=8)

askimage=PhotoImage(file='ask.png')
askButton=Button(root, image=askimage, bd=0, bg='#98ccfd', activebackground='#98ccfd', cursor='hand2', command=askbot )
askButton.pack()

def enter_function(event):
    askButton.invoke()

root.bind('<Return>',enter_function)


root.mainloop()