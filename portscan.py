#!/usr/bin/python
#encoding:utf-8

import telnetlib
import threading
import threading
import sys
import requests
import time
import ssl
import re

def thread1(url):
    for port in [0, 80, 88, 95, 101, 102, 105, 107, 109, 110, 111, 113, 115, 117, 119, 123, 137, 138, 139, 143, 161, 162, 163, 164, 174, 177, 178, 179, 191, 194, 199, 201]:
        try:
            t = threading.Thread(target=scan, args=(url, port, ))
            t.start()
            t.join()

        except Exception as a:
            print('**************************线程等待，请稍后'.decode("utf-8").encode("gbk"))
            time.sleep(10)
            pass

def thread2(url):
    for port in [202, 204, 206, 209, 210, 213, 220, 245, 347, 363, 369, 370, 372, 389, 427, 434, 435, 443, 444, 445, 464, 468, 487, 488, 496, 500, 535, 538, 546, 547, 554, 563, 565, 587, 610, 611, 612, 631, 636, 674, 694, 749, 750, 765, 767, 873]:
        try:
            t = threading.Thread(target=scan, args=(url, port, ))
            t.start()
            t.join()

        except Exception as a:
            print('**************************线程等待，请稍后'.decode("utf-8").encode("gbk"))
            time.sleep(10)
            pass

def thread3(url):
    for port in [751, 752, 754, 760, 1109, 2053, 2105, 98, 106, 465, 616, 808, 871, 901, 953, 1127, 1178, 1313, 1529, 2003, 2150, 2988, 3128, 3455, 5432, 4557, 4559, 5232, 5354, 5355, 5680, 6010, 6667, 7100, 7666, 8008, 8080, 8081, 8888, 9080, 9090, 9100, 9359, 10081, 10082, 10083, 20011, 20012, 22305, 22289, 22321, 24554, 27374, 60177, 60179]:
        try:
            t = threading.Thread(target=scan, args=(url, port, ))
            t.start()
            t.join()

        except Exception as a:
            print('**************************线程等待，请稍后'.decode("utf-8").encode("gbk"))
            time.sleep(10)
            pass

def thread4(url):
    for port in [992, 993, 994, 995, 512, 513, 514, 515, 1080, 1236, 1300, 1433, 1434, 1494, 1512, 1524, 1525, 1645, 1646, 1649, 1701, 1718, 1719, 1720, 1758, 1759, 1789, 1812, 1813, 1911, 1985, 1986, 1997, 2049, 2102, 2103, 2104, 2401, 2430, 2431, 2432, 2433, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2809, 3130, 3306, 3346, 4011, 4321, 4444, 5002, 5308, 5999, 6000, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 9876, 10080, 11371, 11720, 13720, 13721, 13722, 13724, 13782, 13783, 22273, 26000, 26208, 33434]:
        try:
            t = threading.Thread(target=scan, args=(url, port, ))
            t.start()
            t.join()

        except Exception as a:
            print('**************************线程等待，请稍后'.decode("utf-8").encode("gbk"))
            time.sleep(10)
            pass

def so(url):

    threading.Thread(target=thread1, args=(url, )).start()
    threading.Thread(target=thread2, args=(url, )).start()
    threading.Thread(target=thread3, args=(url, )).start()
    threading.Thread(target=thread4, args=(url, )).start()

def scan(url, port):

    mulu= ['/dump',
           '/trace',
           '/logfile',
           '/env',
           '/actuator/',
           '/jolokia/list',
           '/robots.txt',
           '/.htaccess',
           '/admin',
           '/WEB-INF/web.xml',
		   '/webpage/system/druid/websession.json',
           '/.svn/entries',
           '/cms',
           '/FCKeditor',
           '/fck',
           '/console/login/LoginForm.jsp',
           '/jenkins/',
           '/em/',
           '/isqlplus/',
           '/ws_utc/config.do',
           '/ws_utc/begin.do',
           '/jmx-console/',
           '/install/',
           '/uddiexplorer/SearchPublicRegistries.jsp',
           '/crossdomain.xml',
           '/WS_FTP.LOG',
           '/console/',
           '/fckeditor/editor/filemanager/connectors/test.html',
           '/.svn/all-wcprops',
           '/manage',
           '/script',
           '/_nodes',
           '/_river',
           '/_config',
           '/containers/json',
           '/index.jsp',
           '/index.html',
           '/Admin',
           '/Admin/login.jsp',
           '/Admin/Login.jsp',
           '/system',
           '/home',
           '/wp-admin/includes/admin.php',
           '/wp-settings.php',
           '/phpinfo.php',
           '/admin.jsp',
           '/login.php',
           '/login.jsp',
           '/index.action',
           '/_plugin/head/',
           '/logs',
           '/solr/#/',
           '/script',
           '/info.php',
           '/phpmyadmin',
           '/phpMyAdmin',
           '/Main.aspx',
           '/login.aspx',
           '/jmx-console',
           '/web-console',
           '/zh-CN/app/Callat/home',
           '/webalizer',
		   '/ws/services',
		   '/ws/services/HelloServices?wsdl'
           ]
    try:
        header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://'+url,
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        #file = open('result.txt', 'w+')

        url2 = "http://"+url+":"+str(port)
        if port == 0:
            url2 = "https://"+url


        #context = ssl._create_unverified_context()
        reponse = requests.get(url2, timeout=3, headers=header)

        code = reponse.status_code

        try:
            banner = reponse.headers['Server'][:25]
        except:
            banner = 'NULL'

        if code == 200 or code == 302 or code == 403 or code == 404 or code == 500:
            print(url2+'-------------------'+str(code)+'***************端口存活'.decode("utf-8").encode("gbk"))

            file = r"result.txt"
            with open(file, 'a+') as f1:
                f1.write(url2+'     ------------'+str(code)+'------------'+'Len---0---Len'+'\n')
                f1.close()

            for m in mulu:
                with open(file, 'a+') as f:
                    try:
                        print(url2+m)
                        reponse2 = requests.get(url2+m, timeout=3, headers=header)
                        code2 = reponse2.status_code
                        if code2 == 200 or code2 == 403 or code == 201:
                            print(url2+m+'*************************'+'存活')
                            html = reponse2.text
                            f.write(url2+m+'              ---------------'+str(code2)+'--------------'+'Len---'+str(html.__len__())+'---Len'+'\n')
                            f.close()
                        else:
                            f.close()
                    except:
                        pass

            urls.append(url2+'-----'+str(code))


    except Exception as a:
        file = r'result.txt'
        if str(a).find('SSLError') >= 0:
            print(url2+'--------'+'200'+'***************端口存活'.decode("utf-8").encode("gbk"))

            with open(file, 'a+') as f1:
                f1.write(url2+'     ------------'+'Len---0---Len'+'\n')
                f1.close()
            for m in mulu:
                with open(file, 'a+') as f:
                    try:
                        reponse2 = requests.get(url2+m, timeout=3, headers=header)
                        print(url2+m)
                        code2 = reponse2.status_code
                        if code2 == 200 or code2 == 403 or code == 201:
                            print(url2+m+'*************************'+'存活')
                            html = reponse2.text
                            f.write(url2+m+'       ---------------'+str(code2)+'--------------'+'Len---'+str(html.__len__())+'---Len'+'\n')
                            f.close()
                        else:
                            f.close()
                    except:
                        pass

        pass


if __name__ == '__main__':
    urls = []
    threads = []

    file1 = open('result.txt','w')
    file1.close()

    file2 = open('result2.txt','w')
    file2.close()

    urllist = open('url.txt','r')
    lines = urllist.readlines()
    n = 5
    for line in lines:
        so(line.replace('\n',''))
        n = n - 1

    urllist.close()

    time.sleep(1)


