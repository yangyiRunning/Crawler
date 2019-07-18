# 正则表达式的使用

# 正则表达式的表示类型

# raw string 类型(原生字符串类型)，即不包含转义符的字符串
# string类型，普通的string类型

# re库默认采用贪婪匹配的方式，即输出匹配最长的子串
import re


def searchPostCard():
    try:
        # 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
        # regex = re.compile(r"[1-9]\d{5}")
        # print(regex.search("BIT 100081"))
        match = re.search(r"[1-9]\d{5}", "BIT 100081")
        if match:
            # 获得匹配后的字符串
            print(match.group(0))
            # 匹配字符串在原始字符串中的开始位置
            print(match.start())
            # 匹配字符串在原始字符串中的结束位置
            print(match.end())
            # 返回(.start() .end())的元组类型
            print(match.span())
        # 查看match对象的类型
        print(type(match))
        # 4个属性
        # 1. 待匹配的文本
        print(match.string)
        # 2. 匹配时使用的pattern对象(正则表达式)  真正经过compile的才算是一个真正意义上的正则表达式
        print(match.re)
        # 3. 正则表达式搜索文本的开始位置
        print(match.pos)
        # 4. 正则表达式搜索文本的结束位置
        print(match.endpos)

        print("-----------------")
        # 从一个字符串的开始位置起匹配正则表达式，返回match对象
        match = re.match(r"[1-9]\d{5}", "100081 BIT")
        if match:
            print(match.group(0))

        print("-----------------")
        # 搜索字符串，以列表类型返回全部能匹配的子串
        ls1 = re.findall(r"[1-9]\d{5}", "BIT100081 TSU100084")
        print(ls1)

        print("-----------------")
        # 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
        ls2 = re.split(r"[1-9]\d{5}", "BIT100081 TSU100084")
        print(ls2)

        # maxsplit 最大分割数，用户可以约定将字符串分割出多少部分，超过这个最大分割数的部分全部返回
        print("-----------------")
        ls3 = re.split(r"[1-9]\d{5}", "BIT100081 TSU100084", maxsplit=1)
        print(ls3)

        print("-----------------")
        # 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
        match2 = re.finditer(r"[1-9]\d{5}", "BIT100081 TSU100084")
        for m in match2:
            if m:
                print(m.group(0))

        print("-----------------")
        # 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
        ls4 = re.sub(r"[1-9]\d{5}", ":zipcode", "BIT100081 TSU100084")
        print(ls4)

    except:
        print("出现异常")


if __name__ == "__main__":
    searchPostCard()
