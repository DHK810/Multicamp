# -*- coding: utf-8 -*-
 
# Importing Scrapy Library
import scrapy
from amazon_crawl.items import AmazonCrawlItem
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.com']
     
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.com/s?k=digital+camera&pageNumber="
    start_urls=['https://www.amazon.com/s?k=digital+camera&pageNumber=1']
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    #for i in range(1,20):
    #    start_urls.append(myBaseUrl+str(i))

    def parse(self, response):
        for products in response.css('div.s-search-results'):
            ab = products.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").extract()
            for a in ab:
                print('--------------------------', a)
            
            urls = products.xpath("//a[@class='a-link-normal a-text-normal']/@href").extract()
            for url in urls:
                
                yield response.follow(url, self.parse_product)
            #url = products.xpath("//a[@class='a-link-normal a-text-normal']/@href").get()
            #print(url)
            #yield scrapy.Request(url, self.parse_product)

    def parse_product(self, response):
        #title은 과정 확인용
        #title = response.xpath("//span[@id='productTitle']/text()").extract()
        #print(title)
        review_url = response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").extract_first()
        yield response.follow(review_url, self.parse_reviews)

    def parse_reviews(self, response):
        item = AmazonCrawlItem()
        #리뷰 전체를 씌운 프레임 찾기 # = id
        data = response.css('#cm_cr-review_list')
        product_title = response.css('.product-title') 

        #data 전체 덩어리에서 star_rating, comments, user, review_date를 가져왔다.
        #내가 원하는 건: 반복을 통해 한번에 star_Rating comments, user, review_date를 가져오고 싶다.
        for a in data.css('div.aok-relative'):
            print('----------------', a)
            item['score'] = a.css("span.a-icon-alt::text").extract() 
            
            item['product_name'] = ''.join(product_title.xpath('.//text()').extract())
            item['review_date'] = a.css("span.review-date::text").extract()
            
            item['user'] = a.css("span.a-profile-name::text").extract()
            
            item['review'] = a.css("span.review-text-content>span::text").extract()
            
            yield item

        #참고용 코드
        #product_title = response.css('.product-title')  

        ## Collecting product star ratings
        ## . = class, data안에서 클래스에 review_rating이 들어간 태그 찾기.
        ## Collecting user reviews
        #star_rating = data.css('.review-rating')    
        #comments = data.css('.review-text-content')
        #user = data.css('.a-profile-name')
        #review_date = data.css('.review-date') 
        ##Combining the results
        #for review in star_rating:
        #    item['score'] = ''.join(review.xpath('.//text()').extract_first())        
        #    item['product_name'] = ''.join(product_title.xpath('.//text()').extract())
        #    item['review_date'] = review_date.xpath('.//text()').extract()         
        #    item['user'] = user.xpath('.//text()').extract()        
        #    item['review'] = ''.join(comments.xpath(".//text()").extract())
        
        #yield item