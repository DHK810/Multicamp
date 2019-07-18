# -*- coding: utf-8 -*-
import scrapy

class MaratangSpider(scrapy.Spider):
    name = 'maratang1'
    allowed_domains = ['naver.com'] 
    start_urls = ['https://search.naver.com/search.naver?date_from=20190711&date_option=8&date_to=20190711&dup_remove=1&nso=so%3Add%2Cp%3Afrom20190711to20190711&post_blogurl=&post_blogurl_without=&query=%EB%A7%88%EB%9D%BC%ED%83%95&sm=tab_pge&srchby=all&st=date&where=post&start=1',
    'https://search.naver.com/search.naver?date_from=20190711&date_option=8&date_to=20190711&dup_remove=1&nso=so%3Add%2Cp%3Afrom20190711to20190711&post_blogurl=&post_blogurl_without=&query=%EB%A7%88%EB%9D%BC%ED%83%95&sm=tab_pge&srchby=all&st=date&where=post&start=11',
    'https://search.naver.com/search.naver?date_from=20190711&date_option=8&date_to=20190711&dup_remove=1&nso=so%3Add%2Cp%3Afrom20190711to20190711&post_blogurl=&post_blogurl_without=&query=%EB%A7%88%EB%9D%BC%ED%83%95&sm=tab_pge&srchby=all&st=date&where=post&start=21']
    #start_urls들을 하나하나 시작

    def parse(self, response):
        for href in response.xpath("//ul[@class='type01']/li/dl/dt/a/@href").extract() :
            print(href)
            yield response.follow(href, self.parse_iframe) #주소 들어간 후에 parse_iframe 함수를 실행

    def parse_iframe(self, response):    
        iframe_url = response.xpath("//iframe/@src").get()
        if iframe_url != None :
            href = 'https://blog.naver.com' + response.xpath("//iframe/@src").get()
            yield response.follow(href, self.parse_details)

    def parse_details(self, response):   
        yield {
            'url' : response.url   # response 에는 html 태그들을 가지고 있다. 태그 호출만 해주면 알아서 반환해줌
        }