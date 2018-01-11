#!/usr/bin/python3

from tkinter import Tk, Frame, StringVar, Entry, Label, Button, messagebox, LEFT
import sqlite3

class MainFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        textEntry = EntryLine(self,self.con)
        textEntry.pack()
        parent.bind("<Return>",textEntry.runInput)
        self.getLines()
    
    def __del__(self):
        self.con.close()
    
    def getLines(self):
        sql = "SELECT no, field FROM sorts"
        for (no, sort) in self.cur.execute(sql):
            SortLine(self,sort,no,self.con).pack()

class EntryLine(Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        
        self.parent = parent
        self.inputText = StringVar()
        self.con = con
        self.cur = con.cursor()
        
        textEntry = Entry(self, textvariable=self.inputText) # 새 항목 입력 칸
        textEntry.pack(side=LEFT)
        textEntry.focus_set()
        self.button = Button(self, text="확인", command=self.runInput) # 새 항목 입력 확인 단추
        self.button.pack(side=LEFT)
        
    def runInput(self, *args):
        sortText = self.inputText.get()
        
        sql = "SELECT count(no) FROM sorts WHERE field=?"
        self.cur.execute(sql,(sortText,))
        
        if self.cur.fetchone()[0] == 0:
            sql = "INSERT INTO sorts(field) VALUES (?)"
            self.cur.execute(sql,(sortText,))
            self.con.commit()
            SortLine(self.parent,sortText,self.cur.lastrowid,self.con).pack()
        else:
            messagebox.showinfo(message='해당 항목이 이미 존재합니다.')

class SortLine(Frame):
    def __init__(self, parent, labelText, lineNum, con):
        super().__init__(parent)
        
        Label(self, text=labelText).pack(side=LEFT)
        Button(self, text="x", command=self.delLine).pack(side=LEFT)
        
        self.lineNum = lineNum
        self.con = con
        self.cur = con.cursor()
    
    def delLine(self):
        sql = "DELETE FROM sorts WHERE no=?"
        self.cur.execute(sql,(self.lineNum,))
        self.con.commit()
        self.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("자료 구분 설정")
    MainFrame(root).pack()
    root.mainloop()
