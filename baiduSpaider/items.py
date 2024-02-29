# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduspaiderItem(scrapy.Item):
    imgurl = scrapy.Field()  # 图片地址
    imgname = scrapy.Field()  # 图片索引
