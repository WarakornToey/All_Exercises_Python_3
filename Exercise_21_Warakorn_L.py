from tkinter import *
import math

def leftClickButton(event):
    BMI = round(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2),2)
    if BMI < 18.5:
        BMIResult = "ผอมเกินไป"
    elif BMI >=18.5 and BMI < 23:
        BMIResult = "น้ำหนักปกติ เหมาะสม"
    elif BMI >=23 and BMI < 25:
        BMIResult = "น้ำหนักเกิน"
    elif BMI >=25 and BMI < 30:
        BMIResult = "อ้วน"
    elif BMI >= 30 :
        BMIResult = "อ้วนมาก"

    labelResult.configure(text="ค่า BMI ของคุณคือ :" + str(BMI) + "  ผลการประเมินคือ : "+ BMIResult)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()