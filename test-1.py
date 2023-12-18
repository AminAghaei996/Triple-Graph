from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk

import pandas as pd
import matplotlib.pyplot as plt

Select_Cnt=0
selection=[]
ColorTable=['blue','orange','green']
Country_Names=[]   

ProcessedData = pd.read_csv(r'C:\OTHER FILES\University\3. Fall 2023\Planning For changes In Information Technology\Python\Pandas\Tkinter-1\Data.csv')
column1_list = ProcessedData['Country Name'].tolist()

def selection_changed(event):
    global Select_Cnt
    global selection
    #selection[Select_Cnt] = combo.current()
    selection.insert(Select_Cnt, combo.current())
    Selection_name=combo.get()
    Select_Cnt=Select_Cnt+1
    messagebox.showinfo(
        title="New Selection",
        message=f"Selected option: {Selection_name}"
    )
    if Select_Cnt==1:
        c1_Lable = Label(text = f"First Country:   {Selection_name}").place(x = 50,   y = 80) 
        Country_Names.insert(1,f"{Selection_name}")
    if Select_Cnt==2:   
        c2_Lable = Label(text = f"Second Country:  {Selection_name}").place(x = 50,   y = 100) 
        Country_Names.insert(2,f"{Selection_name}")
    if Select_Cnt==3:   
        c3_Lable = Label(text = f"Third Country:   {Selection_name}").place(x = 50,   y = 120) 
        Country_Names.insert(3,f"{Selection_name}")
    if Select_Cnt==3:
        Select_Cnt=0
        for cnt in range(3):  
            row = ProcessedData.loc[selection[cnt],"1960":"2022"]  #mylist.insert(location,value)
            plt.xlabel("Year") 
            plt.ylabel("% of Urban Population to total the population")
            plt.title("Urban Population")
            plt.plot(row, color=ColorTable[cnt], label=Country_Names[cnt])
            plt.xticks(rotation=90)
            plt.legend() 
       #plt.figure()
        plt.show()
        

main_window = tk.Tk()
main_window.config(width=350, height=200)
main_window.title("Urban Population Data Analysis")
combo = ttk.Combobox(state="readonly",values=column1_list)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=50)
Selection_Lable= Label(text = "Select Country").place(x = 50,   y = 25) 
c1_Lable = Label(text = "First Country:").place(x = 50,   y = 80) 
c2_Lable = Label(text = "Second Country:").place(x = 50,   y = 100) 
c3_Lable = Label(text = "Third Country:").place(x = 50,   y = 120) 
main_window.mainloop()
