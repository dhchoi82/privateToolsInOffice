#!/usr/bin/python3

from controlDB import initDB
from manageSort import MainFrame as MngSort
from manageSource import MainFrame as AddSource
from tkinter import Tk, Toplevel, Frame, Entry, Button, Text, StringVar, BOTH
from tkinter.ttk import Combobox

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("자료 정리")
        InputData(self).pack(fill=BOTH)

class InputData(Frame):
    def __init__(self, parent):
        super().__init__()
        
        self.searchText = StringVar()
        
        Combobox(self, values=self.getSorts()).grid(column=0,row=0, sticky="nesw")
        Button(self, text="구분 수정", command=self.mngSort).grid(column=1,row=0)
        sourceEntry = Entry(self, textvariable=self.searchText)
        sourceEntry.grid(column=2,row=0, sticky="nesw")
        sourceEntry.bind("<Return>",self.searchSource)
        Button(self, text="출처 추가", command=self.addSource).grid(column=3,row=0)
        Button(self, text="자료 저장", command=self.submit).grid(column=3, row=2)
        Text(self).grid(column=0,row=1, columnspan=4)
    
    def mngSort(self):
        subWin = Toplevel(self)
        MngSort(subWin).pack(fill=BOTH)
    
    def addSource(self):
        subWin = Toplevel(self)
        AddSource(subWin).pack(fill=BOTH)
    
    def getSorts(self):
        # 현재 저장되어 있는 자료 구분의 튜플을 반환
        return ("a","b","c")
    
    def searchSource(self,*arg):
        # 검색어를 포함한 자료 목록 보여주는 창 띄움
        # 선택된 자료 출처를 표시
        print(self.searchText.get())
    
    def submit(self):
        # 저장된 값 확인 창 띄움
        # 구분과 출처는 해당 no 의 값을 저장
        # 저장 후 입력창 비움
        pass

if __name__ == "__main__":
    initDB()
    
    root = MainWindow()

    root.mainloop()
