from tkinter import *
import subprocess
root=Tk()

l3=Label(root,text='ENTER THE NAME OF MODULE:').pack()
e=Entry(root)
e.pack()
def bu():
   p= subprocess.run('pip3 install '+e.get())
   if(p.returncode==1):
      l=Label(root,text='error!!! occured check\n 1.Name of module \n 2. Internet conection',fg="red").pack(side='bottom')
   if(p.returncode==0):
      l=Label(root,text=' It worked '+e.get()+" is installed",fg="green" ).pack(side='bottom')
   

b=Button(text="enter",command=bu)
b.pack()


root.mainloop()
