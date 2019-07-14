# 查询IP地址

import requests

url = "https://tool.lu/search/?query="


def searchIPAddress():
    try:
        r = requests.get(url + "111.199.189.211")
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("爬取失败")


if __name__ == "__main__":
    searchIPAddress()
