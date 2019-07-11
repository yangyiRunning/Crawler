import requests

r = requests.get("https://92.91p22.space/v.php?category=mf&viewtype=basic&page=53")
print(r.status_code)
r.encoding = "utf-8"
print(r.text)
