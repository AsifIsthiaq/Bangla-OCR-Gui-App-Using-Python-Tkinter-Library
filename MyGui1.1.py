"""
@author: Asif
"""
####################### IMPORTING LIABRARIES ##################################
from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory
from PIL import  Image
import FeatureExtraction as fe
import BuiltInMLP as bim
class GUI(Frame): #GUI is a SubCLass of Frame

    def __init__(self,master=None):
        #Calling Constructor of ParentCLass
        Frame.__init__(self,master)
        #Initializing Tkinter Window 
        #w,h = 250,250
        #master.minsize(width=w, height=h)
        #master.maxsize(width=w, height=h)
        master.title("OCR")
        master.configure(background="#012b49")
        self.configure(background="#012b49")
        self.pack() #combine all the widget in blocks then place it on the parent widget
        
        #Serial Maintain kora Lagbe or pack() ta thikvabe call deyalagbe
        #Label Choose
        #self.choose = Label(self, text="Choose Character Image",bg="#bcd5ff",foreground="green",font=("Arial", 12)).pack()
        self.choose = Label(self,text="Choose Character Image",bg="#012b49",foreground="#68bdf9",font = "Arial 13 bold")
        self.choose.pack(padx=10,pady=10) #fill=x,side=LEFT
        #Button Browse #Helvetica
        self.file = Button(self,text='Browse',bg="PeachPuff",foreground="#012b49",font=("Arial", 10,"bold"), command=self.OpenFile)
        self.file.pack(anchor=CENTER,pady=3)
        #For Showing image on a label
        self.image = PhotoImage(file='empty.PNG')
        self.label = Label(image=self.image,compound="bottom",text="Choosed Character Image",bg="#00406d",foreground="#68bdf9",font=("Arial", 12,"italic"))
        self.label.pack(anchor=S,padx=10,pady=10)
        #Label Which Char Is Selected
        self.operation_action_text = StringVar()
        self.operation_action_text.set("                                           ")
        self.operation_action = Label(self, textvariable=self.operation_action_text,foreground="#FFFFFF",bg="#000000",font=("Arial", 15,"bold"))
        self.operation_action.pack(padx=10,pady=12)
        #Menu Bar
        self.menu = Menu(self)
        self.master.config(menu = self.menu)        
        self.select = Menu(self.menu)
        self.menu.add_cascade(label = 'File', menu = self.select)
        self.select.add_command(label="Open",command=self.OpenFile)
        self.select.add_command(label = 'Exit', command = self.onExit)
        
        self.path=""
        self.predictedChar=""
        
        #Button Extract Feature
        self.ef = Button(self, text='Extract Feature',bg="PeachPuff",foreground="#012b49",font=("Arial", 10,"bold"), command=self.FEbtnClicked)
        self.ef.pack(padx=10,pady=10)
        
        #Text Box For Entry of No of Neuron
        self.L1 = Label(self,text="Enter The No. Of Neuron In Hidden Layer",bg="#012b49",foreground="#68bdf9",font = "Arial 10 bold")
        self.L1.pack(padx=10,pady=0) 
        self.E1 = Entry(self, bd =7,bg="#012b49",foreground="#68bdf9")
        self.E1.pack(pady=16)
        
        #Button Train and Testing
        self.ef = Button(self, text='Train & Test',bg="PeachPuff",foreground="#012b49",font=("Arial", 10,"bold"), command=self.TTbtnClicked)
        self.ef.pack(padx=10,pady=0)
        
    def TTbtnClicked(self):
        y=[0]
        noOfNeuronstr = self.E1.get()
        print("Print Neuron Str : " + noOfNeuronstr)
        predchar=bim.BIMLP(noOfNeuronstr)
        print("Predicted Char",predchar[0])
        self.predictedChar="Predicted Character Is : "+self.NumToChar(predchar[0])
        print(self.predictedChar)
        self.operation_action_text.set(self.predictedChar)
        self.master.update_idletasks()
        noOfNeuronstr = self.E1.delete(0,len(noOfNeuronstr))
    
    def NumToChar(self,x):
        if x==1:
            return "অ "
        elif x==2:
            return "আ "
        elif x==3:
            return "ই " 
        elif x==4:
            return "ঈ "
        elif x==5:
            return "উ "
        elif x==6:
            return "ঊ "
        elif x==7:
            return "এ "
        elif x==8:
            return "ঐ "
        elif x==9:
            return "ও "
        elif x==10:
            return "ঔ "
        elif x==11:
            return "ঋ "
        else:
            return ":'("
        
    def FEbtnClicked(self):
        print("Path : "+self.path)
        fe.DatasetForTesting(self.path)
        charstr="Feat. Extraction Complete."
        self.operation_action_text.set(charstr)
        self.master.update_idletasks()
    
    def OpenFile(self):
        '''
        name = askopenfilename(initialdir="F:\Recovery After Formatting\Thesis\Main\Python Code Thesis\Starting 1\Data2/",
                           filetypes =(("Image File", "*.PNG"),("All Files","*.*")),
                           title = "Choose a file."
                           )
        '''
        name = askopenfilename(initialdir="F:\Recovery After Formatting\Thesis\Main\Python Code Thesis\Gui\Testing Char Image/",
                           filetypes =(("Image File", "*.PNG"),("All Files","*.*")),
                           title = "Choose a file."
                           )
        '''
        name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Image File", "*.PNG"),("All Files","*.*")),
                           title = "Choose a file."
                           )
        '''
        print (name)
        self.path = name
        #Updating image label with the char image
        self.image2 = PhotoImage(file=self.path)
        self.label.configure(image=self.image2)
        self.label.image=self.image2
        #Updating Label with selected char name        
        namearr = name.split('/')
        s1=namearr[len(namearr)-1] 
        s2=s1.split('.')
        #charstr="Selected Char Image Is "+s2[len(s2)-2]
        charstr="                                           "
        print(charstr)        
        self.operation_action_text.set(charstr)
        self.master.update_idletasks()
              
    def onExit(self):
        self.destroy()


root = Tk()
app = GUI(master=root)
app.mainloop()
#root.destroy()
