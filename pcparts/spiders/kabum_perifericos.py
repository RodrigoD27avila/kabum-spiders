# -*- coding: utf-8 -*-
import scrapy
from pcparts.items import GenericItem, GenericLoader


class KabumPerifericosSpider(scrapy.Spider):
    mouse_teclado = [
        'mouse-gamer',
        'teclado-gamer',

    ]
    name = 'kabum_perifericos'
    allowed_domains = ['https://www.kabum.com.br/perifericos']
    start_urls_0    = ['https://www.kabum.com.br/perifericos/teclado-mouse/{0}?ordem=5&limite=100&pagina=1&string='.format(x) for x in mouse_teclado]
    start_urls_1    = ['https://www.kabum.com.br/perifericos/som-acessorios/headphone-game?ordem=5&limite=100&pagina=1&string=',
        	           'https://www.kabum.com.br/computadores/monitores?ordem=5&limite=100&pagina=1&string=']\

    start_urls = start_urls_0 + start_urls_1


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