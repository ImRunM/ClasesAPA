# coding: utf-8
import tkinter as tk
import tkinter.messagebox as msg
get_ipython().run_line_magic('pinfo', 'msg.askquestion')
msg.askquestion()
resposta = msg.askquestion()
resposta == tk.YES
resposta == tk.yes
tk.yes
tk.YES
resposta == tk.OK
resposta == msg.YES
resposta = msg.askquestion()
resposta = msg.yes
resposta = msg.YES
resposta == msg.YES
resposta == msg.askquestion(type = msg.OK)
resposta = msg.askquestion(type = msg.OK)
resposta
resposta = msg.askquestion(type = msg.ABORTRETRYIGNORE)
resposta
resposta = msg.askquestion(type = msg.ABORTRETRYIGNORE)
resposta
resposta = msg.askquestion(type = msg.ABORTRETRYIGNORE)
resposta = msg.askquestion(type = msg.ABORTRETRYIGNORE)
resposta = msg.askquestion(type = msg.ABORTRETRYIGNORE)
resposta = msg.askquestion(type = msg.ABORTRETRYIGNORE)
resposta = msg.askquestion(type = msg.OKCANCEL, title = "Títol")
resposta = msg.askquestion(type = msg.OKCANCEL, title = 'Títol')
resposta = msg.askquestion(type = msg.OKCANCEL, title = 'Títol', message = 'Esto provocará el fin del mundo')
resposta = msg.askquestion(type = msg.OKCANCEL, title = 'Títol', message = 'Esto provocará el fin del mundo', detail = '¿Seguro que quieres hacerlo?')
resposta = msg.askquestion(type = msg.OKCANCEL, title = 'Títol', message = 'Esto provocará el fin del mundo', detail = '¿Seguro que quieres hacerlo?', icon = msg.WARNING)
resposta = msg.askquestion(type = msg.OKCANCEL, title = 'Títol', message = 'Esto provocará el fin del mundo', detail = '¿Seguro que quieres hacerlo?', icon = msg.ERROR)
from tkinter import simpledialog as sd
sd.askfloat(title = 'tutula', prompt = 1)
real = sd.askfloat(title = 'tutula', prompt = '¡METE UN REAL ENERGUMENO!')
real 
real = sd.askfloat(title = 'tutula', prompt = '¡METE UN REAL ENERGUMENO!', minvalue = 13, maxvalue = 14)
real
real = sd.askfloat(title = 'tutula', prompt = '¡METE UN REAL ENERGUMENO!', minvalue = 13, maxvalue = 14, initialvalue = 33)
sd.askstring(title = 'Titulo', prompt = 'Pon tu contraseña')
sd.askstring(title = 'Titulo', prompt = 'Pon tu contraseña', show = '-')
from tkinter import filedialog as fd
fd.askopenfile() 
fd.askopenfile()
import Path
from pathlib import Path
file = fd.askopenfile()
file 
path(file)
filename = fd.askopenfilename()
filename = fd.askopenfilename()
filename = fd.askopenfilename(initialdir = Path(filename).parent) # para que al repetir el comando vuelva a ponerse el último directorio visitado
filename = fd.askopenfilename(initialdir = Path(filename).parent, filetypes = (('aidop', '.wa .mp3 .au'),('video', '.mp4 .avi .mov'), ('imagen', '.jpg .png')))
# .*  indica cualquier tipo de archivo
filename = fd.askopenfilename(initialdir = Path(filename).parent, filetypes = (('aidop', '.wa .mp3 .au'),('video', '.mp4 .avi .mov'), ('imagen', '.jpg .png'), ('Todo', '.*)))
filename = fd.askopenfilename(initialdir = Path(filename).parent, filetypes = (('aidop', '.wa .mp3 .au'),('video', '.mp4 .avi .mov'), ('imagen', '.jpg .png'), ('Todo', '.*')))
filename = fd.asksaveasfilename(defaultextension = '.wav')
filename 
filename = fd.askopenfilenames()
filename = fd.askopenfilename(initialdir = Path(filename).parent, filetypes = (('aidop', '.wa .mp3 .au'),('video', '.mp4 .avi .mov'), ('imagen', '.jpg .png'), ('Todo', '.*')))
filename = fd.askopenfilename(initialdir = Path(filename).parent, filetypes = (('aidop', '.wav .mp3 .au'),('video', '.mp4 .avi .mov'), ('imagen', '.jpg .png'), ('Todo', '.*')))
filename = fd.askopenfilenames()
filename
filename = fd.askopenfilenames()
filenme 
filename
filename = fd.askdirectory()
filename
from tkinter.colorchooser import askcolor
#Hay diferentes maneras de indicar colores: modo RGB (255, 0, 0), cadena de texto que empieza con # y se codifica en hexadecimal (#FF0000) y el nombre descritivo en ingles ('red')
askcolor()
askcolor()
askcolor()
askcolor('deepskyblue')
askcolor(title = '¿Color?','deepskyblue')
askcolor(title = '¿Color?',color = 'deepskyblue')
get_ipython().run_line_magic('save', '')
