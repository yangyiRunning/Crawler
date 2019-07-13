# 通过篡改headers的方式爬取当当书籍
import requests


def getDangForce(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        print(r.request.header)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")


if __name__ == "__main__":
    print(getDangForce("https://www.baidu.com"))
