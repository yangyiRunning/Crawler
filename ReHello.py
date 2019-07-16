# 正则表达式的使用

# 正则表达式的表示类型

# raw string 类型(原生字符串类型)，即不包含转义符的字符串
# string类型，普通的string类型

import re


def searchPostCard():
    try:
        match = re.search(r"[1-9]\d{5}", "BIT 100081")
        if match:
            print(match.group(0))

        print("-----------------")
        match = re.match(r"[1-9]\d{5}", "100081 BIT")
        if match:
            print(match.group(0))

        print("-----------------")
        ls1 = re.findall(r"[1-9]\d{5}", "BIT100081 TSU100084")
        print(ls1)

        print("-----------------")
        ls2 = re.split(r"[1-9]\d{5}", "BIT100081 TSU100084")
        print(ls2)

        # maxsplit 最大分割数，用户可以约定将字符串分割出多少部分，超过这个最大分割数的部分全部返回
        print("-----------------")
        ls3 = re.split(r"[1-9]\d{5}", "BIT100081 TSU100084", maxsplit=1)
        print(ls3)

        print("-----------------")
        match2 = re.finditer(r"[1-9]\d{5}", "BIT100081 TSU100084")
        for m in match2:
            if m:
                print(m.group(0))

        print("-----------------")
        ls4 = re.sub(r"[1-9]\d{5}", ":zipcode", "BIT100081 TSU100084")
        print(ls4)

    except:
        print("出现异常")


if __name__ == "__main__":
    searchPostCard()
