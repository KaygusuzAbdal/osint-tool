# -*- coding: utf-8 -*-

try:
    from googlesearch import search
except ImportError:
    print("'googlesearch' isimli modül bulunamadı")

try:
    import requests
except ImportError:
    print("'requests' isimli modül bulunamadı")

try:
    import time
except ImportError:
    print("'time' isimli modül bulunamadı")

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("'BeautifulSoup' isimli modül bulunamadı")

try:
    from lxml.html import fromstring
except ImportError:
    print("'fromstring' isimli modül bulunamadı")

try:
    from itertools import cycle
except ImportError:
    print("'cycle' isimli modül bulunamadı")

try:
    import subprocess
except ImportError:
    print("'subprocess' isimli modül bulunamadı")

try:
    import sys
except ImportError:
    print("'sys' isimli modül bulunamadı")


try:
    import signal
except ImportError:
    print("'signal' isimli modül bulunamadı")


def clear():
    subprocess.call(["clear"])


def get_intro():
    print("\033[1;31m")
    print(r"""
  ______           __      __  __           __      ______                   
 /_  __/_  _______/ /__   / / / /___ ______/ /__   /_  __/__  ____ _____ ___ 
  / / / / / / ___/ //_/  / /_/ / __ `/ ___/ //_/    / / / _ \/ __ `/ __ `__ \
 / / / /_/ / /  / ,<    / __  / /_/ / /__/ ,<      / / /  __/ /_/ / / / / / /
/_/  \__,_/_/  /_/|_|  /_/ /_/\__,_/\___/_/|_|    /_/  \___/\__,_/_/ /_/ /_/ 

                            """)
    print("\033[1;36mOSINT Uygulaması".center(83))
    print("")
    print("\033[1;31mİstihbarat Tim".center(83))
    print("\033[1;37m Livcon\n".center(83))
    print("\033[1;32mProgramın kullanımı hakkında daha fazla bilgi edinmek için:\n\033[1;37mTelegramdan bana ulaşabilirsiniz: https://t.me/Livcon\n")


def signal_handler(sig, frame):
    print("")
    sys.exit(0)


def filter_by_domain(list):
    global domainList
    result = []
    for domain in domainList:
        if domain in list:
            result.append(list)
    return result


def printList(list):
    for x in range(0, len(list)):
        print(list[x])


def exitList():
    input("\n\033[1;37mÇıkmak için enter'a basınız")
    clear()
    print('\033[1;31m\nSistem kapatıldı')
    print('\033[1;37mBu programı tercih ettiğiniz için teşekkürler')
    sys.exit(0)


def googleSearch(query):
    global domainList
    clear()
    print("\n\033[1;36mSonuçlar Aranıyor ...\nBu işlem birkaç dakika sürebilir\033[1;37m")
    googleResult = list(search(query, tld="co.in", pause=2))
    if len(googleResult) < 1:
        print("\033[1;31mAradığınız kriterlerde hiçbir sonuç bulunamadı\n")
        return " "
    else:
        print("\033[1;36m" + str(len(googleResult)) + " Sonuç Bulundu!\n\033[1;32m")
        return googleResult


def filterSearch(result):
    global domainList
    filteredList = list(filter(filter_by_domain, result))
    if len(filteredList) < 1:
        print("\033[1;31mAradığınız kriterlerde hiçbir sonuç bulunamadı\n")
    else:
        print("\033[1;36m" + str(len(filteredList)) + " Sonuç Bulundu!\n\033[1;32m")
    printList(filteredList)
    print("\n\033[1;36mŞu domainlere göre filtrelendi : ")
    print(str(domainList) + "\033[1;37m")
    exitList()


def dorkoptions():
    clear()
    get_intro()
    print("\033[1;37m [1] Manual")
    print("\033[1;37m [2] AllInText")
    print("\033[1;37m [3] InText")
    print("\033[1;37m [4] AllInUrl")
    print("\033[1;37m [5] InUrl")
    print("\033[1;37m [6] AllInTitle")
    print("\033[1;37m [7] InTitle")
    print("\033[1;37m [8] Geri Dön")


domainList = []


def optionFilter():
    while True:
        global domainList, query
        filterOption = input("\n Sonuçları filtrelemek ister misiniz ? (Y/n) ")
        if not filterOption:
            clear()
            get_intro()
            print("\033[1;31m Lütfen bir seçenek seçin!\033[1;37m")
        elif filterOption.upper() == "N":
            print(googleSearch(query))
            exitList()
            break
        elif filterOption.upper() == "Y":
            domainList = [item for item in input("\n Filtrelenecek domainleri (arada bir boşluk bırakarak) giriniz\n  > ").split()]
            if len(domainList) == 0:
                domainList = ["instagram", "youtube", "steam", "facebook", "ayyildiz", "turkhackteam", "imhatimi",
                              "spyhackerz",
                              "crackturkey", "turksiberkonseyi", "turkdefarmy", "crackerteam", "siberdeyiz", "linkedin",
                              "donanimhaber", "snapchat"]
            if len(query) > 1:
                filterSearch(googleSearch(query))
                break


def optionDork():
    while True:
        optionDork = input("\n Dork kullanmak ister misiniz ? (Y/n) ")
        if not optionDork:
            clear()
            get_intro()
            print("\033[1;31m Lütfen bir seçenek seçin!\033[1;37m")
        elif optionDork.upper() == "N":
            searchTexts()
            break
        elif optionDork.upper() == "Y":
            dorkoptions()
            choice = input("\n\033[1;37m Lütfen yukarıdaki seçeneklerden birini seçiniz > ")
            if choice == "1":
                searchTexts()
                break


query = ""


def searchTexts():
    while True:
        global query
        query = input("\n Aramak istediğiniz kelimeyi girin\n  > ")
        if len(query) == 0:
            clear()
            get_intro()
            print("\033[1;31m Lütfen aratmak için bir değer girin!\033[1;37m")
            continue
        elif len(query) < 2:
            clear()
            get_intro()
            print("\033[1;31m Yanlış veya bulunması zor bir değer girdiniz!\033[1;37m")
            continue
        optionFilter()


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:100]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            editedProxy = "https://" + proxy
            proxies.add(editedProxy)
    return proxies


def setProxy():
    print("\033[0;37mProxy listesi alınıyor..")
    proxies = get_proxies()
    url = 'https://httpbin.org/ip'
    proxy_pool = cycle(proxies)
    print("\033[1;32mProxy listesi alındı\n\033[0;37m")
    for i in range(1, 58):
        proxy = next(proxy_pool)
        print("Proxy #%d bağlantı için deneniyor.." % i + "\nBu işlem birkaç dakika sürebilir")
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy})
            print("\033[1;32mProxy bağlantısı kuruldu\n\033[0;37m")
            print(response.json())
            print("Sistem açılıyor..")
            time.sleep(3)
            break
        except:
            print("\033[1;31mBaşarısız. Bağlantı hatası\n\033[0;37m")


signal.signal(signal.SIGINT, signal_handler)
clear()
setProxy()
clear()
get_intro()
optionDork()
