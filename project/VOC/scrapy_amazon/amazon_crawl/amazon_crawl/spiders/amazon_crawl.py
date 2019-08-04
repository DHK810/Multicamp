# -*- coding: utf-8 -*-
import re
import scrapy
from amazon_crawl.items import AmazonCrawlItem
from datetime import timedelta, date
from urllib import parse
import time
import random
from time import sleep



keyword = "digital+camera"
base_url = "www.amazon.com"
url_format = "https://www.amazon.com/s?k=digital+camera&page="

class amazon_crawlSpider(scrapy.Spider):
    
    name = 'amazon_crawl'
    allowed_domains = ['amazon.com']
    


    def start_requests(self):
        for i in range(1,100):

            yield scrapy.Request(url_format + str(i), self.parse)
    def parse(self, response):
        
        for href in response.xpath("//a[@class='a-link-normal a-text-normal']@href").extract() :
            yield response.follow(base_url + href, self.parse_details)

        
        #yield response.follow(url_format.format(keyword, page_no + 1), self.parse)


    def parse_details(self, response):  
        item = AmazonCrawlItem()

        
        item['product_name'] = str(response.xpath("//span[@id = 'productTitle']/text()").get())
        
        item['review'] = str(response.xpath("//div[@class='a-section review aok-relative']").extract())
    
        # title = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', title.replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').replace('\\n','').replace('\\r', '').replace('\\t','').strip()))
        # content = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', content.replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').replace('\\n','').replace('\\r', '').replace('\\t','').strip()))
        
        # item['content'] = content
        # item['title'] = title
        
        yield item
