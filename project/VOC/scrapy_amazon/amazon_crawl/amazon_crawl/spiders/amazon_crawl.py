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
url_format = "https://www.amazon.com/s?k={0}&page={1}"

base_url = "www.amazon.com"

class amazon_crawlSpider(scrapy.Spider):
    
    name = 'amazon_crawl'
    allowed_domains = ['amazon.com']
    
    start_urls = []
    


    for i in range(1,4):
        
        start_urls.append(url_format.format(keyword, str(i)))

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, self.parse)

    #digital camera 입력했을 때 사이트
    def parse(self, response):

        for href in response.xpath("//a[@class='a-link-normal a-text-normal']/@href").extract() :
            print('href = ', href)
            yield response.follow(href, self.parse_product)
            
    #하나의 프로덕트 선택된 화면
    def parse_product(self, response):  
        if response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").get() is not None:
            url = response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").get()
            print('------------------------------------------', url)
            yield response.follow(url, self.parse_reviews)
        
            
    
    # 리뷰전체보기 버튼 클릭하기
    def parse_reviews(self, response):
        item = AmazonCrawlItem()
        item['review'] = response.xpath("//div[@class= 'card-padding']/div[2]/div[2]/div/div").extract()
        yield item


        # item['product_name'] = str(response.xpath('//a[@data-hook="product-link"]/text()').get())
        # item['reviewDate'] = response.xpath("//span[@class = 'a-size-base a-color-secondary review-date']/text()").get()
        # item['score'] = response.xpath("//span[@class = 'a-icon-alt']/text()").get().split()[0]    

    # 마지막 review 사이트

    # def parse_reviews_detail(self, response):
    #     item = AmazonCrawlItem()
    #     item['review'] = str(response.xpath("//span[@class='a-size-base review-text review-text-content']/text()").get())
    #     item['product_name'] = str(response.xpath('//a[@data-hook="product-link"]/text()').get())
    #     item['reviewDate'] = response.xpath("//span[@class = 'a-size-base a-color-secondary review-date']/text()").get()
    #     item['score'] = response.xpath("//span[@class = 'a-icon-alt']/text()").get().split()[0]
        
    #     item['product_name'] = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', item['product_name'].replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').replace('\\n','').replace('\\r', '').replace('\\t','').strip()))       
    #     item['review'] = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', item['review'].replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').replace('\\n','').replace('\\r', '').replace('\\t','').strip()))
    #     yield item
    
    #     if response.xpath("//ul[class='a-pagination']/a/@href").get() is not None:
    #         next_page = response.xpath("//ul[class='a-pagination']/a/@href").get()
    #         yield response.Request(next_page, self.parse_reviews)


# # -*- coding: utf-8 -*-
# import re
# import scrapy
# from amazon_crawl.items import AmazonCrawlItem
# from datetime import timedelta, date
# from urllib import parse
# import time
# import random
# from time import sleep

# keyword = "digital+camera"
# url_format = "https://www.amazon.com/s?k={0}&page={1}"

# base_url = "www.amazon.com"

# class amazon_crawlSpider(scrapy.Spider):
    
#     name = 'amazon_crawl'
#     allowed_domains = ['amazon.com']
    
#     start_urls = []
    


#     for i in range(1,10):
        
#         start_urls.append(url_format.format(keyword, str(i)))

#     def start_requests(self):
#         for u in self.start_urls:
#             yield scrapy.Request(u, self.parse)

#     def parse(self, response):
#         for href in response.xpath("//a[@class='a-link-normal a-text-normal']/@href").extract() :
            
            

#             yield response.follow(href, self.parse_product)
            

#     def parse_product(self, response):  
  
#         if response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").get() is not  None:
#             review_url = response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").get()

#             yield response.follow(review_url, self.parse_reviews)

#     def parse_reviews(self,response):
#         item = AmazonCrawlItem()
#         item['review'] = str(response.xpath("//div[@class='a-section review aok-relative']").extract())
#         item['product_name'] = str(response.xpath('//a[@data-hook="product-link"]/text()').get())

#         item['product_name'] = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', item['product_name'].replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').replace('\\n','').replace('\\r', '').replace('\\t','').strip()))       
#         item['review'] = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', item['review'].replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').replace('\\n','').replace('\\r', '').replace('\\t','').strip()))
#         if response.xpath("//ul[class='a-pagination']/a/@href").get() is not None:
#             yield response.follow(response, callback=self.parse_reviews)
#         yield item