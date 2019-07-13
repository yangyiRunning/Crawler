import requests


def searchWord():
    try:
        kv = {'wd', 'python'}
        r = requests.get("http://www.baidu.com/s", params=kv)
        print(r.headers)
        print(r.status_code)
        print(r.request.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")


if __name__ == "__main__":
    searchWord()