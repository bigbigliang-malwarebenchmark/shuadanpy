#coding=utf-8
import requests
from requests import RequestException

def get_page(url):
    try:
        headers = {
            'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        # 伪装成浏览器
        }
        a = 0
        while 1:
            a = a + 1
            if(a < 10):
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    #print 'success!'
                    pass
                    #return response.text
                #return None
            if(a == 10):
                print 'success!'
                break
    except RequestException:
        print u'请求出错'
        return None

def main():
    url = 'https://www.xiaohongshu.com/page/topics/5d5515ec9916850001ab623b?tab=hot'  # 待刷浏览量博客的url
    get_page(url)

if __name__ == '__main__':
    main()