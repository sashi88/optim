'''
Created on Jul 11, 2013

@author: sashika
'''
  
from Tkinter import *
from ttk import *
import optimizationLogic 
import tkMessageBox

class Example(Frame):
   
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
    
        
    def initUI(self):
    
        self.parent.title("Water Outflow Optimization Model")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
  
        self.rowconfigure(0, pad=15)
        self.rowconfigure(4, pad=25)
        
        lbl = Label(self, text="Please Enter Reservoir Water Capacity")
        lbl.grid(row=0,sticky=W, pady=4, padx=5, column=1)

        lbl1 = Label(self, text="Excess Water Amount \n of Nachchaduwa Reservoir")
        lbl1.grid(row=1, column=0, sticky=W+E, pady=4, padx=5)
        entry1 = Entry(self)
        entry1.grid(row=1, column=1, padx=5, sticky=W)       #sticky=E+W+S+N
        entry1.insert(0, 0) 
        
        lbl2 = Label(self, text="Remaining Water Capacity \n Nuwara Weva")
        lbl2.grid(row=2, column=0, sticky=W+E, pady=4, padx=5)
        entry2 = Entry(self)
        entry2.grid(row=2, column=1, padx=5, sticky=W)
        entry2.insert(0, 0)
        
        lbl3 = Label(self,text="Please Enter Canal Threshold Values \n Otherwise It Will Use Default Values")
        lbl3.grid(row=3, column=1,sticky=W+E, pady=4, padx=5)
        
        lbl4 = Label(self, text="Nuwara Weva Low Level \n Feeder Canal Capacity")
        lbl4.grid(row=4, column=0, sticky=W+E, pady=4, padx=5)
        entry4 = Entry(self)
        entry4.grid(row=4, column=1, padx=5, sticky=W)
        entry4.insert(0, 15000)
        
        lbl5 = Label(self, text="Nuwara Weva Higher Level \n Feeder Canal Capacity")
        lbl5.grid(row=5, column=0, sticky=W+E, pady=4, padx=5)
        entry5 = Entry(self)
        entry5.grid(row=5, column=1, padx=5, sticky=W)
        entry5.insert(0, 20000)
        
        lbl6 = Label(self, text="Malwathu Oya Capacity")
        lbl6.grid(row=6, column=0, sticky=W+E, pady=4, padx=5)
        entry6 = Entry(self)
        entry6.grid(row=6, column=1, padx=5, sticky=W)
        entry6.insert(0, 40000)
        
        lbl7 = Label(self, text="Special Water Releasing \n Canal Capacity")
        lbl7.grid(row=7, column=0, sticky=W+E, pady=4, padx=5) 
        entry7 = Entry(self)
        entry7.grid(row=7, column=1, padx=5, sticky=W)
        entry7.insert(0, 0)
        
        cbtn = Button(self, text="Cancel")
        cbtn.grid(row=15, column=0, sticky=W)
        
        def okClick():
            # convert string into int, reservoir capacity
            excessNachwa=int (entry1.get())
            capacityNW=int (entry2.get())
            # convert string into int, Canals capacity
            NW_LowLevel=int(entry4.get())
            NW_HigherLevel=int(entry5.get())
            MalwathuOya=int(entry6.get())
            SpecialCanal=int(entry7.get())
            
            if excessNachwa!=0 :
                optimizationLogic.optimLogic(excessNachwa,capacityNW,NW_LowLevel,NW_HigherLevel,MalwathuOya,SpecialCanal)
            else:    
                tkMessageBox.showinfo("Warning", "Please give the excess water amount in Nachchaduwa Reservoir")
            #return exWater, nuwaraWater, cannalA
            #print exWater, nuwaraWater, cannalA   
        
        obtn = Button(self, text="OK", command=okClick)
        obtn.grid(row=15, column=1,padx=5, sticky=W)               
        
def main():
  
    root = Tk()
    root.geometry("500x500+300+100")
    app = Example(root)
    root.mainloop()  
    

if __name__ == '__main__':
    main()  
    
