import tkinter as tk,math, random,sys,os,time,turtle
import random
 
from turtle import Screen, ScrolledCanvas, RawTurtle, TurtleScreen, bgcolor, fillcolor, left, width
from tkinter import messagebox as msg
from PyDictionary import PyDictionary
from tkinter import *
from tkinterweb import HtmlFrame
from winsound import *
from tkinter.colorchooser import askcolor


alphabet = {
    'A': ((0,0),(0.5,1),(0.75,0.5),(0.25,0.5),(0.75,0.5),(1,0)),
    'B': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.75,0.375),(0.75,0.125),(0.625,0),(0,0)),
    'C': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'D': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.125),(0.625,0),(0,0)),
    'E': ((0.75,0),(0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'F': ((0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'G': ((0.75,0.5),(0.625,0.5),(0.75,0.5),(0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'H': ((0,0),(0,1),(0,0.5),(0.75,0.5),(0.75,1),(0.75,0)),
    'I': ((0,0),(0.25,0),(0.125,0),(0.125,1),(0,1),(0.25,1)),
    'J': ((0,0.125),(0.125,0),(0.375,0),(0.5,0.125),(0.5,1)),
    'K': ((0,0),(0,1),(0,0.5),(0.75,1),(0,0.5),(0.75,0)),
    'L': ((0,0),(0,1),(0,0),(0.75,0)),
    'M': ((0,0),(0,1),(0.5,0),(1,1),(1,0)),
    'N': ((0,0),(0,1),(0.75,0),(0.75,1)),
    'O': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125)),
    'P': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5)),
    'Q': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125),(0.875,0)),
    'R': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.875,0)),
    'S': ((0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,0.375),(0.675,0.5),(0.125,0.5),(0,0.625),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'T': ((0,1),(0.5,1),(0.5,0),(0.5,1),(1,1)),
    'U': ((0,1),(0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,1)),
    'V': ((0,1),(0.375,0),(0.75,1)),
    'W': ((0,1),(0.25,0),(0.5,1),(0.75,0),(1,1)),
    'X': ((0,0),(0.375,0.5),(0,1),(0.375,0.5),(0.75,1),(0.375,0.5),(0.75,0)),
    'Y': ((0,1),(0.375,0.5),(0.375,0),(0.375,0.5),(0.75,1)),
    'Z': ((0,1),(0.75,1),(0,0),(0.75,0)),
}


def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def quit():
    global root
    root.quit()

root=Tk()
root.title("ALPHABETIC TUTOR")
root.iconbitmap(resource_path0("0.ico"))
root.geometry("1280x1000")


dictionary = PyDictionary()

frame = Frame(root, borderwidth=10 , bg = "pink" )
frame11 = Frame(root, bg = "#33A4FF")
frame22=Frame(root,bg="cyan")
frame33 = Frame(root, bg = "pink")
frame44 = Frame(root, bg = "orange")
frame55 = Frame(root,width=155,height=100,padx=2, )
wframe = Text(root, bg = "#F6F4A7",width=155,height=100,padx=2,)
iframe = Text(root, bg = "white",width=155,height=100,padx=2,)
gframe = HtmlFrame(root,messages_enabled = False)  

dframe = Frame(root)


def hide_prev_frames():
    frame.pack_forget()
    frame11.pack_forget()
    frame22.pack_forget()
    frame33.pack_forget()
    frame44.pack_forget()
    frame55.pack_forget()
    wframe.pack_forget()
    iframe.pack_forget()
    dframe.pack_forget()
    gframe.pack_forget()
    
    
    
def sound():
    hide_prev_frames()
    msg.showinfo("TIP","On tapping the button ,you get the pronouncation")
   
    frame.pack(fill = BOTH, expand = True )

   
    store=tk.StringVar()

    def sound1(j):
        store.set(PlaySound(resource_path0(j),SND_FILENAME))
 
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 

    for p in alphabets:
        i=p.upper()
        sb=Button(frame,text=i,command=lambda j = i: sound1(j),padx=7,bg="#ffb3fe")
        sb.pack(side=LEFT,padx=6)    

def words():
    
    hide_prev_frames()
    msg.showinfo("TIP","On tapping the button ,you get list of the words")
    frame11.pack(fill = BOTH, expand = True)
 

    store=tk.StringVar()

    def words1(j):
        wframe.pack(fill = BOTH, )
        wframe.delete(1.0,END)
        wframe.delete("1.0","end")
        wordsfile=open(resource_path0(j+".txt"),"r") 
        wordsfile1=wordsfile.read()
        wframe.delete(1.0,END)
        wframe.delete("1.0","end")
        wframe.insert(END,wordsfile1)
        wordsfile.close()

 
 
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 

    for p in alphabets:
        i=p.upper()
        wb=Button(frame11,text=i,command=lambda j = i: words1(j),padx=7,bg="#ffb3fe")
        wb.pack(side=LEFT,padx=6)    



def image():
    hide_prev_frames()
    msg.showinfo("TIP","On tapping the button ,you get images")
    frame22.pack(fill = BOTH, expand = True)
    
    store=tk.StringVar()

    def img(j):
      
        iframe.pack(fill = BOTH, )
        global img
        img=PhotoImage(file=resource_path0(j+".png"))
     
        iframe.delete(1.0,END)
        iframe.delete("1.0","end")
        iframe.image_create(END,image=img)

  

 
 
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 

    for p in alphabets:
        i=p.upper()
        ib=Button(frame22,text=i,command=lambda j = i: img(j),padx=7,bg="#ffb3fe")
        ib.pack(side=LEFT,padx=6)    

def howto():
    hide_prev_frames()
    msg.showinfo("TIP","On tapping the button ,letter is drawn")
    frame33.pack(fill = BOTH, expand = True )
    store=tk.StringVar()
   

    def howto(j):
        newwindow=Toplevel(root)
        newwindow.iconbitmap(resource_path0("0.ico"))
        newwindow.title("HOW TO")
       

        canvas = ScrolledCanvas(newwindow,width=1000,height=900)
        canvas.pack()
        screen = TurtleScreen(canvas)
        myPen = turtle.RawTurtle(canvas)
        myPen.hideturtle()
        myPen.speed(3)
        window = screen
        
        myPen.pensize(5)
        

        def displayMessage(j,fontSize,color,x,y):
            
            myPen.color(color)
            j=j.upper()
            
            for character in j:
                if character in alphabet:
                    letter=alphabet[character]
                    myPen.penup()
                    for dot in letter:
                        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
                        myPen.pendown()
                    
                    x += fontSize
                
                if character == " ":
                    x += fontSize
                x += characterSpacing 
                
            #Main Program Starts Here
        fontSize = 300
        characterSpacing = 1
        fontColor = "#FF00FF"
 
        displayMessage(j,fontSize,fontColor,-200,-110)
        time.sleep(1)
         
        time.sleep(1)
        newwindow.destroy()
        


 
        
    

        

    
    
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    

    for p in alphabets:
        i=p.upper()
        hb=Button(frame33,text=i,command=lambda j = i: howto(j),padx=7,bg="#ffb3fe")
        hb.pack(side=LEFT,padx=6)  

 
 
 



def slate():
    hide_prev_frames()
    msg.showinfo("TIP","just like a paint")
    msg.showinfo("TIP","to increase the size of brush,increase the slider")
    frame44.pack(fill = BOTH, expand = True)
    class Paint(object):

        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'

        def __init__(self):
            self.frame44 = frame44

            self.pen_button = Button(self.frame44, text='pen', command=self.use_pen)
            self.pen_button.grid(row=0, column=0)

            self.brush_button = Button(self.frame44, text='brush', command=self.use_brush)
            self.brush_button.grid(row=0, column=1)

            self.color_button = Button(self.frame44, text='color', command=self.choose_color)
            self.color_button.grid(row=0, column=2)

            self.eraser_button = Button(self.frame44, text='eraser', command=self.use_eraser)
            self.eraser_button.grid(row=0, column=3)

            self.choose_size_button = Scale(self.frame44, from_=1, to=10, orient=HORIZONTAL)
            self.choose_size_button.grid(row=0, column=4)

            self.c = Canvas(self.frame44, bg='white', width=600, height=600)
            self.c.grid(row=1, columnspan=5)

            self.setup()
            self.frame44.mainloop()

        def setup(self):
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)

        def use_pen(self):
            self.activate_button(self.pen_button)

        def use_brush(self):
            self.activate_button(self.brush_button)

        def choose_color(self):
            self.eraser_on = False
            self.color = askcolor(color=self.color)[1]

        def use_eraser(self):
            self.activate_button(self.eraser_button, eraser_mode=True)

        def activate_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=RAISED)
            some_button.config(relief=SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode

        def paint(self, event):
            self.line_width = self.choose_size_button.get()
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                width=self.line_width, fill=paint_color,
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.old_x = event.x
            self.old_y = event.y

        def reset(self, event):
            self.old_x, self.old_y = None, None


    if __name__ == '__main__':
        Paint()



def DEVELOPER():
    hide_prev_frames()
    msg.showinfo(" ","D SRI OME HOTHA")
    list=["pursuing civil engineer"]
    for items in list:
        msg.showinfo(" ",items)
    
    

    dsoh=Label(frame55,text="D SRI OME HOTHA",bg="black",fg="white",font="bold")
    dsoh.pack(expand=True)
    list=["pursuing civil engineer"]
    for items in list:
        Label(frame55,text=items,bg="black",fg="white",font="bold").pack()
    frame55.pack(  )

def google():
    hide_prev_frames()
    msg.showinfo("tip","search what you want")
    gframe.load_website("google.com")
    gframe.pack(fill="both", expand=True)



def dictionaryfun():
    hide_prev_frames()
    msg.showinfo("TIP","search the meaning of the words")    
     
 
    def dict():
        meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
  
    
    Label(dframe, text="type and find", font=("Aerial", 18)).pack()
    meaning = Label(dframe, text="", font=("Poppins",15), width= 100 )
    meaning.pack(expand=TRUE)
    dframe.pack()

    word = Entry(dframe, font=("Times New Roman", 15))
    word.pack()
    dframe.pack()
 
    Button(dframe, text="Find", font=("Poppins bold",15),command=dict,bg="green",fg="yellow").pack(side=LEFT)

my_menu=Menu(root)
root.config(menu=my_menu)

 
sound_menu=Menu(my_menu)
my_menu.add_cascade(label="sounds",menu=sound_menu)
sound_menu.add_command(label="sound",command=sound)
 
words_menu=Menu(my_menu)
my_menu.add_cascade(label="words",menu=words_menu)
words_menu.add_command(label="words",command=words)

images_menu=Menu(my_menu)
my_menu.add_cascade(label="images",menu=images_menu)
images_menu.add_command(label="images",command=image) 

slate_menu=Menu(my_menu)
my_menu.add_cascade(label="slate",menu=slate_menu)
slate_menu.add_command(label="slate",command=slate)

google_menu=Menu(my_menu)
my_menu.add_cascade(label="google.com",menu=google_menu)
google_menu.add_command(label="google.com",command=google)

dictionary_menu=Menu(my_menu)
my_menu.add_cascade(label="dictionary",menu=dictionary_menu)
dictionary_menu.add_command(label="dictionary",command=dictionaryfun)

how_to_menu=Menu(my_menu)
my_menu.add_cascade(label="how to",menu=how_to_menu)
how_to_menu.add_command(label="how to",command=howto)

DEVELOPER_menu=Menu(my_menu)
my_menu.add_cascade(label="DEVELOPER",menu=DEVELOPER_menu)
DEVELOPER_menu.add_command(label="DEVELOPER",command=DEVELOPER)

quit_menu=Menu(my_menu,bg="#FF0000",fg="white")
my_menu.add_cascade(label="quit",menu=quit_menu)
quit_menu.add_command(label="quit",command=quit)

root.mainloop()
