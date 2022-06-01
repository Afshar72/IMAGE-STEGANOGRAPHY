# importing modules
from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from stegano import exifHeader as stg
from tkinter import messagebox
from tkinter import Tk, Label
from time import sleep
 
 
class LoadingSplash:
    def __init__(self):
        #setting root window
        self.root = Tk()
        self.root.config(bg="#000000")
        self.root.title("Custom Loader")
        self.root.attributes("-fullscreen", True)
       
 
 
        #loading text:
        Label(self.root, text="LOADING...", font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=520, y=320)
 
 
        #loading blocks:
        for i in range(16):
            Label(self.root, bg="#1F2732", width=2, height=1).place(x=(i+23)*23, y=450)
       
        #update root to see animation:
        self.root.update()
        self.play_animation()
        #window in main loop:
        self.root.mainloop()
   
    #loader animation:
    def play_animation(self):
        for i in range(3):
            for j in range(16):
                #make block yellow:
                Label(self.root,bg="#FFBD09", width=2, height=1 ).place(x=(j+23)*23, y=450)
                sleep(0.03)
                self.root.update_idletasks()
                #make block dark:
                Label(self.root, bg="#1F2732", width=2, height=1).place(x=(j+23)*23, y=450)
       
        else:
            self.root.destroy()
 
 
#exit
def Exit():
   LoginScreen.destroy()
def Login():
   if entry.get()=='admin' and SaveEntry.get()=='123' or entry.get()=='ashhar' and SaveEntry.get()=='qwerty'  or entry.get()=='afshar' and SaveEntry.get()=='09876' or entry.get()=='abrar' and SaveEntry.get()=='abrar123':      

 
       
 
       LoginScreen.destroy()
       if __name__  ==  "__main__":LoadingSplash()
       Screen = Tk()
       Screen.title("Image Steganography")
       Screen.config(bg="#333333")
    #    image2 =Image.open('BGBG.png')
    #    image1 = ImageTk.PhotoImage(image2)
    #    w = image1.width()
    #    h = image1.height()
       Screen.attributes('-fullscreen', True)
   
       # exit
       def Exit():
           Screen.destroy()
 
       # decoding the file
       def Decode():
           Screen.destroy()
           DecScreen = Tk()    
           DecScreen.title("Decode")
           DecScreen.attributes('-fullscreen', True)
           DecScreen.config(bg="#333333")
           label = Label(text="Decoded Message",bg= "black",fg = "white", padx=6, pady=8,font=("Times New Roman",18))
           label.place(relx=0.25, rely=0.4)
        #    SaveEntry = Entry(font=("Times New Roman",18))
        #    SaveEntry.place(relx=0.5, rely=0.2)
             
 
           
 
           def OpenFile():
            #    global FileOpen
            #    FileOpen = StringVar()
            #    FileOpen = askopenfilename(initialdir="/Desktop", title="Select the File", filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))
            #    decimage = PhotoImage(file=FileOpen)
            #    decimage_label = Label(DecScreen, image=decimage)
            #    decimage_label.place(relx=0.2, rely=0.2, relheight=0.4, relwidth=0.4)
               global FileOpen
               FileOpen = StringVar()
               FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))
 
               label2 = Label(text=FileOpen,bg= "white",fg = "black", padx=5, pady=5,font=("Times New Roman",18))
               label2.place(relx=0.5, rely=0.2)
               decimage = PhotoImage(file=FileOpen)
               decimage_label = Label(DecScreen, image=decimage,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
               decimage_label.place(relx=0.5, rely=0.2, relheight=0.4, relwidth=0.4)
 
           def Decoder():
                Message = stg.reveal(FileOpen)
                label3 = Label(text=Message,bg= "white",fg = "black", padx=5, pady=5,font=("Times New Roman",18))
                label3.place(relx=0.5, rely=0.4)
                if __name__  ==  "__main__":LoadingSplash()
                
 
           def Exit():
                DecScreen.destroy()
 
           SelectButton = Button(text="Select the file", command=OpenFile,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           SelectButton.place(relx=0.25, rely=0.2)
           EncodeButton = Button(text="Decode", command=Decoder,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           EncodeButton.place(relx=0.3, rely=0.6)
 
           EncodeButton = Button(text="Exit", command=Exit,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           EncodeButton.place(relx=0.55, rely=0.6)
       
       # encoding the file
       def Encode():
           Screen.destroy()
 
           EncScreen = Tk()
           EncScreen.title("Encode")
           EncScreen.attributes('-fullscreen', True)
           EncScreen.config(bg="#333333")
           label = Label(text="Confidential Message",bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           label.place(relx=0.1, rely=0.2)
           entry = Entry(font=("Times New Roman",18))
           entry.place(relx=0.5, rely=0.2)
           label1 = Label(text="Name of the File",bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           label1.place(relx=0.1, rely=0.3)
           SaveEntry = Entry(font=("Times New Roman",18))
           SaveEntry.place(relx=0.5, rely=0.3)
 
           def OpenFile():
               global FileOpen
               FileOpen = StringVar()
               FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))
 
               label2 = Label(text=FileOpen,bg= "white",fg = "black", padx=5, pady=5,font=("Times New Roman",18))
               label2.place(relx=0.5, rely=0.3)
               encimage = PhotoImage(file=FileOpen)
               encimage_label = Label(EncScreen, image=encimage,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
               encimage_label.place(relx=0.2, rely=0.2, relheight=0.4, relwidth=0.4)
 
           def Encoder():
               Response = messagebox.askyesno("PopUp", "Do you want to encode the image?")
               if Response == 1:
                   stg.hide(FileOpen, SaveEntry.get() + ".jpg", entry.get())
                   EncScreen.destroy()
                   if __name__  ==  "__main__":LoadingSplash()
                   StatScreen = Tk()
                   StatScreen.title("Status")
                   StatScreen.attributes('-fullscreen', True)
                   StatScreen.config(bg="#333333")
 
                   def OpenFile():
                        global FileOpen
                        FileOpen = StringVar()
                        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",filetypes=(("only jpeg files", "*jpg"), ("all type of files", "*.*")))
 
                        label2 = Label(text=FileOpen,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
                        label2.place(relx=0.3, rely=0.1)
 
                   def CheckStatus():
                        Response = messagebox.askyesno("Status", "Do you want to check the status?")
                        if Response == 1:
                               # stg.hide(FileOpen, SaveEntry.get() + ".jpg", entry.get())
                            messagebox.showinfo("Pop Up", "Successfully Encoded")
 
                   def Exit():
                        StatScreen.destroy()
                           
                   SelectButton = Button(text="Select file", command=OpenFile,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
                   SelectButton.place(relx=0.1, rely=0.1)
 
                   SelectButton = Button(text="Check Status", command=CheckStatus,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
                   SelectButton.place(relx=0.1, rely=0.5)
 
                   SelectButton = Button(text="Exit", command=Exit,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
                   SelectButton.place(relx=0.7, rely=0.5)
 
 
               else:
                    messagebox.showwarning("Pop Up", "Unsuccessful, please try again")
 
           SelectButton = Button(text="Select the file", command=OpenFile,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           SelectButton.place(relx=0.1, rely=0.4)
           EncodeButton = Button(text="Encode", command=Encoder,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
           EncodeButton.place(relx=0.4, rely=0.5)
 
 
         
           
       
 
 
 
       # creating buttons
       EncodeButton = Button(text="Encode", command=Encode,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
       EncodeButton.place(relx=0.3, rely=0.4)
 
       DecodeButton = Button(text="Decode", command=Decode,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
       DecodeButton.place(relx=0.6, rely=0.4)
       
       DecodeButton = Button(text="Exit", command=Exit,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
       DecodeButton.place(relx=0.47, rely=0.55)
 
 
 
   else:
      messagebox.showinfo("Invalid Authentication", "Invalid User ID: & Password")
 
 
# Initializing the screen
if __name__  ==  "__main__":
    LoadingSplash()
 
 
LoginScreen = Tk()
LoginScreen.title("Image Steganography")
LoginScreen.attributes('-fullscreen', True)
bg = PhotoImage(file = "login.png")
canvas1 = Canvas( LoginScreen, width = 1920,height = 1080)
 
canvas1.pack(fill = "both", expand = True)
 
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
# LoginScreen.config(bg="bgr.png")
 
#Login and password
label = Label(text="Login ID",bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
label.place(relx=0.388, rely=0.40)
entry = Entry(font=("Times New Roman",18))
entry.place(relx=0.388, rely=0.45,relheight=0.04,relwidth=0.23)
label1 = Label(text="Password",bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
label1.place(relx=0.388, rely=0.57)
SaveEntry = Entry(font=("Times New Roman",18))
SaveEntry.place(relx=0.388, rely=0.62,relheight=0.04,relwidth=0.23)
 
# creating buttons
EncodeButton = Button(text="Login", command=Login,bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
EncodeButton.place(relx=0.663, rely=0.58)
 
DecodeButton = Button(text="Exit", command=Exit, bg= "black",fg = "white", padx=5, pady=5,font=("Times New Roman",18))
DecodeButton.place(relx=0.3, rely=0.58)
 
mainloop()
 
 
 

