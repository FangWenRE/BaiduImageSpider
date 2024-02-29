import scrapy
from baiduSpaider.items import *
import json


class BaiduSpider(scrapy.Spider):
    name = 'baiduSpaider'
    allowed_domains = ['image.baidu.com/']


    def __init__(self):
        self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&' \
                   'logid=11620454687379829430&ipn=rj&ct=201326592&is=&fp=result&fr=&word={0}&' \
                   'queryWord={0}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&' \
                   'copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&' \
                   'pn={1}&rn=30&gsm=b4000000000000b4&1666401445687='
        self.index = 0 # 图片序号

        self.pag_num = 40 # 爬取的页数，每页30张图片

    def start_requests(self):
        for p in range(1, self.pag_num):
            page = p * 30
            url = self.url.format('教室举手',page)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = BaiduspaiderItem()

        # 对不符合要求的进行异常处理
        try:
            rs = json.loads(response.text)
        except Exception as e:
            return

        # 对图片地址定位对一些变量初始化
        datas = rs['data']
        datas.pop()
        image_url_list = []
        index_list = []


        # 提取图片地址，存储到管道，并返回
        for index, data in enumerate(datas):
            try:
                obj_url = data['replaceUrl'][0]['ObjURL']
            except KeyError:
                continue

            if len(obj_url) > 50:
                print(self.index, obj_url)
                image_url_list.append(obj_url)
                self.index += 1
                index_list.append(self.index)

        item['imgurl'] = image_url_list
        item['imgname'] = index_list
        yield item