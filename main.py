from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class FaceRecognitionSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        # --- FIRST IMAGE ---
        # Ensure this path matches the actual location on your computer
        img1 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img1.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.f_lbl1 = Label(self.root, image=self.photoimg1)
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        # --- SECOND IMAGE ---
        img2 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img2.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl2 = Label(self.root, image=self.photoimg2)
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        # --- THIRD IMAGE ---
        img3 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img3.webp")
        # Fixed typo: changed LANC7OS to LANCZOS
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.f_lbl3 = Label(self.root, image=self.photoimg3)
        self.f_lbl3.place(x=1000, y=0, width=500, height=130)



        # --- BG IMAGE---
        img4 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img4.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        self.bg_img = Label(self.root, image=self.photoimg4)
        self.bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl=Label(self.bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="navy",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button
        img5 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img5.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(self.bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(self.bg_img,text="Employee Details",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=200,y=300,width=220,height=40)


        #detect button
        img6 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img6.webp")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(self.bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(self.bg_img,text="Face Detector",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=500,y=300,width=220,height=40)


        #dattendance face button
        img7 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img7.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(self.bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1=Button(self.bg_img,text="Attendance",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=800,y=300,width=220,height=40)


        #help button
        img8 = Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img8.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(self.bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1=Button(self.bg_img,text="Help",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=1100,y=300,width=220,height=40)


        #train face button
        img9= Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img9.webp")
        img9= img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(self.bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1=Button(self.bg_img,text="Train Face",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=200,y=600,width=220,height=40)


        #photos face button
        img10= Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img10.jpg")
        img10= img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(self.bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)

        b1=Button(self.bg_img,text="Photos",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=500,y=600,width=220,height=40)


        #developerbutton
        img11= Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img11.AVIF")
        img11= img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(self.bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1=Button(self.bg_img,text="Developer Info",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=800,y=600,width=220,height=40)


        #exit button
        img12= Image.open(r"C:\Users\atifa\OneDrive\Desktop\pictures\img12.jpg")
        img12= img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1=Button(self.bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1=Button(self.bg_img,text="Exit",cursor="hand2",font=("comic sans ms",15,"bold"),bg="skyblue",fg="navy")
        b1.place(x=1100,y=600,width=220,height=40)

if __name__=="__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()    





