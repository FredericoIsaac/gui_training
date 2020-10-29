from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap(r'C:\Users\Frede\OneDrive\Ambiente de Trabalho\Frederico Gago\Educação\Programação\Python\projects_GUI\gui_training\exe\codemy.ico')
root.geometry("400x400")


def myClick():
	global myLabel
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	e.delete(0, 'end')
	myLabel.pack(pady=10)
	#myButton["state"] = DISABLED

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)

# Overwrite the existing label (pack system)
def myDelete():
    	#myLabel.pack_forget()
		myLabel.destroy()
		myButton["state"] = NORMAL

deleteButton = Button(root, text="Delete Text", command=myDelete)
deleteButton.pack(pady=10)


root.mainloop()