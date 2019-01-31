# -*- coding:UTF-8 -*-
import json
import time
from contextlib import closing

import requests


class get_photos(object):
    def __init__(self):
        self.photos_id = []
        self.download_server = 'https://unsplash.com/photos/xxxxxyyyyy/download?force=trues'
        self.target = 'http://unsplash.com/napi/feeds/home'
        self.headers = {'authorization': 'Client-ID 16572e62-637c-4a91-a0c3-2020ca981435'}

    def get_ids(self):
        req = requests.get(url=self.target, headers=self.headers, verify=False)
        html = json.loads(req.text)
        next_page = html['next_page']
        for each in html['photos']:
            self.photos_id.append(each['id'])
        time.sleep(1)
        for i in range(5):
            req = requests.get(url=next_page, headers=self.headers, verify=False)
            html = json.loads(req.text)
            next_page = html['next_page']
            for each in html['photos']:
                self.photos_id.append(each['id'])
            time.sleep(1)

    def download(self, photo_id, filename):

        target = self.download_server.replace('xxxxxyyyyy', photo_id)
        with closing(requests.get(url=target, stream=True, headers=self.headers, verify=False, )) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = get_photos()
    print('获取图片连接中:')
    gp.get_ids()
    print('图片下载中:')
    for i in range(len(gp.photos_id)):
        print('  正在下载第%d张图片' % (i + 1))
        gp.download(gp.photos_id[i], (i + 1))
