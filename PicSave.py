import requests
import os

url = "https://userdisk.webry.biglobe.ne.jp/022/455/23/N000/000/003/151626433501164766179_Z90X-fyqrewi2751167.jpg"
root = "/Users/yangyi/Documents/"
path = root + url.split("/")[-1]


def savePic():
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            print(r.status_code)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")


if __name__ == "__main__":
    savePic()
