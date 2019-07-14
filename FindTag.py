# 基于bs4库的HTML内容查找方法

url = "https://python123.io/ws/demo.html"
container = "html.parser"

import requests
from bs4 import BeautifulSoup
import re


def findTags():
    try:
        r = requests.get(url)
        r.raise_for_status()
        demo = r.text
        soup = BeautifulSoup(demo, container)
        # 会返回一个列表类型的对象
        print(soup.find_all("a"))
        print(soup.find_all(["a", "b"]))
        print("----------------------")
        # 打印所有的标签信息
        for t in soup.find_all(True):
            print(t.name)
        print("----------------------")
        # 打印以b开头的所有的信息
        for t in soup.find_all(re.compile("b")):
            print(t.name)
        print("----------------------")
        # 打印p标签中包含course属性的信息
        print(soup.find_all("p", "course"))
        print("----------------------")
        # 查找id的为link1的值
        print(soup.find_all(id='link1'))
        # 查找id的为link的值
        print(soup.find_all(id='link'))
        # 查找以link开头但是不与link完全一致的标签形式
        print(soup.find_all(id=re.compile("link")))
        print("----------------------")
        # 是否对子孙全部检索，默认是True
        print(soup.find_all("a", recursive=True))
        print(soup.find_all("a", recursive=False))
        # <>...</>中的字符串区域的检索字符串
        print(soup.find_all(string="Basic Python"))
        print(soup.find_all(string=re.compile("python")))
    except:
        print("爬取异常")


if __name__ == "__main__":
    findTags()
