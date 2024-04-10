import numpy as np
from tkinter import *

root = Tk()
root.title("l6 Розв'язання квадратного рівняння")
root.geometry('1200x500+500+300')
#root.minsize(600, 240)
root.resizable(0, 0)

fontSize = 28
arrVar = np.empty(20, StringVar)
for i in range(20):
	arrVar[i] = StringVar(root, value='0')
resVar = StringVar(root, value='')

def callback():
	matrixA = np.empty((4, 4))
	for i in range(4):
		for j in range(4):
			matrixA[i][j] = arrVar[i*4 + j].get()

	arrB = np.empty(4)
	for i in range(4):
		arrB[i] = arrVar[16 + i].get()

	detA = np.linalg.det(matrixA)

	if (detA == 0):
		resVar.set(value="Корені не знайдено!")
		return
	
	tmp = np.array(matrixA)
	for i in range(4):
		tmp[i][0] = arrB[i]

	x1 = np.linalg.det(tmp) / detA

	tmp = np.array(matrixA)
	for i in range(4):
		tmp[i][1] = arrB[i]

	x2 = np.linalg.det(tmp) / detA
	
	tmp = np.array(matrixA)
	for i in range(4):
		tmp[i][2] = arrB[i]

	x3 = np.linalg.det(tmp) / detA
	
	tmp = np.array(matrixA)
	for i in range(4):
		tmp[i][3] = arrB[i]

	x4 = np.linalg.det(tmp) / detA

	resVar.set(value="x₁ = " + str(round(x1, 3)) + "  x₂ = " + str(round(x2, 3)) + "\nx₃ = " +  str(round(x3, 3)) + 
			"  x₄ = " + str(round(x4, 3)))

for i in range(4):
	for j in range(4):
		Entry(root, textvariable=arrVar[i*4 + j], font=("Arial", fontSize), width=7).grid(row=i, column=j*2, padx=5, pady=5)

for i in range(4):
	for j in range(3):
		Label(root, text=("x" + chr(0x2081 + j) + " + "), font=("Arial", fontSize)).grid(row=i, column=j*2+1, padx=5, pady=5)

for i in range(4):
	Label(root, text=("x" + chr(0x2084) + " = "), font=("Arial", fontSize)).grid(row=i, column=7, padx=5, pady=5)
	Entry(root, textvariable=arrVar[16 + i], font=("Arial", fontSize), width=7).grid(row=i, column=8, padx=5, pady=5)

button = Button(root, bg="#FFE4B5", text="Старт", font=("Arial", fontSize), command=callback, width=15, height=2)
button.grid(row=5, column=0, columnspan=4, rowspan=4, padx=5, pady=6)

frame = LabelFrame(root, text="Розв'язок", borderwidth=4, font=("Arial", fontSize), labelanchor='n')

label = Label(frame, textvariable=resVar, font=("Arial", fontSize), width=20, height=4).pack(fill='both', expand=True)

frame.grid(row=5, column=5, columnspan=5, rowspan=4, padx=5, pady=6)

root.mainloop()