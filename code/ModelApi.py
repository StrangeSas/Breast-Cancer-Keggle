from tkinter import *
from tkinter import ttk
import pickle
import pandas as pd
import numpy as np


def answer_geting() -> np.array:
    all_entries = list({i.get() for i in boxes})
    result = np.array(all_entries, dtype=np.float64)
    print(type(result[0]))
    print(result)
    return result

def answer_validation(result):
    n = int(0)
    for i in result:
        if type(i) == np.string_ :
            n += 1
    if n > 0 :
        return False
    else:
        return True

def calculate_result():
    stuff = answer_geting()

    if answer_validation(stuff) == False:
        label1 = Label(app_window, text="you have non number in your entries")
        label1.pack(anchor=NW, padx=20, pady=6)
        return
    else:
        example = model.predict([stuff])
        label1 = Label(app_window, text=example)
        label1.pack(anchor=NW, padx=20, pady=6)
        return(example)



with open("breast_cancer.pkl", "rb") as w:
    model = pickle.load(w)
with open("columns.pkl", "rb") as w:
    columns = list(pickle.load(w))
value = pd.DataFrame()

app_window = Tk()
app_window.title("Breast cancer model")
frame1 = Frame(app_window)
frame1.pack()

boxes = list()

n = 0

for i in columns:
    boxes.append(Entry(frame1, width=30, name=str(i)))
    boxes[n].insert(0, "{}".format(0))
    boxes[n].pack(padx=10, pady=5)
    n +=1


btn = ttk.Button(text="Calculate", command=calculate_result)
btn.pack(anchor=NW, padx=6,pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6,pady=6)
app_window.mainloop()
