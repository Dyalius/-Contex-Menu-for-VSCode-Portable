#REG_FILES = r"SOFTWARE\Classes\*\shell\VSCode"
REG_FILES = r"SOFTWARE\Classes\*\shell\VSCode"

from winreg import *
def set_reg_root(keyval,value_name,type,value):
    try:
        try:
            try:
                registry_key = OpenKey(HKEY_CLASSES_ROOT, keyval, 0,KEY_ALL_ACCESS)#modify if exists
            except:
                pass
        except:
            try:
                registry_key = CreateKey(HKEY_CLASSES_ROOT, keyval)#create if not exists

            except:
                pass
        SetValueEx(registry_key,value_name,0,type,value)
        registry_key.Close()
        return True
    except WindowsError:
        return WindowsError

def get_reg(keyval,name):
    try:
        registry_key = OpenKey(HKEY_CLASSES_ROOT, keyval, 0,KEY_ALL_ACCESS)#modify if exists
        save = QueryValueEx(registry_key, name)
        registry_key.Close()
        return save
    except WindowsError:
        return WindowsError
    
def getRegKey(KEY,keyval):
    try:
        try:
            registry_key = OpenKey(KEY, keyval, 0,KEY_ALL_ACCESS)#modify if exists
        except:
            return false
    except:
        try:
            registry_key = CreateKey(KEY, keyval)#create if not exists
        except:
            return false
    return registry_key

def SetValue_inKey(KEY,reg_value_as_path,value_name,type,value):
    try:
        key=getRegKey(KEY,reg_value_as_path)
    except WindowsError:
        return WindowsError
    set=SetValueEx(key,value_name,0,type,value)
    key.Close()
    return set

#key variables
root=HKEY_CLASSES_ROOT
localm=HKEY_LOCAL_MACHINE
#gloval variables
import os
pwd=os.path.dirname(os.path.abspath(__file__))
Context_Value = r"Open w&ith Codexd"
Code_exe_Path = pwd+r"\Code.exe"
#Code_exe_Path = r"C:\Program Files\Microsoft VS Code\Code.exe"



#shell variables
    #shell default
shell_path = r"SOFTWARE\Classes\*\shell\VSCode"
shell_def_value = Context_Value
shell_icon_value = Code_exe_Path
    #shell default comm
shell_path_command = shell_path+r"\command"
shell_command_def = r'"'+Code_exe_Path+r'" "%1"'


#directory variables

directory_path = r"SOFTWARE\Classes\Directory\shell\VSCode"
directory_def_value = Context_Value
directory_icon_value = Code_exe_Path

directory_path_command = directory_path+r"\command"
directory_command_def = r'"'+Code_exe_Path+r'" "%V"'


#background variables

background_path = r"SOFTWARE\Classes\Directory\background\shell\VSCode"
background_def_value = Context_Value
background_icon_value = Code_exe_Path

background_path_command = background_path+r"\command"
background_command_def = r'"'+Code_exe_Path+r'" "%V"'

#drive variables

drive_path = r"SOFTWARE\Classes\Drive\shell\VSCode"
drive_def_value = Context_Value
drive_icon_value = Code_exe_Path

drive_path_command = drive_path+r"\command"
drive_command_def = r'"'+Code_exe_Path+r'" "%V"'




#set shell default
set_shell = SetValue_inKey(localm,shell_path,"",REG_EXPAND_SZ,shell_def_value)
set_shell_icon = SetValue_inKey(localm,shell_path,"Icon",REG_EXPAND_SZ,shell_icon_value)
#set shell command
set_shell_command = SetValue_inKey(localm,shell_path_command,"",REG_EXPAND_SZ,shell_command_def)

#set directory default
set_directory = SetValue_inKey(localm,directory_path,"",REG_EXPAND_SZ,directory_def_value)
set_directory_icon = SetValue_inKey(localm,directory_path,"Icon",REG_EXPAND_SZ,directory_icon_value)
#set directory command
set_directory_command = SetValue_inKey(localm,directory_path_command,"",REG_EXPAND_SZ,directory_command_def)

#set background default
set_background = SetValue_inKey(localm,background_path,"",REG_EXPAND_SZ,background_def_value)
set_background_icon = SetValue_inKey(localm,background_path,"Icon",REG_EXPAND_SZ,background_icon_value)
#set background command
set_background_command = SetValue_inKey(localm,background_path_command,"",REG_EXPAND_SZ,background_command_def)

#set drive default
set_drive = SetValue_inKey(localm,drive_path,"",REG_EXPAND_SZ,drive_def_value)
set_drive_icon = SetValue_inKey(localm,drive_path,"Icon",REG_EXPAND_SZ,drive_icon_value)
#set drive command
set_drive_command = SetValue_inKey(localm,drive_path_command,"",REG_EXPAND_SZ,drive_command_def)



#a=set_reg_root(REG_PATH_SHELL,"",REG_SZ,r"Open w&ith Codee")
#b=set_reg_root(REG_PATH_SHELL,"Icon",REG_SZ,r"C:\Program Files\Microsoft VS Code\Code.exe")
#c=b=set_reg_root(REG_PATH_SHELL+r"command","",REG_EXPAND_SZ,r'"C:\Program Files\Microsoft VS Code\Code.exe" "%1"')
#get_value=get_reg(REG_FILES,"test")

#print(a)
