from tkinter import *
import math

def leftClickButton(event):
    BMI = round(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2),2)
    if BMI < 18.5:
        BMIResult = "ผอมเกินไป"
    elif 18.6 < BMI < 22.9:
        BMIResult = "น้ำหนักปกติ เหมาะสม"
    elif 23.0 < BMI < 24.9:
        BMIResult = "น้ำหนักเกิน"
    elif 25.0 < BMI < 29.9:
        BMIResult = "อ้วน"
    else :
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