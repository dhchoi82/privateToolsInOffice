#!/usr/bin/python3

from tkinter import Tk, Frame, StringVar, Entry, Label, Message, Button, messagebox, LEFT, BOTH, RIGHT
import sqlite3

class MainFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        self.textEntry = EntryLine(self,self.con)
        self.textEntry.pack()
    
    def __del__(self):
        self.con.close()

class EntryLine(Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        
        self.parent = parent
        self.author = StringVar()
        self.year = StringVar()
        self.title = StringVar()
        self.publisher = StringVar()
        self.pages = StringVar()
        self.url = StringVar()
        self.etc = StringVar()
        self.con = con
        self.cur = con.cursor()
        
        line0 = Frame(self)
        line0.pack(fill=BOTH)
        Label(line0, text="저자:").pack(side=LEFT) # 저자
        authorEntry = Entry(line0, textvariable=self.author)
        authorEntry.pack(side=LEFT)
        authorEntry.focus_set()
        Label(line0, text="연도:").pack(side=LEFT) # 연도
        Entry(line0, textvariable=self.year).pack(side=LEFT)
        Label(line0, text="제목:").pack(side=LEFT) # 제목
        Entry(line0, textvariable=self.title).pack(side=LEFT)
        
        line1 = Frame(self)
        line1.pack(fill=BOTH)
        Label(line1, text="발행인/학술지:").pack(side=LEFT) # 발행인/학술지
        Entry(line1, textvariable=self.publisher).pack(side=LEFT)
        Label(line1, text="페이지:").pack(side=LEFT) # 페이지
        Entry(line1, textvariable=self.pages).pack(side=LEFT)
        
        line2 = Frame(self)
        line2.pack(fill=BOTH)
        Label(line2, text="URL:").pack(side=LEFT) # URL
        Entry(line2, textvariable=self.url).pack(side=LEFT)
        Label(line2, text="기타:").pack(side=LEFT) # 기타
        Entry(line2, textvariable=self.etc).pack(side=LEFT)
        Button(line2, text="확인", command=self.runInput).pack(side=RIGHT) # 새 항목 입력 확인 단추
    
    def runInput(self, *args):
        auth = self.author.get()
        year = self.year.get()
        titl = self.title.get()
        publ = self.publisher.get()
        page = self.pages.get()
        url = self.url.get()
        etc = self.etc.get()
        
        sql = "SELECT count(no) FROM sources WHERE author=? AND year=? AND title=? AND pages=? AND url=?"
        self.cur.execute(sql,(auth,year,titl,page,url))
        
        if self.cur.fetchone()[0] == 0:
            sql = "INSERT INTO sources(author,year,title,publisher,pages,url,etc) VALUES (?,?,?,?,?,?,?)"
            self.cur.execute(sql,(auth,year,titl,publ,page,url,etc))
            self.con.commit()
            SourceLine(self.parent,self.cur.lastrowid,self.con).pack()
        else:
            messagebox.showinfo(message='해당 항목이 이미 존재합니다.')

class SourceLine(Frame):
    def __init__(self, parent, lineNum, con):
        super().__init__(parent)
        
        self.lineNum = lineNum
        self.con = con
        self.cur = con.cursor()
        
        words = self.getWords()
        
        labelText = "저자: {}, 연도: {}, 제목: {}, 발행인/학술지: {}, 페이지: {}, URL: {}, 기타: {}".format(words[1],words[2],words[3],words[4],words[5],words[6],words[7])
        
        Message(self, text=labelText, width=600).pack(fill=BOTH)
        buttons = Frame(self)
        buttons.pack(fill=BOTH)
        Button(self, text="x", command=self.delLine).pack(side=RIGHT)
        #Button(self, text="수정", command=self.updateLine).pack(side=RIGHT)
    
    def delLine(self):
        sql = "DELETE FROM sources WHERE no=?"
        self.cur.execute(sql,(self.lineNum,))
        self.con.commit()
        self.destroy()
    
    def updateLine(self): #
        words = self.getWords()
    
    def getWords(self):
        sql = "SELECT * FROM sources WHERE no=?"
        self.cur.execute(sql,(self.lineNum,))
        return self.cur.fetchone()

if __name__ == "__main__":
    root = Tk()
    root.title("자료 출처 정리")
    MainFrame(root).pack()
    root.mainloop()
