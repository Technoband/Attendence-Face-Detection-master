from tkinter import *
from Functions import *
from attendanceWebcam import *
from attendanceVideo import *
from attendanceImage import *
from tkinter import filedialog
import tkinter.messagebox
from PIL import ImageTk, Image


def clickCapture():
    ans = tkinter.messagebox.askyesno("Confirm", "Do you want to capture image?")
    if ans:
        name = enterName.get()
        captureImage(name)


def startProgramWebcam():
    tkinter.messagebox.showinfo("Info", "Please wait a while, Processing your Database Images...")
    startWebcam()


def startProgram():
    rootStart = Tk()
    rootStart.title("Choose Option")
    rootStart.minsize(500, 80)
    rootStart.maxsize(500, 80)
    rootStart.configure(bg="#888888")
    rootStart.geometry('%dx%d+%d+%d' % (500, 80, 300, 600))
    Button(rootStart, text="Video", fg="#000000", bg="#11A5E4", width=25, height=2,command=callStartVideo).pack(side='left', padx=(40, 0))
    Button(rootStart, text="Image", fg="#000000", bg="#11A5E4", width=25, height=2,command=callStartImage).pack(side='right', padx=(0, 40))


def callStartImage():
    filename = filedialog.askdirectory(initialdir=os.path.dirname(__file__), title="Select Folder")
    if len(filename) > 0:
        startImage(filename)
    else:
        tkinter.messagebox.showinfo("Info", "Please select Image Folder")


def callStartVideo():
    filename = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title="Select Folder")
    if len(filename) > 0:
        startVideo(filename)
    else:
        tkinter.messagebox.showinfo("Info", "Please select Video")


def openExcelOption():
    rootExcel = Tk()
    rootExcel.title("Choose Option")
    rootExcel.minsize(380, 140)
    rootExcel.maxsize(380, 140)
    rootExcel.configure(bg="#888888")
    rootExcel.geometry('%dx%d+%d+%d' % (380, 140, 300, 600))
    Button(rootExcel, text="Attendance Live Webcam", fg="#000000", bg="#0AC2F0", width=25, height=2, command=openExcelWebcam).pack(pady=(5, 2))
    Button(rootExcel, text="Attendance Image", fg="#000000", bg="#0AC2F0", width=25, height=2, command=openExcelImage).pack(pady=(0, 2))
    Button(rootExcel, text="Attendance Video", fg="#000000", bg="#0AC2F0", width=25, height=2, command=openExcelVideo).pack(pady=(0, 5))


root = Tk()
root.title('Facial Recognition Attendance Program (Alpha-Version V1.0)')
root.minsize(910, 750)
root.maxsize(910, 750)
root.configure(background="#FFFFFF")

heading = Label(root, text="Welcome to BVCOE \n Admin Panel", fg='#000000', bg="#ECD705")
heading.configure(font=("Cambria", 35))
heading.pack(fill="x")

img = ImageTk.PhotoImage(Image.open('Logo/logo.png'))
labelImage = Label(root, image=img, borderwidth=0)
labelImage.pack(pady=20)

enterName = Entry(root, fg="#FFFFFF", bg="#000000")
enterName.configure(font=20)
enterName.pack()

btn1 = Button(root, text="Add Image to Database", fg="#000000", bg="#08CAF0", width=25, height=2, command=clickCapture).pack(pady=(5, 20))
btn2 = Button(root, text="Mark Your Live Attendence ", fg="#000000", bg="#08CAF0", width=25, height=2, command=startProgramWebcam).pack(pady=(0, 20))
btn3 = Button(root, text="Import Image/Video", fg="#000000", bg="#08CAF0", width=25, height=2, command=startProgram).pack(pady=(0, 20))
btn4 = Button(root, text="Open Attendance Sheet", fg="#000000", bg="#08CAF0", width=25, height=2, command=openExcelOption).pack(pady=(0, 20))
# btn5 = Button(root, text="Read Me", fg="#000000", bg="#08CAF0", width=25, height=2, command=openReadme).pack(pady=(0, 20))

root.mainloop()
