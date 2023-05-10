from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student



class Student_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")


        # First Image
        img=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\IcbtLogo.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)


        # Second Image
        img1=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\facialrecognition.png")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)


        # Third Image 
        img2=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\cardiff.jpg")
        img2=img2.resize((520,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=520, height=150)


        # Background Image
        img3=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\Teacher-with-students-1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=710)


        # Titile - ICBT CAMPUS - STUDENT ATTENDENCE SYSTEM
        title_lbl=Label(bg_img,text="ICBT CAMPUS - STUDENT ATTENDENCE SYSTEM",font=("times new roman",28,"bold"),bg="grey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=50)


        # Button - STUDENT DETAILS
        img4=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\std.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        # Button - FACE DETECTOR
        img5=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\fad.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        # Button - ATTENDENCE
        img6=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\attendant.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="ATTENDENCE",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        # Button - REGISTER ADMIN
        img7=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\employee.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="REGISTER ADMIN",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # Button - TRAIN DATA
        img8=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        # Button - PHOTOS
        img9=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\photos.jpeg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        # Button - DEVELOPER
        img10=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        # Button - EXIT
        img11=Image.open(r"D:\01. Project\Student-Attendance-System\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)


    # Functions Button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student( self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Student_Attendance_System(root)
    root.mainloop()