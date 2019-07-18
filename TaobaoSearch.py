# 淘宝商品比较定向爬虫

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取异常"


def parsePage(listType, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            # 去掉最外层的单引号或者双引号
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            listType.append(price, title)
    except:
        print("转换异常")


def printGoodList(listType):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for i in listType:
        count = count + 1
        print(tplt.format(count, i[0], i[1]))


def main():
    goods = "书包"
    depth = 3
    searchUrl = "https//s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = searchUrl + "&s=" + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)


if __name__ == "__main__":
    main()
