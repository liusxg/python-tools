'''
author: liusxg
env: python:3.6.2
description: 下载指定知乎页面图片，默认下载原图
'''

from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

RAW_PIC_ATTRS = 'data-original'
IMG_TAG = 'img'
GET_WEB_ERRO = '获取网页失败'
SUCCESS_CODE = [200]

class DownloadImg:

    def getWebText(self, webUrl):

        # 注意这里如果使用requests.get 需要设置ua，否则请求会出现400错误
        res = urlopen(webUrl)

        if res.code not in SUCCESS_CODE:
            raise Exception()

        return BeautifulSoup(res.read())

    #默认获取原图链接
    def extraImageTag(self, bsObj):
        imgArray = bsObj.find_all(name=IMG_TAG)
        imgLinkArr = []

        for img in imgArray:

            if RAW_PIC_ATTRS in img.attrs:
                imgLinkArr.append(img.attrs[RAW_PIC_ATTRS])

        return imgLinkArr

    def downloadImg(self, imgUrls, localPath):
        print("开始下载图片...")
        for imgUrl in imgUrls:
            imgName = imgUrl.split('/')[-1]
            urlretrieve(url=imgUrl, filename=localPath + "/" + imgName, reporthook=self.completeReport(imgUrl))

        print("所有图片下载完成...")

    def completeReport(self, url):
        print(url + " 下载完成。")

if __name__ == '__main__':

    webUrl = '知乎回答路径，比如：https://www.zhihu.com/question/332004102/answer/783562516'
    localPath = '本地目录'
    # webUrl = 'https://www.baidu.com/'
    dp = DownloadImg()
    bsObj = dp.getWebText(webUrl=webUrl)
    imgArray = dp.extraImageTag(bsObj)
    dp.downloadImg(imgArray, localPath)


