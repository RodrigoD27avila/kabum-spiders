# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def _clenaup_name(name):
    return name.replace('\s+', ' ')

def _kabum_avaliable(href):
    return not (href == '#')

def _price_to_float(price):
    strprice = price.replace('R$', '').replace('.', '').replace(',', '.').strip()
    return float(strprice)

class GenericLoader(scrapy.loader.ItemLoader):
    default_output_processor = TakeFirst()

class GenericItem(scrapy.Item):
    name              = scrapy.Field(input_processor=MapCompose(_clenaup_name))
    price_cache       = scrapy.Field(input_processor=MapCompose(_price_to_float))
    price_installment = scrapy.Field(input_processor=MapCompose(_price_to_float))
    link              = scrapy.Field()
    avaliable         = scrapy.Field(input_processor=MapCompose(_kabum_avaliable))
    date              = scrapy.Field()


    