import pandas as pd
from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Árlista információk")
        self.pack(fill=BOTH, expand=1)

        kilepoGomb = Button(self, text="Kilépés",command=self.client_exit)
        beolvasoGomb = Button(self, text="Beolvasás",command=self.beolvas)

        Label(self, text="Kérem a cikkszámot!").place(x=20, y=20)
        global cikkszambeolvasas
        cikkszambeolvasas = Entry(self)
        cikkszambeolvasas.place(x=20, y=50)

        Label(self, text="Kérem az excel file nevét!").place(x=20, y=80)
        global excel_filenev_beolvasas
        excel_filenev_beolvasas = Entry(self)
        excel_filenev_beolvasas.place(x=20, y=100)

        kilepoGomb.place(x=20, y=460)
        beolvasoGomb.place(x=20, y=130)
 
    def client_exit(self):
        exit()

    def beolvas(self):
        df=pd.read_excel('{}'.format(excel_filenev_beolvasas.get()))
        df2=df.set_index('Cikkszám')
        
        gorgo = Scrollbar(self)
        szoveg = Text(self, height=4, width=75)
        gorgo.pack(side=RIGHT, fill=Y)
        szoveg.pack(side=RIGHT, fill=Y)
        gorgo.config(command=szoveg.yview)
        szoveg.config(yscrollcommand=gorgo.set)
        cikkszaminfo = df2.ix[int(cikkszambeolvasas.get())]
        szoveg.insert(END, cikkszaminfo)
        #print(df2.ix[int(cikkszambeolvasas.get())])
       
root = Tk()
root.geometry("900x500")
app = Window(root)
root.mainloop()  
