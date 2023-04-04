'''
GUI for demonstrating the difficulty in distinguishing between
real and synthetic images of Greek characters from ancient papyri.

Matthew Swindall
Ancient Live Project

For MTSU Scholars Day Presentation

Based on: Dataset Augmentation in Papyrology with Generative Models: A Study of Synthetic Ancient Greek Character Images
            Pending publication at IJCAI 20222222
'''

# Import necessary libraries
from tkinter import messagebox, Label, Tk, simpledialog
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font
import os
import pandas as pd
import random
# Avoid recursion error by increasing resursion limit
import sys
sys.setrecursionlimit(10**6)

dim = (140, 140)

# Initialize global variables
global checker, guess, labels, grid, counter, one, two, three, four, five, six, seven, eight, nine,ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive
global photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, photo11, photo12, photo13, photo14, photo15, photo16, photo17, photo18, photo19, photo20, photo21, photo22, photo23, photo24, photo25, QR, qr, qrimage

# Initializing variables
frompath = "anonymized/"
fnames = []

# Creating list of char images
for (root, dirs, files) in os.walk(frompath, topdown=True):
    for fname in files:
        fnames.append(str(os.path.join(root, fname)))

# Randomize list of files to sort
grid = random.sample(fnames, 25)
labels = []


# Initialize GUI parameters
pad = tk.Tk()
pad.attributes('-fullscreen', True)
pad.title("CAN YOU TELL WHICH CHARACTERS ARE SYNTHETIC?")#\N CLICK ON THE SYNTHETIC IMAGES, THEN CLICK 'CHECK'")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')
myFont2 = tkinter.font.Font(family = 'Helvetica', size = 28, weight = 'bold')
myFont3 = tkinter.font.Font(family = 'Helvetica', size = 32, weight = 'bold')

check = Image.open("check.png")
check = check.resize(dim)
mark = ImageTk.PhotoImage(check)

qrimage = Image.open("synth_site_QR.png")
qrimage = qrimage.resize(dim)
qr = ImageTk.PhotoImage(qrimage)

df = pd.read_csv("anonymization_key.csv", index_col=0)
ids = list(df["Anonymized ID"])
vals = list(df["Catagory"])
adict = dict(zip(ids, vals))

for g in grid:
    imgid = int(g.split("/")[1][:-4])
    cat = adict[imgid]
    labels.append(cat)
    
# Build Functions for buttons

def One():
    global grid, one, guess
    guess.append(0)
    one.config(image = mark)

def Two():
    global grid, two, guess
    guess.append(1)
    two.config(image = mark)

def Three():
    global grid, three, guess
    guess.append(2)
    three.config(image = mark)

def Four():
    global grid, four, guess
    guess.append(3)
    four.config(image = mark)

def Five():
    global grid, five, guess
    guess.append(4)
    five.config(image = mark)

def Six():
    global grid, six, guess
    guess.append(5)
    six.config(image = mark)

def Seven():
    global grid, seven, guess
    guess.append(6)
    seven.config(image = mark)

def Eight():
    global grid, eight, guess
    guess.append(7)
    eight.config(image = mark)

def Nine():
    global grid, nine, guess
    guess.append(8)
    nine.config(image = mark)
    
def Ten():
    global guess, grid, ten
    guess.append(9)
    ten.config(image = mark)

def Eleven():
    global guess, grid, eleven
    guess.append(10)
    eleven.config(image = mark)

def Twelve():
    global guess, grid, twelve
    guess.append(11)
    twelve.config(image = mark)

def Thirteen():
    global guess, grid, thirteen
    guess.append(12)
    thirteen.config(image = mark)

def Fourteen():
    global guess, grid, fourteen
    guess.append(13)
    fourteen.config(image = mark)

def Fifteen():
    global guess, grid, fifteen
    guess.append(14)
    fifteen.config(image = mark)

def Sixteen():
    global guess, grid, sixteen
    guess.append(15)
    sixteen.config(image = mark)

def Seventeen():
    global guess, grid, seventeen
    guess.append(16)
    seventeen.config(image = mark)

def Eighteen():
    global guess, grid, eighteen
    guess.append(17)
    eighteen.config(image = mark)

def Nineteen():
    global guess, grid, nineteen
    guess.append(18)
    nineteen.config(image = mark)

def Twenty():
    global guess, grid, twenty
    guess.append(19)
    twenty.config(image = mark)

def TwentyOne():
    global guess, grid, twentyone
    guess.append(20)
    twentyone.config(image = mark)

def TwentyTwo():
    global guess, grid, twentytwo
    guess.append(21)
    twentytwo.config(image = mark)

def TwentyThree():
    global guess, grid, twentythree
    guess.append(22)
    twentythree.config(image = mark)

def TwentyFour():
    global guess, grid, twentyfour
    guess.append(23)
    twentyfour.config(image = mark)

def TwentyFive():
    global guess, grid, twentyfive
    guess.append(24)
    twentyfive.config(image = mark)

def Close():
    # Closes Program
    pad.destroy()
    exit()

def Check():
    global grid, guess, labels
    checker = ["real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real", "real"]
    for g in guess:
        checker[g] = "synthetic"
    correct = 0
    acc = 0
    #for k in range(25):
    #    print(checker[k], labels[k])
    #print("*************************")
    for i in range(25):
        if checker[i] == labels[i]:
            correct += 1
    acc = (correct/25)*100
    display = "Your accuracy: {:0.2f}%\n Try again!".format(acc)
    messagebox.showinfo("Accuracy", display)
    
    grid = random.sample(fnames, 25)
    labels = []
    for g in grid:
        imgid = int(g.split("/")[1][:-4])
        cat = adict[imgid]
        labels.append(cat)
    pad.update()
    Window()
    
def Window():
    global guess, labels, grid, counter, one, two, three, four, five, six, seven, eight, nine,ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive
    global photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, photo11, photo12, photo13, photo14, photo15, photo16, photo17, photo18, photo19, photo20, photo21, photo22, photo23, photo24, photo25
    guess = []
    
    pic1 = grid[0]
    img1 = Image.open(pic1)
    img1 = img1.resize(dim)
    photo1 = ImageTk.PhotoImage(img1)
    
    pic2 = grid[1]
    img2 = Image.open(pic2)
    img2 = img2.resize(dim)
    photo2 = ImageTk.PhotoImage(img2)
    
    pic3 = grid[2]
    img3 = Image.open(pic3)
    img3 = img3.resize(dim)
    photo3 = ImageTk.PhotoImage(img3)
    
    pic4 = grid[3]
    img4 = Image.open(pic4)
    img4 = img4.resize(dim)
    photo4 = ImageTk.PhotoImage(img4)
    
    pic5 = grid[4]
    img5 = Image.open(pic5)
    img5 = img5.resize(dim)
    photo5 = ImageTk.PhotoImage(img5)
    
    pic6 = grid[5]
    img6 = Image.open(pic6)
    img6 = img6.resize(dim)
    photo6 = ImageTk.PhotoImage(img6)
    
    pic7 = grid[6]
    img7 = Image.open(pic7)
    img7 = img7.resize(dim)
    photo7 = ImageTk.PhotoImage(img7)
    
    pic8 = grid[7]
    img8 = Image.open(pic8)
    img8 = img8.resize(dim)
    photo8 = ImageTk.PhotoImage(img8)
    
    pic9 = grid[8]
    img9 = Image.open(pic9)
    img9 = img9.resize(dim)
    photo9 = ImageTk.PhotoImage(img9)
    
    pic10 = grid[9]
    img10 = Image.open(pic10)
    img10 = img10.resize(dim)
    photo10 = ImageTk.PhotoImage(img10)
    
    pic11 = grid[10]
    img11 = Image.open(pic11)
    img11 = img11.resize(dim)
    photo11 = ImageTk.PhotoImage(img11)
    
    pic12 = grid[11]
    img12 = Image.open(pic12)
    img12 = img12.resize(dim)
    photo12 = ImageTk.PhotoImage(img12)
    
    pic13 = grid[12]
    img13 = Image.open(pic13)
    img13 = img13.resize(dim)
    photo13 = ImageTk.PhotoImage(img13)
    
    pic14 = grid[13]
    img14 = Image.open(pic14)
    img14 = img14.resize(dim)
    photo14 = ImageTk.PhotoImage(img14)
    
    pic15 = grid[14]
    img15 = Image.open(pic15)
    img15 = img15.resize(dim)
    photo15 = ImageTk.PhotoImage(img15)
    
    pic16 = grid[15]
    img16 = Image.open(pic16)
    img16 = img16.resize(dim)
    photo16 = ImageTk.PhotoImage(img16)
    
    pic17 = grid[16]
    img17 = Image.open(pic17)
    img17 = img17.resize(dim)
    photo17 = ImageTk.PhotoImage(img17)
    
    pic18 = grid[17]
    img18 = Image.open(pic18)
    img18 = img18.resize(dim)
    photo18 = ImageTk.PhotoImage(img18)
    
    pic19 = grid[18]
    img19 = Image.open(pic19)
    img19 = img19.resize(dim)
    photo19 = ImageTk.PhotoImage(img19)
    
    pic20 = grid[19]
    img20 = Image.open(pic20)
    img20 = img20.resize(dim)
    photo20 = ImageTk.PhotoImage(img20)
    
    pic21 = grid[20]
    img21 = Image.open(pic21)
    img21 = img21.resize(dim)
    photo21 = ImageTk.PhotoImage(img21)
    
    pic22 = grid[21]
    img22 = Image.open(pic22)
    img22 = img22.resize(dim)
    photo22 = ImageTk.PhotoImage(img22)
    
    pic23 = grid[22]
    img23 = Image.open(pic23)
    img23 = img23.resize(dim)
    photo23 = ImageTk.PhotoImage(img23)
    
    pic24 = grid[23]
    img24 = Image.open(pic24)
    img24 = img24.resize(dim)
    photo24 = ImageTk.PhotoImage(img24)
    
    pic25 = grid[24]
    img25 = Image.open(pic25)
    img25 = img25.resize(dim)
    photo25 = ImageTk.PhotoImage(img25)
    # Build GUI buttons

    # ROW 1
    one = tk.Button(pad, image = photo1, command = One)
    one.grid(row=1, column=1)
    
    two = tk.Button(pad, image = photo2, command = Two)
    two.grid(row=1, column=2)
    
    three = tk.Button(pad, image = photo3, command = Three)
    three.grid(row=1, column=3)
    
    four = tk.Button(pad, image = photo4, command = Four)
    four.grid(row=1, column=4)
    
    five = tk.Button(pad, image = photo5, command = Five)
    five.grid(row=1, column=5)
    
    # ROW 2
    six = tk.Button(pad, image = photo6, command = Six)
    six.grid(row=2, column=1)
    
    seven = tk.Button(pad, image = photo7, command = Seven)
    seven.grid(row=2, column=2)
    
    eight = tk.Button(pad, image = photo8, command = Eight)
    eight.grid(row=2, column=3)
    
    nine = tk.Button(pad, image = photo9, command = Nine)
    nine.grid(row=2, column=4)
    
    ten = tk.Button(pad, image = photo10, command = Ten)
    ten.grid(row=2, column=5)
    
    # ROW 3
    eleven = tk.Button(pad, image = photo11, command = Eleven)
    eleven.grid(row=3, column=1)
    
    twelve = tk.Button(pad, image = photo12, command = Twelve)
    twelve.grid(row=3, column=2)
    
    thirteen = tk.Button(pad, image = photo13, command = Thirteen)
    thirteen.grid(row=3, column=3)
    
    fourteen = tk.Button(pad, image = photo14, command = Fourteen)
    fourteen.grid(row=3, column=4)
    
    fifteen = tk.Button(pad, image = photo15, command = Fifteen)
    fifteen.grid(row=3, column=5)

    # ROW 4
    sixteen = tk.Button(pad, image = photo16, command = Sixteen)
    sixteen.grid(row=4, column=1)
    
    seventeen = tk.Button(pad, image = photo17, command = Seventeen)
    seventeen.grid(row=4, column=2)
    
    eighteen = tk.Button(pad, image = photo18, command = Eighteen)
    eighteen.grid(row=4, column=3)
    
    nineteen = tk.Button(pad, image = photo19, command = Nineteen)
    nineteen.grid(row=4, column=4)
    
    twenty = tk.Button(pad, image = photo20, command = Twenty)
    twenty.grid(row=4, column=5)
    
    # ROW 5
    twentyone = tk.Button(pad, image = photo21, command = TwentyOne)
    twentyone.grid(row=5, column=1)
    
    twentytwo = tk.Button(pad, image = photo22, command = TwentyTwo)
    twentytwo.grid(row=5, column=2)
    
    twentythree = tk.Button(pad, image = photo23, command = TwentyThree)
    twentythree.grid(row=5, column=3)
    
    twentyfour = tk.Button(pad, image = photo24, command = TwentyFour)
    twentyfour.grid(row=5, column=4)
    
    twentyfive = tk.Button(pad, image = photo25, command = TwentyFive)
    twentyfive.grid(row=5, column=5)
    
    # ROW 6
    #msg = tk.Button(pad, font = myFont, text = "Click the synthetic images", fg = "black", bg = "gray")
    #msg.grid(row=6, column=1)
    
    check = tk.Button(pad, font = myFont2, text = "Check", fg = "black", bg = "gray", command = Check)
    check.grid(row=7, column=3)
    
    M1 = tk.Label(pad, font = myFont3, text = "       Synthetic Greek Character Challenge", fg = "black")
    M1.grid(row=1, column=6)
    
    M2 = tk.Label(pad, font = myFont2, text = "       Some images are Greek characters from ancient papyri", fg = "black")
    M2.grid(row=2, column=6)
    
    M3 = tk.Label(pad, font = myFont2, text = "       Some of them, are synthetically generated by an AI model", fg = "black")
    M3.grid(row=3, column=6)
    
    M4 = tk.Label(pad, font = myFont2, text = "       Our experts were 55.14% accurate on average", fg = "black")
    M4.grid(row=4, column=6)
    
    M5 = tk.Label(pad, font = myFont2, text = "       How well can you do?", fg = "black")
    M5.grid(row=5, column=6)
    
    M6 = tk.Label(pad, font = myFont2, text = "       Click on the synthetic images, then the 'CHECK' button", fg = "black")
    M6.grid(row=6, column=6)
    
    M7 = tk.Label(pad, font = myFont2, text = "       To learn more about synthetic Greek characters, scan QR ", fg = "black")
    M7.grid(row=8, column=6)
    
    QR = tk.Label(pad, font = myFont2, text="", fg = "black", image = qr)
    QR.grid(row=9, column=6)
    
    pad.mainloop()

# Begin GUI mainloop
Window()

