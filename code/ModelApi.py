from tkinter import *
from tkinter import ttk
import pickle
import pandas as pd
import numpy as np




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
stuff = np.full([len(columns), 1], 1)
for i in columns:
    boxes.append(Entry(frame1, width=30))
    boxes[n].insert(0, "{}".format(stuff[n]))
    boxes[n].pack(padx=10, pady=5)
    n +=1

def calculate_result(numbers: np.array) -> np.array:
    array_of_numbers = np.array({i for i in boxes})
    print(array_of_numbers)
    value[columns] = np.array(stuff).reshape((1, -1))

    print(value)
    example = model.predict(value)
    return(example)



btn = ttk.Button(text="Calculate", command=calculate_result(stuff))
btn.pack(anchor=NW, padx=6,pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6,pady=6)
app_window.mainloop()
