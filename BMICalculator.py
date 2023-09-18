import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

class BMICalculator:

    def __init__(self, root):
        global weight,height,txtWeight,txtHeight

        root.title("BMI Calculator")
        width=441
        height=191
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        lblWeight=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        lblWeight["font"] = ft
        lblWeight["fg"] = "#333333"
        lblWeight["justify"] = "center"
        lblWeight["text"] = "Enter Your Weight (Kg)"
        lblWeight.place(x=60,y=10,width=271,height=30)

        txtWeight = tk.Entry(root)
        txtWeight["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txtWeight["font"] = ft
        txtWeight["fg"] = "#333333"
        txtWeight["justify"] = "center"
        txtWeight["text"] = ""
        txtWeight.place(x=120,y=40,width=194,height=30)


        lblHeight=tk.Label(root)
        lblHeight["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=12)
        lblHeight["font"] = ft
        lblHeight["fg"] = "#333333"
        lblHeight["justify"] = "center"
        lblHeight["text"] = "Enter Your Height (cm)"
        lblHeight.place(x=40,y=70,width=307,height=30)

        txtHeight=tk.Entry(root)
        txtHeight["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txtHeight["font"] = ft
        txtHeight["fg"] = "#333333"
        txtHeight["justify"] = "center"
        txtHeight["text"] = ""
        txtHeight.place(x=120,y=100,width=195,height=30)

        btnCalculateBMI=tk.Button(root)
        btnCalculateBMI["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnCalculateBMI["font"] = ft
        btnCalculateBMI["fg"] = "#000000"
        btnCalculateBMI["justify"] = "center"
        btnCalculateBMI["text"] = "Calculate"
        btnCalculateBMI.place(x=170,y=140,width=112,height=30)
        btnCalculateBMI["command"] = self.calculateBMI

    def calculateBMI(self):
        weight = txtWeight.get()
        height = txtHeight.get()

        if weight == "":
            tk.messagebox.showinfo(message="Weight is mandatory")
            return

        if height == "":
            tk.messagebox.showinfo(message="Height is mandatory")
            return

        if (is_float(height)):
            bmi = int(weight) / float(height) ** 2
            if bmi <= 18.5:
                tk.messagebox.showinfo(message="You are Under Weight" + "  BMI : " + str(bmi))
            elif bmi >= 18.5 and bmi <= 24.9:
                tk.messagebox.showinfo(message="You are Normal" + "  BMI : " + str(bmi))
            elif bmi >= 25 and bmi <= 29.9:
                tk.messagebox.showinfo(message="You are Overweight" + "  BMI : " + str(bmi))
            elif bmi >= 30 and bmi <= 34.9:
                 tk.messagebox.showinfo(message="You are Obese (Class 1)" + "  BMI : " + str(bmi))
            elif bmi >= 35 and bmi <= 39.9:
                 tk.messagebox.showinfo(message="You are Obese (Class 2)" + "  BMI : " + str(bmi))
            elif bmi > 40:
                 tk.messagebox.showinfo(message="You are Extreme Obese" + "BMI : " + str(bmi))
        else:
            tk.messagebox.showinfo(message="Please enter valid number" )




def is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()


