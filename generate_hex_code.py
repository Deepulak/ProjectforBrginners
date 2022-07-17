from tkinter import *
from tkinter import ttk
import random

class main:
	def __init__(self, master):
		self.master = master
		self.color = StringVar()
		self.widgets()

	def change(self):
		col = "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		self.color.set(col)
		self.preview.configure(bg=col)

	def widgets(self):
		Button(self.master, bd=10, text="Get Hex-Code", font=("algerian", 20), command=self.change).pack()
		ttk.Entry(self.master, textvariable=self.color, font=("algerian", 20)).pack(pady=10)
		self.preview = Frame(self.master, bd=10, relief=RIDGE, height=300, width=300, bg="white")
		self.preview.pack(pady=10)

if __name__ == "__main__":
	root = Tk()
	main(root)
	root.title("Hex Code")
	root.mainloop()
