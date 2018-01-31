#!/usr/bin/python3

import os
from tkinter import Tk, Frame, Label, Text, Entry, Button, StringVar, messagebox, filedialog, END

class GuiBackupSet(Frame):
    def __init__(self, tkmaster=None):
        super().__init__(master=tkmaster, padx=10, pady=10)
        
        self.originPath = StringVar()
        self.copyPath = StringVar()
        self.runStringInit = 'xcopy /y/e/h/r/k/d "{}" "{}"'
        self.runString = StringVar(value=self.runStringInit)
        
        Button(self, text='원본 설정', command=self.setOrigin).grid(row=0,column=0,padx=5,pady=5)
        Button(self, text='백업본 설정', command=self.setCopy).grid(row=0,column=1,padx=5,pady=5)
        Button(self, text='백업 실행', command=self.runBackup).grid(row=0,column=2,padx=5,pady=5)
        self.runCmdLabel = Text(self, height=5, width=30)
        self.runCmdLabel.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
    
    def setOrigin(self):
        self.originPath.set(filedialog.askdirectory())
        self.setRunString()
    
    def setCopy(self):
        self.copyPath.set(filedialog.askdirectory())
        self.setRunString()
    
    def setRunString(self):
        text = self.runStringInit.format(self.originPath.get(),self.copyPath.get())
        self.runString.set(text)
        self.runCmdLabel.delete(1.0,END)
        self.runCmdLabel.insert(1.0,self.runString.get())
    
    def runBackup(self):
        answer = messagebox.askyesno(message='xcopy를 실행하시겠습니까?')
        if answer == True:
            os.system(self.runString.get())

if __name__ == '__main__':
    root = Tk()
    root.title('xcopy 백업')
    GuiBackupSet(root).pack()
    root.mainloop()
