import requests


def getDang(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        print("爬取失败")


if __name__ == "__main__":
    print(getDang("http://search.dangdang.com/?key=%B5%CD%D3%FB%CD%FB%C9%E7%BB%E1&act=input"))
