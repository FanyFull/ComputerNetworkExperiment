import requests

myUrl = 'https://ip.useragentinfo.com/json?ip'
ip = '40.79.150.121'
myUrl += ip
r = requests.get(myUrl)
print(r.json())
