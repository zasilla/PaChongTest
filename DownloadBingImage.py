import json
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import os
import re


def get_page_detail(idx):
    data = {
        'format': 'js',
        'idx': idx,
        'n': 7,
        'nc': 1544539643529,
        'pid': 'hp'
    }
    url = 'https://cn.bing.com/HPImageArchive.aspx?' + urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None


def pars_page_detail(html):
    data = json.loads(html)
    for item in data.get('images'):
        image_url = "https://cn.bing.com" + item.get('url')
        yield image_url


def download_img(url):
    #检查文件夹路径是否存在，不存在的话创建文件夹，否则跳过
    img_dir = os.getcwd() + "\images\\"
    if os.path.exists(img_dir):
        pass
    else:
        os.mkdir(img_dir)
    image_name = re.findall(r'/([^/]+)$', url)
    #检查文件是否存在，如果存在则跳过
    if not os.path.exists(img_dir + image_name[0]):
        with open(img_dir + image_name[0], "wb") as f:
            try:
                conn = requests.get(url)
            except RequestException:
                print(url)
                print("请重新下载")
            f.write(conn.content)
            f.close()
            print(url, "保存成功")
    else:
        print(image_name[0] + "已经下载")


def main():
    for idx in range(7):
        html = get_page_detail(idx)
        for url in pars_page_detail(html):
            download_img(url)



if __name__ == '__main__':
    main()
