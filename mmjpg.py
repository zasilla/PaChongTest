
import requests
import re
import os
from PIL import Image
from io import BytesIO

url='http://www.mmjpg.com/mm'
res=requests.get(url)
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "http://www.mmjpg.com/", "Connection": "close"}
for i in range(1,1576):
    res=requests.get(url+'/'+str(i))
    res.encoding = 'utf-8'
    img_url=re.findall(r'data-img="(.*?)" alt',res.text)
    page_numbers=re.findall(r'</i><a href="/mm/(.*?)</a><em class=',res.text)
    page_numbers=int(page_numbers[0].split('>')[1])
    title=re.findall(r'<h2>(.*?)</h2>',res.text)

    #print ('downloading pakge '+str(i)+' url is'+img_url[0])

    img_dir = os.getcwd() + "\mmimages\\" + title[0]
    if os.path.exists(img_dir):
        pass
    else:
        os.makedirs(img_dir)

    for j in range(1,page_numbers+1):
        res2 = requests.get(url + '/' + str(i)+'/'+str(j))
        img_url = re.findall(r'data-img="(.*?)" a', res2.text)
        # print (img_url[0])
        ress=requests.get(img_url[0], headers = burp0_headers)
        # print ress.text
        imge_file = open(img_dir + "\\" + str(j) + '.jpg', 'wb')
        imge_file.write(ress.content)
        imge_file.close()
        print(img_url[0] + "保存成功")
