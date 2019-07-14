# 爬取最好大学网上的大学排名信息 (定向爬虫)

# 1. 从网络上获取大学排名网页内容  getHTMLText()
# 2. 提取网页内容中信息到合适的数据结构  fillUnivList()
# 3. 利用数据结构展示并输出结果  printUnivList()

# BeautifulSoup只是bs4库中的一个类
import bs4

container = "html.parser"

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, container)
    for t in soup.find("tbody").children:
        if isinstance(t, bs4.element.Tag):
            tds = t("td")
            # print(tds)
            # 在列表ulist中的添加字段
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:{4}^10}"
    print(tplt.format("排名", "学校名称", "地点", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0] if u[0] else "",
                          u[1] if u[1] else "",
                          u[2] if u[2] else "",
                          u[3] if u[3] else "",
                          chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # top 20
    printUnivList(uinfo, 20)


if __name__ == "__main__":
    main()
