from tkinter import *
from tkinter.ttk import Progressbar
import openpyxl

workbook = openpyxl.load_workbook(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Questions.xlsx")

worksheet = workbook.active

questions = []
first_option = []
second_option = []
third_option = []
fourth_option = []
correct_answers = []

for row in worksheet.iter_rows(min_row=2, values_only=True):
    questions.append(row[0])
    first_option.append(row[1])
    second_option.append(row[2])
    third_option.append(row[3])
    fourth_option.append(row[4])
    correct_answers.append(row[5])

workbook.close()


def select(event):
    b = event.widget
    value = b['text']
    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()
    for i in range(35):
        if value == correct_answers[i]:
            if value == first_option[34]:
                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    amountlabel.config(image=amountimage)
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()

                def on_closing():
                    root2.destroy()
                    root.destroy()

                amountlabel.config(image=image35)
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.grab_set()
                root2.config(bg="black")
                root2.geometry('500x400+140+30')
                root2.title('You Are Fabulous')
                centerimg = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\center.png")
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='You Did It!!', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()

                happyimage = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\happy.png")
                happYLabel = Label(root2, image=happyimage, bg='black')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='black')
                happYLabel1.place(x=30, y=280)

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0, activebackground='black', cursor='hand2', activeforeground='white',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0,
                                     activebackground='black', cursor='hand2', activeforeground='white',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing)
                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=sprites[i])

        if value not in correct_answers:
            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountlabel.config(image=amountimage)
                root1.destroy()

            def on_closing():
                root1.destroy()
                root.destroy()

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('WON!!!')
            img = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\center.png")
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack()
            sadimage = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\sad.png")
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                    bd=0, activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0,
                                 activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()

            break


def lifeline50():
    lifeline50Button.config(image=image50x)
    lifeline50Button.config(state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton4.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton3.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[15]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[16]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[17]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[18]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[19]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[20]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[21]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[22]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[23]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[24]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[25]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[26]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[27]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[28]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[29]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[30]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[31]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[32]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[33]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[34]:
        optionButton2.config(text='')
        optionButton4.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)

    progressbarA.place(x=580, y=190)
    progressbarLabelA.place(x=580, y=320)

    progressbarB.place(x=620, y=190)
    progressbarLabelB.place(x=620, y=320)

    progressbarC.place(x=660, y=190)
    progressbarLabelC.place(x=660, y=320)

    progressbarD.place(x=700, y=190)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=90)

        progressbarB.config(value=60)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=80)

        progressbarB.config(value=30)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)

        progressbarB.config(value=30)

        progressbarC.config(value=40)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=10)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)

        progressbarB.config(value=20)

        progressbarC.config(value=80)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=70)

        progressbarB.config(value=10)

        progressbarC.config(value=50)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=20)

        progressbarB.config(value=80)

        progressbarC.config(value=70)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)

        progressbarB.config(value=70)

        progressbarC.config(value=20)

        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=90)

        progressbarB.config(value=80)

        progressbarC.config(value=30)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)

        progressbarB.config(value=60)

        progressbarC.config(value=80)

        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=35)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)

        progressbarB.config(value=90)

        progressbarC.config(value=65)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[15]:
        progressbarA.config(value=60)

        progressbarB.config(value=90)

        progressbarC.config(value=65)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[16]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[17]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[18]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[19]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[20]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[21]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=80)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[22]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[23]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[24]:
        progressbarA.config(value=60)

        progressbarB.config(value=90)

        progressbarC.config(value=65)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[25]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[26]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=80)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[27]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=80)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[28]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[29]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=80)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[30]:
        progressbarA.config(value=90)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[31]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=80)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[32]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[33]:
        progressbarA.config(value=95)

        progressbarB.config(value=65)

        progressbarC.config(value=60)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[34]:
        progressbarA.config(value=96)

        progressbarB.config(value=65)

        progressbarC.config(value=66)

        progressbarD.config(value=80)


root = Tk()
root.geometry('1520x1080')
root.title('Python MCQ Mania')
root.config(bg='black')

leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='black', padx=70, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='black', pady=20)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black', pady=30, padx=30)
bottomFrame.grid(row=2, column=0)

centerImage = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\center.png")
logoLabel = Label(middleFrame, image=centerImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\50-50.png")
image50x = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\50-50-X.png")

lifeline50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black',
                          width=180, height=80, command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\audiencePole.png")
audiencePolex = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\audiencePoleX.png")
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=180, height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

amountimage = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture0.png")
image1 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture0.png")
image2 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture0.png")
image3 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture0.png")
image4 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture0.png")
image5 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture1.png")
image6 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture1.png")
image7 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture1.png")
image8 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture1.png")
image9 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture1.png")
image10 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture2.png")
image11 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture2.png")
image12 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture2.png")
image13 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture2.png")
image14 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture2.png")
image15 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture3.png")
image16 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture3.png")
image17 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture3.png")
image18 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture3.png")
image19 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture3.png")
image20 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture4.png")
image21 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture4.png")
image22 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture4.png")
image23 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture4.png")
image24 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture4.png")
image25 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture5.png")
image25 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture5.png")
image30 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture6.png")
image30 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture6.png")
image35 = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\Picture8.png")

sprites = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11,
           image12, image13, image14, image15, image16, image17, image18, image19, image20, image21, image22,
           image23, image24, image25, image30, image35]

amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file=r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\sprites\lay.png")
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)

questionArea = Text(bottomFrame, font=('arial', 12, 'bold'), bg='black', fg='white', width=34, height=2,
                    wrap='word', bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 12, 'bold'), bg='black', fg='white',
                       cursor='hand2', bd=0, activebackground='black', activeforeground='white')
optionButton1.place(x=100, y=100)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 12, 'bold'), bg='black', fg='white',
                       cursor='hand2', bd=0, activebackground='black', activeforeground='white')
optionButton2.place(x=370, y=100)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 12, 'bold'), bg='black', fg='white',
                       cursor='hand2', bd=0, activebackground='black', activeforeground='white')
optionButton3.place(x=100, y=180)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 12, 'bold'), bg='black', fg='white',
                       cursor='hand2', bd=0, activebackground='black', activeforeground='white')
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()
