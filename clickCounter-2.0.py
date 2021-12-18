from tkinter import *

class clickCount:
   
    def clicks(self,event):
        #clicks = 0
        global count
        count += 1
        return count
    
    def main(self, h, w):
        root = Tk()
        root.minsize(h,w)
        root.attributes('-alpha', 0.25)
        root.bind("<Button-1>", self.clicks)
        root.mainloop()
        return count

count = 0 
height, width = 700, 500 #sample window/image size
total = clickCount()
print(total.main(height, width))
