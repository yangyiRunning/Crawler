import requests


def getDangForce(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        print(r.request.header)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")


if __name__ == "__main__":
    print(getDangForce("https://www.baidu.com"))
