# bs4解析库的使用
import requests
from bs4 import BeautifulSoup

# bs4的4种解析器
# bs4的HTML解析器  安装bs4
container = "html.parser"


# Ixml的HTML解析器 pip install Ixml
# container = "Ixml"
# Ixml的XML解析器 pip install Ixml
# container = "xml"
# html5lib的解析器 pip install html5lib
# container = "html5lib"


def analysisSoup():
    try:
        r = requests.get("https://python123.io/ws/demo.html")
        print(r.status_code)
        r.raise_for_status()
        demo = r.text
        soup = BeautifulSoup(demo, container)
        # 打印网页源代码
        print(soup.prettify())
        print("-------------------------")
        # 打印title
        print(soup.title)
        # 打印解析出来的页面当中的a标签(获取第一个a标签)
        print(soup.a)
        # 获取tag的名字
        print(soup.a.name)
        # 获取a这个tag的父tag的名字
        print(soup.a.parent.name)
        # p tag的名称
        print(soup.a.parent.parent.name)
        # 获取a标签的属性 获取的是一个字典，所以可以用字典的方式对其中的每一个信息进行提取
        dictAttrs = soup.a.attrs
        print(dictAttrs)
        # 获取a标签属性当中的class属性
        print(dictAttrs["class"])
        # 获取a标签属性当中的链接属性
        print(dictAttrs["href"])
        # 打印标签属性的类型 (是个字典类型)
        # 如果没有属性时，获取的是一个空字典，但是不论是否有属性，总是能获取一个字典
        print(type(dictAttrs))
        # 打印标签本身的类型 (是个bs4.element.Tag类型)
        print(type(soup.a))
        # 打印a标签当中的内容(字符串)信息
        print(soup.a.string)
        # 打印P标签当中的内容(字符串)信息
        print(soup.p.string)
        # 打印p标签的字符串内容对应的类型 (是一个bs4.element.NavigableString类型)
        # 其实看打印的内容，p标签的下级还有一个b标签，但是并没有打印出b标签对应的类型
        # 说明NavigableString是可以跨越多个标签层次的
        print(type(soup.p.string))
        newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", container)
        # 打印b标签当中的内容(字符串)信息
        print(newsoup.b.string)
        # 打印b标签的字符串内容对应的类型 (是一个bs4.element.Comment类型)
        print(type(newsoup.b.string))
        # 需要对文本的类型做出判断，以判断它究竟是不是注释的类型
    except:
        print("爬取失败")


if __name__ == "__main__":
    analysisSoup()
