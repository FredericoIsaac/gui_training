from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.title("Client Relation Manager")
root.geometry("400x400")


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
)

print(mydb)