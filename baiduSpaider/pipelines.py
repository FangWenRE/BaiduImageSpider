# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline, FilesPipeline
from scrapy import Request

# 继承ImagesPipeline，重写相关方法
class BaiduspaiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # Request meta传参：图片信息
        # 这里注意，如果item['imgurl']的value是字符串直接yild即可，列表需要循环！
        names = item['imgname']
        for index, item in enumerate(item['imgurl']):
            name = names[index]
            yield Request(url=item, meta={'name': name})

    def file_path(self, request, response=None, info=None):
        name = request.meta['name']  # 获取图片的名字
        filename = u'baiu_{0}.jpg'.format(name)  # 自定义图片名称
        return filename
