import scrapy

class ClerkSpider(scrapy.Spider):
    name = 'clerk'
    allowed_domains = []
    start_url = []

    def parse(self,response):
        link = response.xpath().extract()