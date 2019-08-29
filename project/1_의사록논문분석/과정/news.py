# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.einfomax.co.kr']
    start_urls = []
    for i in range(1,5):
        urls=f'http://news.einfomax.co.kr/news/articleList.html?page={i}&sc_area=A&view_type=sm&sc_word=%EA%B8%88%EB%A6%AC'
        start_urls.append(urls)
    
    print (start_urls)
    def parse(self, response):
        
        for block in response.css('div.list-block'):
            url='http://news.einfomax.co.kr'+str(block.css('div.list-titles a::attr(href)').get())
            yield response.follow(url, self.parse_text)

    def parse_text(self, response):
        title=response.css('div.article-head-title::text').get()
        date_raw = response.css('div.info-text ul li').getall()[1]
        idx=date_raw.find('승인')
        date=date_raw[idx:]
        date=date.split()[1]

        text_raw = response.css('div#article-view-content-div::text').extract()

        text=''
        for t in text_raw:
            if t.find('(끝)') != -1 :
                break
            
            t=t.replace('\r','')
            t=t.replace('\t','')
            t=t.replace('\n','')
            text+=t

        yield {
            'date' : date,
            'title' : title,
            'text' : text,
            'url' : response.url
            }
        
