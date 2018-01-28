# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:31:09 2018

@author: yatli

Interfaces of GraphEngine Module.
This file would be inplaced by the one generated by SWIG.
"""


class Cell:
    
    def __init__(self):
        pass
    
    def GetField(self, name):
        pass
    
    def SetField(self, name, value):
        pass
    
    def RemoveField(self, name):
        pass
    
    def HasField(self, name):
        pass
    
    def AppendField(self, name, value):
        pass
        
    
    @property
    def ID(self) -> int:
        pass




def NewCell(cell_type: str):
    pass

def NewCell2(cell_type: str, cell_id: int):
    pass

def NewCell3(cell_type: str, content: str):
    pass


def LoadCell(cell_type: str) -> Cell:
    pass