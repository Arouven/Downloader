from tkinter import*


obj=Tk()  
obj.title("youtube-dl")  
obj.geometry("600x600")  
wintext = Text(obj)  



from subprocess import call

command = "youtube-dl https://www.youtube.com/watch?v=NG3WygJmiVs -c"
call(command.split(), shell=False)


wintext.insert(INSERT, "Hello.....")  
wintext.insert(END, "welcome to c# corner.....")  
wintext.pack()  
obj.mainloop()   