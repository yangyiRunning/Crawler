# 爬虫通用代码框架
import requests


def getHtmlText(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "https://92.91p22.space/v.php?category=mf&viewtype=basic&page=53"
    print(getHtmlText(url))
