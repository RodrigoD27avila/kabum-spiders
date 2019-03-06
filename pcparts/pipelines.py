# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

from datetime import datetime

class GenericPipeline(object):
    def process_item(self, item, spider):
        item['date'] = datetime.utcnow().strftime("%Y/%m/%d")
        return item
        

class IsAvaliable(object):
    def process_item(self, item, spider):
        if item['avaliable']:
            return item
        else:
            DropItem()
