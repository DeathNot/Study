import requests
from bs4 import BeautifulSoup
import time
import random

class IP():
    
    def __init__(self):
        self.start_url = 'http://www.ip3389.com/ih/'
        self.headers = {
            'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
    
    def getHtmlText(self, url, code='utf-8'):
        try:
            r = requests.get(url, headers=self.headers, timeout=30)
            r.raise_for_status()
            r.encoding = code
            return r.text
        except:
            return ''
    
    def getPageNum(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        pageNum = soup.find_all('a',{'class':'num'})[-1].text
        return int(pageNum)
        
    def getIPList(self, num):
        url = self.start_url + 'p' + str(num) + '/'
        html = self.getHtmlText(url)
        soup = BeautifulSoup(html, 'html.parser')
        ip_list = soup.find('table', {'id':'ip_list'})
        trs = ip_list.find_all('tr')
        for tr in trs:
            try:
                td = tr.find_all('td')
                yield td[2].text + ':' + td[3].text
            except:
                continue
    
    def saveIP(self, ipLst):
        root = 'E:\\ip.txt'
        with open(root, 'a') as f:
            for ip in ipLst:
                try:
                    f.write(ip + '\n')
                except:
                    continue
        f.close()
    
    def getRandomList(self):
        root = 'E:\\ip.txt'
        iplst = []
        with open(root, 'r') as f:
            for i in f.readlines():
                iplst.append('http://' + i.strip())
        f.close()
        return iplst
    
    def getRandomIP(self, iplst):
        proxy_ip = random.choice(iplst)
        proxies = {'http':proxy_ip}
        return proxies
        
    def run(self, nu=100):
        for i in range(1, nu+1):
            time.sleep(3)
            try:
                ipLst = self.getIPList(i)
                self.saveIP(ipLst)        
            except:
                continue       