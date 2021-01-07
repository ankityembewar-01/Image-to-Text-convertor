#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import basic modules 
from tkinter import*
from tkinter import filedialog 
root = Tk()
root.geometry("750x480")
root.resizable(0,0)
root.title("Image_to_Text")
root.configure(background='maroon')
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#defining function:

def openfilename(): 
    filename = filedialog.askopenfilename(title ='Select Image') 
    return filename 


def read_it():
    img = cv2.imread(openfilename())
    word = pytesseract.image_to_string(img)
    tbox1.tag_configure("center", justify='center')
    tbox1.insert(END, word) 
    tbox1.tag_add("center", "1.0", "end")
    scrollbar = Scrollbar(root,orient=VERTICAL)
    scrollbar.place(x=713,y=100,height=257, width=20 )
    scrollbar.config( command = tbox1.yview)
    
def clearTextInput():
    tbox1.delete("1.0","end")


#front-end Design  

l1 = Label(root,text = "Image Convertor to Text",font=("Ink Free",30,"bold","underline"), fg="white", bg='maroon')
l1.place(x=135,y=20)

tbox1 = Text(root,height = 11, width = 68, font=("Times New Roman",15,"bold"),fg="black",relief = "solid")
tbox1.place(x=30, y=100)

btn_1 = Button(root, text ='Get Text',font=("Century Schoolbook",19,"bold"),bg="goldenrod2",fg="red",relief="raised",command = read_it)
btn_1.place(x = 100, y = 380 , width = 140)

btn_2 = Button(root, text="Clear", font=("Century Schoolbook",19,"bold"),bg="goldenrod2",fg="red",relief="raised", command=clearTextInput)
btn_2.place(x = 520, y = 380 , width = 120)

root.mainloop()


# In[ ]:





# In[ ]:




