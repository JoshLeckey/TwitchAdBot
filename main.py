import threading
from random import randrange

from selenium import webdriver
import concurrent.futures
import ThreadPoolExecutorPlus
import urllib.request
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



def logic():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options)

    try:
        if len(proxies) != 0:
            options.add_argument('--proxy-server=%s' % proxies[randrange(0, len(proxies))])
    except:
        pass
    try:
        driver.get(url)
    except:
        driver.close()
        return
    try:
        time.sleep(3)
        button = driver.find_element_by_class_name("fLjesT").submit()
    except:
        pass
    try:
        time.sleep(1)
        ad = driver.find_element_by_class_name("iSkfse")
        print("watching ad now :)")
        time.sleep(30)
        driver.quit()
    except:
        print("no ads -- Quiting")
        driver.quit()


capabilities = webdriver.DesiredCapabilities.CHROME
url = "https://www.twitch.tv/"
url += input("Enter Channel Name e.g. bethesda (dont include the twitch.tv/)\n")
threads = input("Enter the amount of threads\n")
threads = int(threads)
threads_list = list()
proxies = []
answer = input("Do you want to use proxies (Y/N)\n")
if answer.upper() == "Y" or answer.upper() == "YES":
    pbo = False
    while(pbo == False):
        location = input("Enter the proxy location\n")
        try:
            proxyf = open(location, "r")
        except:
            next()
        count = 0
        proxytype = input("What is the proxy type (Socks, http, ssl)\n")
        for line in proxyf:
            if line != "\n":
                proxies.append(line.strip())
        proxyf.close()
        pbo = True

for i in range(threads):
    t = threading.Thread(name='Thread {}'.format(i), target=logic())
    t.start()
    time.sleep(1)
    print (t.name + 'started')
    threads_list.append(t)

for thread in threads_list:
    thread.join()

print ("Completed")


