# 信息的标记 XML Json YAML 三种标记格式

# 提取HTML中的所有URL链接

# 1. 搜索到所有的a标签
# 2. 解析a标签格式，提取href后的链接的内容

url = "https://python123.io/ws/demo.html"
container = "html.parser"

import requests
from bs4 import BeautifulSoup


def findAllAATag():
    try:
        r = requests.get(url)
        r.raise_for_status()
        demo = r.text
        soup = BeautifulSoup(demo, container)
        for link in soup.find_all("a"):
            print(link.get("href"))
    except:
        print("爬取异常")


if __name__ == "__main__":
    findAllAATag()
