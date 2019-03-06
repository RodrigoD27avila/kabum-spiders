# -*- coding: utf-8 -*-
import scrapy
from pcparts.items import GenericItem, GenericLoader


class KabumHardwareSpider(scrapy.Spider):
    hardware = [
        'processadores',
        'placa-de-video-vga',
        'ssd-2-5',
        'placas-mae',
        'memoria-ram',
        'fontes',
        'disco-rigido-hd'

    ]
    name = 'kabum_hardware'
    allowed_domains = ['https://www.kabum.com.br/hardware']
    start_urls      = ['https://www.kabum.com.br/hardware/{0}?ordem=5&limite=100&pagina=1&string='.format(x) for x in hardware]

    def parse(self, response):
        search_result = response.css('.listagem-box')
        for selector in search_result:
            item = GenericLoader(item=GenericItem(), selector=selector)
            item.add_css('name', '.H-titulo > a::text')
            item.add_css('link', '.H-titulo > a::attr(href)')
            item.add_css('price_cache', '.listagem-preco::text')
            item.add_css('price_installment', '.listagem-precoavista > b::text')
            item.add_css('avaliable', '.listagem-bots > div > a::attr(href)')
            yield item.load_item()