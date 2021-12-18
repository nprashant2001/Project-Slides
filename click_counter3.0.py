from tkinter import *
from PIL import Image

im = Image.open('test.jpg') #sample jpg file

w, h = im.size
print('width: ', w) #test
print('height:', h) #test

class clickCount:
   
    def clicks(self,event):
        #clicks = 0
        global count
        count += 1
        return count
    
    def main(self, w, h):
        root = Tk()
        root.minsize(w, h)
        root.attributes('-alpha', 0.5)
        root.bind("<Button-1>", self.clicks)
        root.mainloop()
        return count

count = 0 
total = clickCount()
print(total.main(w, h))
