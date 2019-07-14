# 对HTML标签树的遍历


import requests
from bs4 import BeautifulSoup

url = "https://python123.io/ws/demo.html"
container = "html.parser"


def foreachHtmlTagTree():
    try:
        r = requests.get(url)
        print(r.status_code)
        r.raise_for_status()
        demo = r.text
        print(demo)
        print("--------------------")
        soup = BeautifulSoup(demo, container)
        print(soup.prettify())
        print("--------------------")
        # 打印head标签
        print(soup.head)

        # 3种遍历方式:
        # 1. 下行遍历: 根节点->叶子节点
        # 2. 上行遍历: 叶子节点->根节点
        # 3. 平行遍历: 兄弟节点之间相互遍历

        # 1. 下行遍历 contents children descendants
        # 打印head标签的儿子节点 (因为返回的类型是一个列表，所以可以用列表的方式对返回的数据进行检索)
        print(soup.head.contents)
        # 打印body标签的儿子节点 (因为返回的类型是一个列表，所以可以用列表的方式对返回的数据进行检索)
        # 注意: 对于一个标签的儿子节点并不仅仅包括标签节点，也包括字符串节点，比如像\n也是一个body标签的儿子标签类型
        print(soup.body.contents)
        # 获取body儿子节点的数量
        print(len(soup.body.contents))
        # 检索列表中的索引为1的(也就是第2个)标签
        print(soup.body.contents[1])

        print("--------------------")
        # 2. 上行遍历 parent parents
        # 打印title标签的父亲标签
        print(soup.title.parent)
        # 打印html标签的父亲标签
        print(soup.html.parent)
        # soup本身也是一种特殊的标签，打印它的父标签 (为None，说明soup的父标签为空)
        print(soup.parent)
        print("--------------------")
        # 标签树的上行遍历
        for parent in soup.a.parents:
            if parent is None:
                print(parent)
            else:
                print(parent.name)

        # 3. 平行遍历(同一个父亲节点下的兄弟节点才可以平行遍历)
        # next_sibling  previous_sibling  next_siblings  previous_siblings
        # 获取到的a标签的下一个平行标签，不一定是标签，可能是一个navigableString类型
        print(soup.a.next_sibling)
        print(soup.a.next_sibling.next_sibling)
        print(soup.a.previous_sibling)
        print(soup.a.previous_sibling.previous_sibling)

        print("--------------------")
        # 遍历后续节点
        for sibling in soup.a.next_sibling:
            print(sibling)
        # 遍历前续节点
        for sibling in soup.a.previous_sibling:
            print(sibling)

        print("--------------------")
        # 美化显示
        print(soup.prettify())

    except:
        print("爬取失败")


if __name__ == "__main__":
    foreachHtmlTagTree()
