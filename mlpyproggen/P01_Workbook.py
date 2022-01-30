# -*- coding: utf-8 -*-
#
#         Workbook
#
# * Version: 4.03
# * Author: Harold Linke
# * Date: January 8, 2022
# * Copyright: Harold Linke 2021
# *
# *
# * MobaLedCheckColors on Github: https://github.com/haroldlinke/MobaLedCheckColors
# *
# *  
# * https://github.com/Hardi-St/MobaLedLib
# *
# * MobaLedCheckColors is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# *
# * MobaLedCheckColors is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program.  if not, see <http://www.gnu.org/licenses/>.
# *
# *
# ***************************************************************************

#------------------------------------------------------------------------------
# CHANGELOG:
# 2021-12-23 v4.01 HL: - Inital Version converted by VB2PY based on MLL V3.1.0
# 2022-01-07 v4.02 HL: - Else:, ByRef check done - first PoC release
# 2022-01-08 V4.03 HL: - added Workbook Save and Load



from tkintertable import TableCanvas, TableModel
import tkinter as tk
from tkinter import ttk
from mlpyproggen.X01_Excel_Consts import *
from vb2py.vbconstants import *
from vb2py.vbfunctions import *
import time

#import mlpyproggen.M20_PageEvents_a_Functions as M20
import subprocess
import pickle
import mlpyproggen.Prog_Generator as PG
import mlpyproggen.F00_mainbuttons as F00

#import mlpyproggen.M01_Gen_Release_Version as M01
import keyboard
#import mlpyproggen.M25_Columns as M25
#import mlpyproggen.M02_global_variables as M02


def Date_str():
    return "01.01.2022"

def Time_str():
    return "12:00:00"

def Center_Form(form):
    return

def Shell(cmd):
    Run(cmd)

def updateWindow():
    PG.global_controller.update()

def TimeValue(Duration):
    return 5

def getvalue(row,column):
    value=ActiveSheet.tablemodel.getValueAt(row-1,column-1)
    #print("P01.getvalue:",row,column,value)
    
    return value

def ActiveCell():
    global Selection
    table = ActiveSheet.table
    row = table.getSelectedRow()+1
    col = table.getSelectedColumn()+1
    Selection = CSelection(ActiveSheet.Cells(row,col)) #*HL
    return ActiveSheet.Cells(row,col) #*HL

def set_activeworkbook(workbook):
    global ThisWorkbook,ActiveSheet,ActiveWorkbook
    ActiveWorkbook = Workbook = ThisWorkbook = workbook
    ActiveSheet = ActiveWorkbook.Sheets("DCC")
    PG.global_controller.activeworkbook = workbook
    
def create_workbook(frame=None, path=None,workbookName=None,workbookFilename=None):
    global ThisWorkbook,ActiveSheet,ActiveWorkbook
    workbook = ThisWorkbook = CWorkbook(frame=frame,path=path,workbookName=workbookName,workookFilename=workbookFilename)
    set_activeworkbook(workbook)
    return workbook
    
def IsError(testval):
    return False

def Cells(row:int, column:int):
    cell = ActiveSheet.Cells(row,column)
    return cell

def Range(cell1,cell2):
    return CRange(cell1,cell2)

def Sheets(sheetname):
    return ActiveWorkbook.Sheets(sheetname)

def Rows(row:int):
    sheet = ActiveSheet
    return sheet.MaxRange.Rows[row]
   
def Columns(col:int):
    sheet = ActiveSheet
    return sheet.MaxRange.Columns[col]

def IsEmpty(obj):
    if len(obj)==0:
        return True
    else:
        return False

def val(value):
    valtype=type(value)
    if valtype is CCell:
        cellvalue = value.get_value()
        if cellvalue != "":
            if IsNumeric(cellvalue):
                return int(cellvalue)
            else:
                return 0
        else:
            return 0
    elif valtype is str:
        if value != "":
            if IsNumeric(value):
                return int(value)
            else:
                return 0
        else:
            return 0
    return int(value)

def VarType(obj):
    valtype=type(obj)
    if valtype is str:
        return vbString
    else:
        return None
def Unload(UserForm):
    UserForm.destroy()

def ChDrive(srcdir):
    print("ChDrive:", srcdir)
    return

def Format(value,formatstring):
    if formatstring == "hh:mm:ss":
        time_sec = value%60
        value=int(value/60)
        time_min = value % 60
        value=int(value/60)
        time_h=value
        time_str = str(time_h)+":"+str(time_min)+":"+str(time_sec)
        return time_str
    elif formatstring == "0000":
        return "{0:4d}".format(value)
    elif formatstring == "00":
        return "{0:2d}".format(value)
    else:
        pass
    
    return str(value) # no formating implemented yet


def MsgBox(ErrorMessage:str, msg_type:int, ErrorTitle:str):
    if msg_type == vbQuestion + vbYesNoCancel:
        res=tk.messagebox.askyesnocancel(title=ErrorTitle, message=ErrorMessage)
        if res == None:
            return vbCancel
        if res:
            return vbYes
        else:
            return vbNo
    elif msg_type == vbOKCancel:
        res=tk.messagebox.askokcancel(title=ErrorTitle, message=ErrorMessage)
        if res == None:
            return vbCancel
        if res:
            return vbOK
        else:
            return vbCancel
    
    else:
        res=tk.messagebox.askyesnocancel(title=ErrorTitle, message=ErrorMessage)
        if res == None:
            return vbCancel
        if res:
            return vbYes
        
    return vbNo

def InputBox(Message:str, Title:str, Default=None):
    res = tk.simpledialog.askstring(Title,Message,initialvalue=Default)
    if res == None:
        res=""
    return res

def Time():
    return time.time()

def Run(cmd):
    subprocess.run(cmd,shell=True)
    
def set_statusmessage(message):
    PG.global_controller.set_statusmessage(message)
    PG.global_controller.update()

__VK_LBUTTON = 0x1
__VK_RBUTTON = 0x2
__VK_MBUTTON = 0x4
__VK_UP = 0x26
__VK_DOWN = 0x28
__VK_RETURN = 0xD
__VK_ESCAPE = 0x1B
__VK_CONTROL = 0x1C

def GetAsyncKeyState(key):
    if key==__VK_UP:
        return keyboard.is_pressed("up")
    if key==__VK_DOWN:
        return keyboard.is_pressed("down")
    if key==__VK_RETURN:
        return keyboard.is_pressed("enter")
    if key==__VK_ESCAPE:   
        return keyboard.is_pressed("escape")
    if key==__VK_CONTROL:   
        return keyboard.is_pressed("crtl")
    return


def GetCursorPos():
    pass

def SetCursorPos(x,y):
    pass

def DoEvents():
    pass

datasheet_fieldnames = "A;Aktiv;Filter;Adresse oder Name;Typ;Start-\nwert;Beschreibung;Verteiler-\nNummer;Stecker\nNummer;Icon;Name;Beleuchtung, Sound, oder andere Effekte;Start LedNr;LEDs;InCnt;Loc InCh;LED\nSound\nKanal;Comment"
datasheet_formating = { "HideCells" : ((0,"*"),(1,"*")),
                        "ProtectedCells"  : ((0,"*"),(1,"*"),("*",4),("*",12),("*",13),("*",14),("*",15),("*",16)),
                        "FontColor"       : { "1": {
                                                    "font"     : ("Arial",10),
                                                    "fg"       : "#FFFF00",
                                                    "bg"       : "#0000FF",
                                                    "Cells"    : ((0,"*"),(1,"*"))
                                                    },
                                              "2": {
                                                    "font"     : ("Wingdings",10),
                                                    "fg"       : "#000000",
                                                    "bg"       : "#FFFFFF",
                                                    "Cells"    : (("*",1),)
                                                    },                                                          
                                            "default": {
                                                   "font"     : ("Arial",10),
                                                   "fg"       : "#000000",
                                                   "bg"       : "#FFFFFF",
                                                   "Cells"    : (("*","*"),)
                                                   }
                                }
                    }
                        
sheetdict={"DCC":
            {"Name":"DCC",
             "Filename"  : "\\csv\\dcc.csv",
             "Fieldnames": datasheet_fieldnames,
             "Formating" : datasheet_formating,
             "SheetType" : "Datasheet"
             },
           "Selectrix":
            {"Name":"Selectrix",
             "Filename"  : "\\csv\\Selectrix.csv",
             "Fieldnames": "A;Aktiv;Filter;Channel oder\nName[0..99];Bitposition\n[1..8];Typ;Start-\nwert;Beschreibung;Verteiler-\nNummer;Stecker\nNummer;Icon;Name;Beleuchtung, Sound, oder andere Effekte;Start LedNr;LEDs;InCnt;Loc InCh;LED\nSound\nKanal;Comment",
             "Formating" : datasheet_formating,
             "SheetType" : "Datasheet"
             },
           "CAN":
            {"Name":"CAN",
             "Filename"  : "\\csv\\CAN.csv",
             "Fieldnames": datasheet_fieldnames,
             "Formating" : datasheet_formating,
             "SheetType" : "Datasheet"
             },
           "Examples":
            {"Name":"Examples",
             "Filename"  : "\\csv\\Examples.csv",
             "Fieldnames": datasheet_fieldnames,
             "Formating" : datasheet_formating,
             "SheetType" : "Datasheet"
             },                             
           "Config":
            {"Name":"Config",
             "Filename":"\\csv\\Config.csv",
             "Fieldnames": "A;B;C;D",
             "SheetType" : "Config",
             "Formating" : { "HideCells"       : (("*",3),),
                            "ProtectedCells"  : ( ("*",1),("*",3)),
                            "FontColor"       : { "1": {
                                                        "font"     : ("Arial",10),
                                                        "fg"       : "#0000FF",
                                                        "bg"       : "#FFFFFF",
                                                        "Cells"    : ((0,"*"),)
                                                        },
                                                "default": {
                                                       "font"     : ("Arial",10),
                                                       "fg"       : "#000000",
                                                       "bg"       : "#FFFFFF",
                                                       "Cells"    : (("*","*"),)
                                                       }
                                                }
                            }
            },
           "Languages":
            {"Name":"Languages",
             "Filename":"\\csv\\Languages.csv",
             "Fieldnames": "A;B;C;D;E;F;G;H;I"
            },
           "Lib_Macros":
            {"Name":"Lib_Macros",
             "Filename":"\\csv\\Lib_Macros.csv",
             "Fieldnames": "A;B;C;D;E;F;G;H;I;J;K;L;M;N;O;P;Q;R;S;T;U;V;W;X;Y;Z;AA;AB;AC;AD;AE;AF;AG;AH;AI;AJ;AK;AL;AM;AN;AO;AP;AQ;AR;AS"
            },
           "Libraries":
            {"Name":"Libraries",
             "Filename":"\\csv\\Libraries.csv",
             "Fieldnames": "A;B;C;D;E;F;G;H;I;J",
             "Formating" : {"ProtectedCells"  : ((0,"*"),(1,"*"),(2,"*"),(3,"*"),(4,"*"),(5,"*"),(6,"*"),(7,"*")),
                            "FontColor"       : { "1": {
                                                        "font"     : ("Arial",10),
                                                        "fg"       : "#FFFF00",
                                                        "bg"       : "#0000FF",
                                                        "Cells"    : ((6,"*"),)
                                                        },
                                                "default": {
                                                       "font"     : ("Arial",10),
                                                       "fg"       : "#000000",
                                                       "bg"       : "#FFFFFF",
                                                       "Cells"    : (("*","*"),)
                                                       }
                                                }
                            }
            },                   
           "Par_Description":
            {"Name":"Par_Description",
             "Filename":"\\csv\\Par_Description.csv",
              "Fieldnames": "A;B;C;D;E;F;G;H;I;J;K"
            },                  
           "Platform_Parameters":
            {"Name":"Platform_Parameters",
             "Filename":"\\csv\\Platform_Parameters.csv",
             "Fieldnames": "A;B;C;D;E"
            }
        }


class CWorkbook:
    def __init__(self, frame=None,path=None,workbookName=None, workookFilename=None):
        global Workbooks
        # Row and Columns are 0 based and not 1 based as in Excel

        if workbookName:
            self.Name = workbookName
        else:
            self.Name = "PyProgramWorkbook"
        Workbooks.append(self)
        if frame != None:
            self.Path = path
            self.master = frame
            self.tabframedict = {}
            
            style = ttk.Style(frame)
            style.configure('downtab.TNotebook', tabposition='sw')
            self.container = ttk.Notebook(frame, style="downtab.TNotebook")

            self.container.grid(row=0,column=0,columnspan=2,sticky="nesw")
            self.tabdict = dict()
            self.tabdict_frames = dict()
            self.sheets = list()
        
            for sheetname in sheetdict.keys():
                tabframe = ttk.Frame(self.container,relief="ridge", borderwidth=1)
                worksheet = self.new_sheet(sheetname,tabframe)
                tabframe.sheetname = sheetname
                tabframe.sheet = worksheet
                self.sheets.append(worksheet)
                self.container.add(tabframe, text=sheetname)
                self.tabframedict[sheetname]=worksheet
                if not self.showws and not PG.global_controller.show_pyPrgrammGenerator:
                    self.container.tab(tabframe,state="hidden")
                    
            self.container.bind("<<NotebookTabChanged>>",self.TabChanged)
               
        else:
            self.Path = path
            self.tablemodel= None
            self.sheets = None
            
    def new_sheet(self,sheetname,tabframe):
        sheetname_prop = sheetdict.get(sheetname)
        sheettype = sheetname_prop.get("SheetType","")
        callback = sheettype=="Datasheet"
        self.showws = sheettype in ["Datasheet","Config"]
        formating_dict = sheetname_prop.get("Formating",None)
        fieldnames = sheetname_prop.get("Fieldnames",None)
        if type(fieldnames) == str:
            fieldnames = fieldnames.split(";")
        worksheet = CWorksheet(sheetname,workbook=self, csv_filepathname=self.Path + sheetname_prop["Filename"],frame=tabframe,fieldnames=fieldnames,formating_dict=formating_dict,Sheettype=sheettype,callback=callback)
        return worksheet

            
    def TabChanged(self,_event=None):
        newtab_name = self.container.select()
        if newtab_name != "":
            newtab = self.container.nametowidget(newtab_name)
            sheet_name = newtab.sheetname
            sheet = newtab.sheet
            if sheet:
                sheet.Activate()
                print("Sheet activated:",sheet_name)
            
            #newtab.tabselected()
        #logging.debug("TabChanged %s - %s",self.oldTabName,newtab_name)        
        
    def Sheets(self,name):
        if self.sheets != None:
            for sheet in self.sheets:
                if sheet.Name == name:
                    return sheet
        return None
    
    def Worksheets(self,name):
        if self.sheets != None:
            for sheet in self.sheets:
                if sheet.Name == name:
                    return sheet
        return None
    
    def Activate(self):
        return
    
    def Save(self,filename=None):
        if filename == None:
            filename = tk.filedialog.asksaveasfilename(parent=self.master,
                                                        defaultextension='.table',
                                                        initialdir=os.getcwd(),
                                                        filetypes=[("pickle","*.table"),
                                                          ("All files","*.*")])
        if filename:
            self.SaveWorkbook(filename)
        return
    
    def Load(self,filename=None):
        """load from a file"""

        if filename == None:
            filename = tk.filedialog.askopenfilename(parent=self.master,
                                                      defaultextension='.table',
                                                      initialdir=os.getcwd(),
                                                      filetypes=[("pickle","*.table"),
                                                        ("All files","*.*")])
        if not os.path.exists(filename):
            print ('file does not exist')
            return
        if filename:
            self.LoadWorkbook(filename)
        return        
    
    def SaveWorkbook(self,filename):
        workbookdata = {}
        for sheet in self.sheets:
            sheetdata = sheet.getData()
            workbookdata[sheet.Name] = sheetdata
        
        fd = open(filename,'wb')
        pickle.dump(workbookdata,fd)
        fd.close()
        return
    
    def LoadWorkbook(self,filename):
        fd=open(filename,'rb')
        workbookdata = pickle.load(fd)
        
        for sheet in self.sheets:
            data = workbookdata.get(sheet.Name,{})
            sheet.setData(data)
            sheet.init_data()
            
        return        
        

class CWorksheet:
    def __init__(self,Name,tablemodel=None,workbook=None,csv_filepathname=None,frame=None,fieldnames=None,formating_dict=None,Sheettype="",callback=False):
        
        self.width = 1800
        self.height = 600
        self.Workbook = workbook
        self.ProtectContents = False
        self.Datasheet = Sheettype == "Datasheet"
        self.csv_filepathname = csv_filepathname
        self.fieldnames = fieldnames
        self.formating_dict = formating_dict
        self.Name = Name
        self.Shapes = CShapeList()
        if tablemodel:
            self.tablemodel = tablemodel
            self.table = TableCanvas(frame, model=tablemodel,width=self.width,height=self.height,scrollregion=(0,0,self.width,self.height))
        else:
            if csv_filepathname:
                self.tablemodel = TableModel()
                self.table = TableCanvas(frame, model=tablemodel,width=self.width,height=self.height,scrollregion=(0,0,self.width,self.height))
                self.table.importCSV(filename=self.csv_filepathname, sep=';',fieldnames=self.fieldnames)
                self.tablemodel = self.table.getModel()
                if callback:
                    self.table.set_left_click_callback(self.left_click_callback)
            else:
                return
        if self.formating_dict:
            self.tablemodel.nodisplay = self.formating_dict.get("HideCells",[])
            self.tablemodel.protected_cells = self.formating_dict.get("ProtectedCells",[])
            self.tablemodel.format_cells = self.formating_dict.get("FontColor",{})
        
        self.table.show()
        self.update_table_properties()        
        
    def init_data(self):
        F00.worksheet_init(self)

        
    def update_table_properties(self):
        self.LastUsedRow_val = self.tablemodel.getLastUsedRow()+1
        self.LastUsedColumn_val = self.tablemodel.getColumnCount()
        self.UsedRange_val = CRange((0,0) , (self.LastUsedRow_val,self.LastUsedColumn_val),ws=self)
        self.MaxRange_val  = CRange((0,0) , (self.LastUsedRow_val,self.LastUsedColumn_val),ws=self)
        self.Rectangles = CRectangles()
        self.AutoFilterMode = False
        self.searchcache = {}
        self.Shapes = CShapeList([])
        self.CellDict = CCellDict()
        self.End_val = self.LastUsedColumn_val        
        
    def left_click_callback(self,value1,value2,callertype="cell"):
        
        if callertype=="cell":
            row=value1
            col=value2
            print("Left_Click_Call_Back:",row,col)
            if col == 1:  # aktive column
                cell = self.Cells(row+1,col+1)
                if cell.Value == "":
                    cell.Value = chr(252)
                else:
                    cell.Value= ""
                self.Redraw_table()
                return False
            else:
                return True
        elif callertype=="canvas":
            print("Leftclick-Canvas",value1)
            #callingshape = self.Shapes.shapelist[int(value1[0])]
            Application.caller = int(value1[0])
            if Application.canvas_leftclickcmd!=None:
                Application.canvas_leftclickcmd()
                return False
        
    def EnableMousePosition(self):
        pass
        
    def addrow_after_current_row(self,copy=False):
        cur_row = self.table.getSelectedRow()
        num_rows = len(self.table.get_selectedRecordNames())
        if num_rows==0:
            num_rows = 1
        copyfromrow=None
        if copy:
            copyfromrow = cur_row
        self.table.addRows(num=num_rows,atrow=cur_row,copyfromrow=copyfromrow)
    
    def deleterows(self):
        self.table.deleteRow()
        
    def moveRows(self): #,sc_rowlist,destrow):
        self.table.Flag_move=True
        print("Move started")
        return
        
    def get_LastUsedRow(self):
        self.LastUsedRow_val = self.tablemodel.getLastUsedRow()+1 #self.tablemodel.getRowCount()
        return self.LastUsedRow_val
    
    def set_LastUsedRow(self,value):
        self.LastUsedRow_val = value
        self.tablemodel.setLastUsedRow(value-1)
    
    LastUsedRow = property(get_LastUsedRow, set_LastUsedRow, doc='Last used row')
    
    def get_LastUsedColumn(self):
        self.LastUsedColumn_val = self.tablemodel.getColumnCount()
        return self.LastUsedColumn_val
    
    def set_LastUsedColumn(self,value):
        self.LastUsedColumn_val= value
    
    LastUsedColumn = property(get_LastUsedColumn, set_LastUsedColumn, doc='Last used row')
    End = property(get_LastUsedColumn, set_LastUsedColumn, doc='Last used row')

    def get_UsedRange(self):
        self.UsedRange_val = CRange((0,0) , (self.get_LastUsedRow(),self.LastUsedColumn_val),ws=self)
        return self.UsedRange_val
    
    def set_UsedRange(self,value):
        self.UsedRange_val = value
               
    UsedRange = property(get_UsedRange, set_UsedRange, doc='used range')    
    MaxRange  = property(get_UsedRange, set_UsedRange, doc='used range')         
           
    def Cells(self,row, col):
        #print("Cells", self.Name, row, col)
        if row <=self.tablemodel.getRowCount() and col <=self.tablemodel.getColumnCount():
            cell = CCell(self.tablemodel.getCellRecord(row-1, col-1))
        else:
            cell=CCell("")
        cell.set_tablemodel(self.tablemodel)
        cell.set_row(row)
        cell.set_column(col)
        cell.set_parent(self)
        cell.set_sheet(self)
        return cell
    
    def Range(self,cell1,cell2):
        #print("Range,cell1,cell2,ws=self")
        return CRange((cell1.Row,cell1.Column),(cell2.Row,cell2.Column),ws=self)
        
        r=[]
        for row in range(cell1.Row,cell2.Row+1):
            for col in range(cell1.Column,cell2.Column+1):
                r.append(self.Cells(row, col))
        return r
    
    def Unprotect(self):
        self.ProtectContents = False
        
    def Protect(self, DrawingObjects=True, Contents=True, Scenarios=True, AllowFormattingCells=True, AllowInsertingHyperlinks=True):
        self.ProtectContents = True
        return
        
    def Columns(col:int):
        #print("Columns",col)
        return None
    
    def EnableDisableAllButtons(self,value):
        return
    
    def SetChangedCallback(self,callback):
        self.wschanged_callback = callback
        
    def SetSelectedCallback(self,callback):
        self.wsselected_callback = callback
        
    def EventWSchanged(self, changedcell):
        if self.wschanged_callback and Application.EnableEvents:
            self.wschanged_callback(changedcell)
            
    def EventWSselected(self, selectedcell):
        if self.wsselected_callback and Application.EnableEvents:
            self.wsselected_callback(selectedcell)
            
    def Redraw_table(self,do_bindings=False):
        self.table.redraw()
        if do_bindings:
            #print("Redraw_Table - do bindings")
            self.do_bindings()
        
    def set_value_in_cell(self,row,column,newval):
        cell = self.Cells(row, column)
        cell.Value=newval
        
        """
        colname = self.tablemodel.getColumnName(column-1)
        #coltype = tablemodel.columntypes[colname]
        name = self.tablemodel.getRecName(row-1)
        if colname in self.tablemodel.data[name]:
            if self.tablemodel.data[name][colname] != newval:
                self.tablemodel.data[name][colname] = newval
                if Application.EnableEvents:
                    print("Workbook contents changed")
                    ActiveSheet.EventWSchanged(self)
        """
        
    def create_search_colcache(self,searchcol):
        colcontent = self.tablemodel.getColCells(searchcol-1)
        row = 1
        self.searchcache[searchcol]={}
        searchcol_dict = self.searchcache[searchcol]
        for col in colcontent:
            searchcol_dict[col]=row
            row=row+1
        return
        
    def find_in_col_ret_col_val(self,searchtext, searchcol, resultcol,cache=True):
        
        if cache:
            colcache = self.searchcache.get(searchcol,None)
            if not colcache:
                self.create_search_colcache(searchcol)
                colcache = self.searchcache.get(searchcol,None)
            res_row = colcache.get(searchtext,None)
            if not res_row:
                return None # searchtext not found
            else:
                return self.tablemodel.getCellRecord(res_row-1, resultcol-1)
        else:
            pass
        return None
    
    def find_in_col_ret_row(self,searchtext, searchcol, cache=True):
        
        if cache:
            colcache = self.searchcache.get(searchcol,None)
            if not colcache:
                self.create_search_colcache(searchcol)
                colcache = self.searchcache.get(searchcol,None)
            res_row = colcache.get(searchtext,None)
            if not res_row:
                return None # searchtext not found
            else:
                return res_row
        return None    
                
    def find_in_col_set_col_val(self,searchtext, searchcol, setcol,setval,cache=False):
        if cache:
            colcache = self.searchcache.get(searchcol,None)
            if not colcache:
                self.create_search_colcache(searchcol)
                colcache = self.searchcache.get(searchcol,None)
            res_row = colcache.get(searchtext,None)
            if not res_row:
                return None # searchtext not found
            else:
                self.set_value_in_cell(res_row, setcol, setval)
                return True
        else:
            pass
        return None
    
    def Activate(self):
        global ActiveSheet
        ActiveSheet = self
        self.table.do_bindings()
        return
    
    def do_bindings(self):
        #print("do bindings")
        self.table.do_bindings()
        
    def remove_bindings(self):
        #print("remove bindings")
        self.table.remove_bindings()
    
    def Select(self):
        global ActiveSheet
        ActiveSheet = self
        return
    
    def getData(self):
        data = self.tablemodel.getData()
        return data
    
    def setData(self,data):
        self.tablemodel.createEmptyModel()
        self.tablemodel.setupModel(data)
        self.table.redrawTable()
        
    def getSelectedRow(self):
        selectedRow=self.table.getSelectedRow()+1
        return selectedRow
    
    def clearSheet(self):
        self.table.clearData(question=False)
        self.table.importCSV(filename=self.csv_filepathname, sep=';',fieldnames=self.fieldnames)
        self.tablemodel = self.table.getModel()
        if self.formating_dict:
            self.tablemodel.nodisplay = self.formating_dict.get("HideCells",[])
            self.tablemodel.protected_cells = self.formating_dict.get("ProtectedCells",[])
            self.tablemodel.format_cells = self.formating_dict.get("FontColor",{})
        #self.table.redraw()
        self.update_table_properties()
        self.Activate()

class CShapeList(object):
    def __init__(self,shapelist=[]):
        self.shapelist = shapelist
        
    def AddShape(self, name, shapetype, Left, Top, Width, Height, Fill):
        if shapetype == msoShapeRectangle:
            shape = CShape(name, shapetype, Left, Top, Width, Height, Fill)
            self.shapelist.append(shape)
            shape.index = len(self.shapelist)-1
            shape.tableshape=ActiveSheet.table.addShape(name, "rect", Left, Top, Width, Height, Fill,masteridx=shape.index)
            return shape
        
    def Delete(self,shape):
        self.shapelist.remove(shape)
            
        
    
class CShape(object):
    
    def __init__(self, name, shapetype, Left, Top, Width, Height, Fill):
        self.shapetype = shapetype
        self.Left=Left
        self.Top = Top
        self.Width = Width
        self.height = Height
        self.Name = name
        self.TextFrame2 = ""
        self.AlternativeText = ""
        self.TextFrame2 = ""
        self.Fill = Fill
        self.tableshape=None
        
    def updateShape(self):
        self.tableshape.updateShape(Fill=self.Fill,Text=self.TextFrame2)
        
        
    def Delete(self):
        
        pass
        
        
class CRange:
    def __init__(self,t1,t2,ws=None):
        #print("Range:",t1,t2)
        self.range_list=[]
        self.Rows=[]
        self.Columns = []
        self.Cells = []
        for col in range(t1[1],t2[1]+1):
            self.Columns.append(CColumn(col))
            for row in range(t1[0],t2[0]+1):
                self.range_list.append(ws.Cells(row, col))
        for row in range(t1[0],t2[0]+1):
            self.Rows.append(CRow(row))        
        self.CountLarge = len(self.range_list)
        self.Cells = self.range_list
        self.Font = CFont("Arial",10)
                
    def Find(self,What="", LookIn=xlFormulas, LookAt= xlWhole, SearchOrder= xlByRows, SearchDirection= xlNext, MatchCase= True, SearchFormat= False):
        for cell in self.range_list:
            if cell.Value == What:
                return cell
            
    def Offset(self, offset_row, offset_col):
        for cell in self.range_list:
            cell.offset(offset_row,offset_col)
        return self
    
    def Activate(self):
        for cell in self.range_list:
            cell.Activate()        
            
class CRectangles(object):
    def __init__(self):
        self.rlist = []
        self.Count=0
        
    def add(self,rectangle):
        self.rlist.append(rectangle)
        
    def delete(self,i):
        self.rlist.remove(i)
        

        
    #def __init__(self,rowrange,colrange):
    #    self.Rows=list()
    #    for i in range(rowrange[0],rowrange[1]):
    #        self.Rows.append(CRow(i))
    #    self.Columns=list()
    #    for i in range(colrange[0],colrange[1]):
    #        self.Columns.append(CRow(i))
    
class CRectangle(object):
    
    def __init__(self,row=0,col=0,i=0,onaction=""):
        self.OnAction = onaction
        self.TopLeftCell = CCell("")
        self.TopLeftCell.Row = row
        self.TopLeftCell.Column = col
        self.index = i
        pass
    
    def Delete(self):
        super().delete(self.index)
        pass
    
class CSelection:
    def __init__(self,cell):
        #self.EntireRow = CEntireRow(cell.Row)
        self.EntireColumn = CEntireColumn(cell.Column)
        self.Characters = ""
        self.selectedRows = []
        
    def EntireRow(self):
        self.selectedRows = []
        for row in ActiveSheet.table.multiplerowlist:
            self.selectedRows.append(row+1)
        if self.selectedRows==[]:
            self.selectedRows=[ActiveSheet.table.getSelectedRow()+1]
        return self.selectedRows

class CRow:
    def __init__(self,rownumber):
        self.Row = rownumber
        self.EntireRow = CEntireRow(rownumber)
        
class CEntireRow:
    def __init__(self,rownumber):
        self.Rownumber = rownumber
        self.Hidden = False

        
class CColumn:
    def __init__(self,colnumber):
        self.Column=colnumber
        self.EntireColumn = CEntireColumn(colnumber)
        self.columnwidth = 5
        
        
    def get_columnwidth(self):
        return self.columnwidth
    
    def set_columnwidth(self, value):
        self.columnwidth = value
        ActiveSheet.table.resizeColumn(self.Column-1,value)
        
        
    ColumnWidth = property(get_columnwidth, set_columnwidth, doc='Column Width')
        
class CEntireColumn:
    def __init__(self,colnumber):
        self.Columnnumber = colnumber
        self.Hidden = False
    
    
class CCell(str):
    def __init__(self,value,tablemodel=None):
        str.__init__(value)
        self.Orientation = 0
        self.Row = -1
        self.Column = -1
        self.Formula = ""
        self.tablemodel = tablemodel
        self.CountLarge = 1
        self.Parent = None
        self.Address = (self.Row,self.Column)
        self.Comment = None
        self.Font = CFont("Arial",10)
        self.HorizontalAlignment = xlCenter
        self.Sheet = ActiveSheet
        self.Text = value
        self.Value = value
        
    def __str__(self):
        return str(self.get_value())
    
    def __repr__(self):
        return str(self.get_value())
    
    def get_value(self):
        if self.Row != -1:
            if self.tablemodel == None:
                self.tablemodel = ActiveSheet.tablemodel
            max_cols = self.tablemodel.getColumnCount()
            if self.Column < max_cols:
                value = self.tablemodel.getValueAt(self.Row-1,self.Column-1)
            else:
                value = ""
        return value # self.__value
    
    def set_row(self,row):
        self.Row = row
        self.Address = (self.Row,self.Column)
        
    def set_column(self,column):
        self.Column=column
        self.Address = (self.Row,self.Column)
    
    def set_value(self, newval):
        if self.Sheet != None:
            if self.Row != -1:
                #print("Set_value",self.Row, self.Column,newval,self.Sheet.Name)
                if self.tablemodel == None:
                    self.tablemodel = ActiveSheet.tablemodel
                curval = self.tablemodel.getValueAt(self.Row-1, self.Column-1)
                if curval != newval:
                    self.tablemodel.setValueAt(newval, self.Row-1, self.Column-1)
                    if type(newval) != str:
                        print("Type not str",newval)
                    if Application.EnableEvents:
                        #print("Workbook contents changed:",)
                        ActiveSheet.EventWSchanged(self)
                            #M20.Global_Worksheet_Change(self)
                
    def set_tablemodel(self,tablemodel):
        self.tablemodel = tablemodel
        
    def set_sheet(self,sheet):
        self.Sheet=sheet
    
    def set_parent(self,parent):
        self.Parent = parent
        
    def check_if_empty_row(self):
        if self.tablemodel == None:
            self.tablemodel = ActiveSheet.tablemodel        
        cols = self.tablemodel.getColumnCount()
        r=self.Row-1
        for c in range(0,cols):
            #absr = self.get_AbsoluteRow(r)
            val = self.tablemodel.getValueAt(r,c)
            if val != None and val != '':
                return False
        return True
    
    def Offset(self, offset_row, offset_col):
        self.Row    = self.Row + offset_row
        self.Column = self.Column + offset_col
        ActiveSheet.table.gotoCell(self.Row-1,self.Column-1)
        return ActiveCell()
    
    def Select(self):
        ActiveSheet.table.gotoCell(self.Row-1,self.Column-1)
        ActiveSheet.EventWSselected(self)
        return
    
    def AutoFilter(self):
        print("Autofilter")
        
    def Activate(self):
        self.Parent.table.gotoCell(self.Row,self.Column)
        
    def Left(self):
        x1,y1,x2,y2 = ActiveSheet.table.getCellCoords(self.Row-1,self.Column-1)
        return x1
    
    def Top(self):
        x1,y1,x2,y2 = ActiveSheet.table.getCellCoords(self.Row-1,self.Column-1)
        return y1
    
    def Width(self):
        x1,y1,x2,y2 = ActiveSheet.table.getCellCoords(self.Row-1,self.Column-1)
        return x2-x1
    
    def Height(self):
        x1,y1,x2,y2 = ActiveSheet.table.getCellCoords(self.Row-1,self.Column-1)
        return y2-y1    
    
    Value = property(get_value, set_value, doc='value of CCell')
    Text = property(get_value, set_value, doc='value of CCell')
    
class CCellDict():
    def __init__ (self):
        data = {}
        
    def __getitem__(self, k):
        #print("Getitem",k)
        return Cells(k[0],k[1])
        
    def __setitem__(self,k,value):
        ccell = Cells(k[0],k[1])
        #print("Setitem",k, value,ccell.Sheet.Name)
        ccell.set_value(value)
        
        
class CWorksheetFunction:
    def __init__(self):
        pass
    def RoundUp(v1,v2):
        #print("RoundUp")
        if v2 == 0:
            if v1 == int(v1):
                return v1
            else:
                return int(v1 + 1)
        else:
            return "Error"
        
class CApplication:
    def __init__(self):
        self.StatusBar = ""
        self.EnableEvents = True
        self.ScreenUpdating = True
        self.Top = 0
        self.Left = 0
        self.Width = 1000 #*HL
        self.Height = 500 #*HL
        self.Version = "15"
        self.WindowState = 0
        self.caller=0
        self.canvas_leftclickcmd=None
        
    def set_canvas_leftclickcmd(self,cmd):
        self.canvas_leftclickcmd=cmd
        
        
    def OnTime(self,time,cmd):
        print("Application OnTime:",time,cmd)
        PG.global_controller.after(time,cmd)
        return
    
    def RoundUp(v1,v2):
        #print("RoundUp")
        if v2 == 0:
            if v1 == int(v1):
                return v1
            else:
                return int(v1 + 1)
        else:
            return "Error"
        
class CFont:
    def __init__(self,name,size):
        self.Name = name
        self.Size = size
        
class CActiveWindow:
    def __init__(self):
        Zoom = 100
        ScrollColumn = 1
        
class SoundLines:
    def __init__(self):
        self.dict = {}
        self.Count = 0
        self.keys = []
    
    def Exists(self,Channel:int):
        pass
    
    def Add(Channel, Pin_playerClass):
        pass
    
class CButton:
    def __init__(self,name):
        self.Name=name
        self.AlternativeText = ""
        self.TextFrame2 = ""
        self.Fill = (0,0,0)
        
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'


# global variables

ActiveWorkbook:CWorkbook = None

ActiveSheet:CWorksheet = None

#WorksheetFunction = CWorksheetFunction()

Application:CApplication = CApplication()

CellDict:CCellDict = CCellDict()

Selection = CSelection(CCell(""))

Workbooks = []

ActiveWindow = CActiveWindow()

#Date = "1.1.2022"
#Time = "12:00"


Now = 0

