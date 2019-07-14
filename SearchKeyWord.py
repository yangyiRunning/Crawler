# 通过百度搜索引擎查询关键词

import requests


def searchWord():
    try:
        kv = {"wd", "python"}
        r = requests.get("http://www.baidu.com/s", params=kv)
        print(r.headers)
        print(r.status_code)
        print(r.request.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")


if __name__ == "__main__":
    searchWord()
