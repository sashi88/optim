from Tkinter import *
from ttk import *
import pylab as p


globx1 =0.0
globx2 =0.0
globx3 =0.0
globx4 =0.0
globObj =0.0
def viewOutput(A,B,C,D,O):
    print "*************Got the call"
    global globx1
    global globx2
    global globx3
    global globx4
    global globObj
    globx1 = A
    globx2 = B
    globx3 = C
    globx4 = D 
    globObj = O
    
    root = Tk()
    root.geometry("400x400+300+100")
    app = resultUi(root)
    root.mainloop()
    

class resultUi(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)    
        self.parent = parent
        self.initUI()
    
    def initUI(self): 
        self.parent.title("Water Outflow Optimization Result")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(4, pad=25)
        
        lbl = Label(self, text="Water Releasing out-put")
        lbl.grid(row=0,sticky=W, pady=4, padx=5, column=1)

        lbl1 = Label(self, text="Water Amount in MalwathuOya")
        lbl1.grid(row=1, column=0, sticky=W+E, pady=4, padx=5)
        
        entry1 = Entry(self)
        entry1.grid(row=1, column=1, padx=5, sticky=W)
        print "!!!!!!!!!!!!!!!"
        print globx1
        entry1.insert(0, globx1)
        entry1.configure(state='disabled')
        
        lbl2 = Label(self, text="Water Amount in SpecialCanal")
        lbl2.grid(row=2, column=0, sticky=W+E, pady=4, padx=5)
        
        entry2 = Entry(self)
        entry2.grid(row=2, column=1, padx=5, sticky=W)
        entry2.insert(0, globx2)
        entry2.configure(state='disabled')
        
        lbl3 = Label(self, text="Water Amount in NW_HigherLevel")
        lbl3.grid(row=3, column=0, sticky=W+E, pady=4, padx=5)
        
        entry3 = Entry(self)
        entry3.grid(row=3, column=1, padx=5, sticky=W)
        entry3.insert(0, globx3)
        entry3.configure(state='disabled')

        lbl4 = Label(self, text="Water Amount in NW_LowLevel")
        lbl4.grid(row=4, column=0, sticky=W+E, pady=4, padx=5)
        
        entry4 = Entry(self)
        entry4.grid(row=4, column=1, padx=5, sticky=W)
        entry4.insert(0, globx4)
        entry4.configure(state='disabled')
        
        def OKclick():
            #self.root.destroy()
            fig = p.figure()
            ax = fig.add_subplot(1,2,1)
            
            y = [globx1,globx2,globx3,globx4]
            # Calculate how many bars there will be
            N = len(y)
            ind = range(N)
            ax.bar(ind, y, facecolor='blue', align='center', ecolor='blue')
            
            #Create a y label
            ax.set_ylabel('Water Amount in m3')
            # Create a title, in italics
            ax.set_title('Outflow Water Releasing - Nachchaduwa Reservoir',fontstyle='italic')
            # This sets the ticks on the x axis to be exactly where we put
            # the center of the bars.
            ax.set_xticks(ind)
            # Labels for the ticks on the x axis.  It needs to be the same length
            # as y (one label for each bar)
            group_labels = ['MalwathuOya', 'SpecialCanal','NW_HigherLevel', 'NW_LowLevel']
            # Set the x tick labels to the group_labels defined above.
            ax.set_xticklabels(group_labels)
            fig.autofmt_xdate()
            #ax.bar(x,y)
            p.show()
   
        obtn = Button(self, text="OK", command=OKclick)
        obtn.grid(row=15, column=1,padx=5, sticky=W)
    
        

     
    
    
    
    