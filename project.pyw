from tkinter import *
import subprocess
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
root=Tk()
top=Label(root,text='MODULE INSTALLER APP',font=('Helvetica', 18, 'bold'),fg="red").pack()
l3=Label(root,text='ENTER THE NAME OF MODULE:').pack()
e=Entry(root)
e.pack()
def bu():
   subprocess.run('python -m pip install --upgrade pip')#updating pip to latest version
   p= subprocess.run('pip3 install '+e.get())
   if(p.returncode==1 and connect()==False):
      l=Label(root,text='error!!! occured check\n 1.NO Internet conection',fg="red").pack(side='bottom')
   if(p.returncode==0):
      l=Label(root,text=' It worked '+e.get()+" is installed",fg="green" ).pack(side='bottom')
   elif(p.returncode==1 and connect()==True):
      l=Label(root,text='error!!! occured check\n 1.Name of module \n',fg="red").pack(side='bottom')
b=Button(text="enter",command=bu)
b.pack()


root.mainloop()
