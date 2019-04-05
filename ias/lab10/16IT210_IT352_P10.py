# import tkinter module 
from tkinter import *
from tkinter import messagebox
# import other necessery modules 
import random 
import time 
import datetime 
import blind , cyclic , choosen
# creating root object 
root = Tk() 
  
# defining size of window 
root.geometry("1500x7000") 

#BackGround
# root.configure(background='black')
# setting up the title of window 
root.title("RSA") 
  
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 
  
f1 = Frame(root, width = 800, height = 700, 
                            relief = SUNKEN) 
f1.pack(side = LEFT) 
  
# ============================================== 
#                  TIME 
# ============================================== 
localtime = time.asctime(time.localtime(time.time())) 
  
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), 
          text = "RSA \n", 
                     fg = "brown", bd = 10, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0) 
  
lblInfo = Label(Tops, font=('arial', 20, 'bold'), 
             text = localtime, fg = "orange", 
                           bd = 10, anchor = 'w') 
                          
lblInfo.grid(row = 1, column = 0) 

#Global Variables 
p = StringVar() 
q = StringVar()
Msg = StringVar() 
e = StringVar() 
r = StringVar()
mode = StringVar() 
Result = StringVar() 
  
# exit function 
def qExit(): 
    root.destroy() 

def input_error():
    # root.destroy()
    messagebox.showerror("Error","Wrong Input")

# Function to reset the window 
def Reset(): 
    p.set("")
    q.set("") 
    Msg.set("") 
    e.set("") 
    r.set("")
    mode.set("") 
    Result.set("") 
  
  
# reference 
lblReference = Label(f1, font = ('arial', 16, 'bold'), 
                text = "P:", bd = 16, anchor = "w") 
                  
lblReference.grid(row = 0, column = 0) 
  
txtReference = Entry(f1, font = ('arial', 16, 'bold'), 
               textvariable = p, bd = 5, insertwidth = 4, 
                        bg = "powder blue", justify = 'right') 
                          
txtReference.grid(row = 0, column = 1) 

#Q
lblQ = Label(f1, font = ('arial', 16, 'bold'), 
                text = "Q:", bd = 16, anchor = "w") 
                  
lblQ.grid(row = 1, column = 0) 
  
txtQ = Entry(f1, font = ('arial', 16, 'bold'), 
               textvariable = q, bd = 5, insertwidth = 4, 
                        bg = "powder blue", justify = 'right') 
                          
txtQ.grid(row = 1, column = 1) 
  
# labels 
lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
         text = "Cipher: ", bd = 16, anchor = "w") 
           
lblMsg.grid(row = 2, column = 0) 
  
txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = Msg, bd = 5, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtMsg.grid(row = 2, column = 1) 
  
lblkey = Label(f1, font = ('arial', 16, 'bold'), 
            text = "e", bd = 16, anchor = "w") 
              
lblkey.grid(row = 3, column = 0) 
  
txtkey = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = e, bd = 5, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtkey.grid(row = 3, column = 1) 

#R
lblR = Label(f1, font = ('arial', 16, 'bold'), 
            text = "r", bd = 16, anchor = "w") 
              
lblR.grid(row = 4, column = 0) 
  
txtR = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = r, bd = 5, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtR.grid(row = 4, column = 1) 

  
lblmode = Label(f1, font = ('arial', 16, 'bold'), 
          text = "MODE(b for blind, c for cyclic,cc for choosen cipher)", 
                                bd = 16, anchor = "w") 
                                  
lblmode.grid(row = 5, column = 0) 
  
txtmode = Entry(f1, font = ('arial', 16, 'bold'), 
          textvariable = mode, bd = 5, insertwidth = 4, 
                  bg = "powder blue", justify = 'right') 
                    
txtmode.grid(row = 5, column = 1) 
  
lblService = Label(f1, font = ('arial', 16, 'bold'), 
             text = "Output:-", bd = 16, anchor = "w") 
               
lblService.grid(row = 2, column = 2) 
  
txtService = Entry(f1, font = ('arial', 16, 'bold'),  
             textvariable = Result, bd = 5, insertwidth = 4, 
                       bg = "powder blue", justify = 'right') 
                         
txtService.grid(row = 2, column = 3)   
  
def Ref(): 
    print("Message= ", (Msg.get())) 
  
    Message = Msg.get() 
    P = p.get() 
    Q = q.get()
    R = r.get()
    E = e.get()
    m = mode.get() 
    # Empty Field
    if P=="" or E=="" or m=="" or Q=="":
        input_error()
        pass
        # error()
    # Blind Signature Attack
    if (m == 'b'): 
        if R=="":
            input_error()
        ans = blind.main(int(P),int(Q),int(R),int(E),Message)
        if ans!=-1:
            Result.set(ans) 
        if ans == -1:
            root.destroy()
            messagebox.showerror('Error','No d value possible')
        elif ans == -2:
            root.destroy()
            messagebox.showerror('Error','No r value possible')
        elif ans == -3:
            root.destroy()
            messagebox.showerror('Error','E & Phi are not co-prime')

    # Cuclic ATtack
    elif m=='c':
        if Message.isdigit!=True:
            # error
            pass 
        ans = cyclic.main(int(P),int(Q),int(E),int(Message))
        if ans!=-1:
            Result.set(ans)
        if ans==-1:
            messagebox.showerror('Error','Incoorect P , Q')
        elif ans == -2:
            messagebox.showerror('Error','E & Phi are not co-prime')
            root.destroy()

        pass
    # CHoosen Cipher 
    elif m=='cc':
        if R=="":
            input_error()
        ans = choosen.main(int(P),int(Q),int(R),int(E),Message)
        if ans!=-1:
            Result.set(ans)
        if ans == -1:
            root.destroy()
            messagebox.showerror('Error','No d value possible')
        elif ans == -2:
            root.destroy()
            messagebox.showerror('Error','No r value possible')
        elif ans == -3:
            root.destroy()
            messagebox.showerror('Error','E & Phi are not co-prime')



  
# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "Show Message", bg = "powder blue", 
                         command = Ref).grid(row = 7, column = 1) 
  
# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                  fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "green", 
                   command = Reset).grid(row = 7, column = 2) 
  
# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 10, text = "Exit", bg = "red", 
                  command = qExit).grid(row = 7, column = 3) 
  
# keeps window alive 
root.mainloop() 