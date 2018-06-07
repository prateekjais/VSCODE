# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from wiki.items import WikiItem


class SpidySpider(scrapy.Spider):
    name = 'spidy'
    allowed_domains = ['https://en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_constituencies_of_the_Lok_Sabha']

    def parse(self, response):
        rowlist = Selector(response).xpath('//table[@class="wikitable sortable"]')[0].xpath('tr/td/text()')
        for i in range (0,len(rowlist),2) :
            item = WikiItem()          
            item['state'] = rowlist[i].extract().strip()                    
            item['no_of_seats'] = rowlist[i+1].extract().strip() 
            yield item    
        
      
