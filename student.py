from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")


                # First Image
        img=Image.open(r"D:\05. ICBT Notes\Student-Attendance-System\college_images\IcbtLogo.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        # Second Image
        img1=Image.open(r"D:\05. ICBT Notes\Student-Attendance-System\college_images\facialrecognition.png")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

        # Third Image 
        img2=Image.open(r"D:\05. ICBT Notes\Student-Attendance-System\college_images\cardiff.jpg")
        img2=img2.resize((520,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=520, height=150)



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()