import scrapy

from scrapy.crawler import CrawlerProcess


class MyCrawler(scrapy.Spider):


    name = 'DAUM CRAWLER'
    start_urls = ['http://www.daum.net']


    def parse(self, response):
        t = response.css("#realTimeSearchWord >li >div >div >span >a >strong::text").extract()
        x = response.css("#realTimeSearchWord >li >div >div >span >a::attr(href)").extract()

        total_href = []
        total_text = []

        temp_text = []
        real_total = []


        for i, go in enumerate(x):
            if i %2 == 0:
                total_href.append(go)

        for i, temp in enumerate(t):
            if i%2 ==0:
                total_text.append(t)
            break

        total_text[0] = t[0]
        k = response.css("#realTimeSearchWord >li >div >div >span >a::text").extract()

        for i, text in enumerate(k):
            if i !=0 and i%2 == 0:
                temp_text.append(text)


        real_total == zip(temp_text,total_href)



        for i in range(11):
            if i==0:
                print total_text[0] + ' ' + total_href[0]
            else:
                print temp_text[i] + ' ' + total_href[i]


        real_total = zip(total_href,total_text)
        for total_href, total_text in real_total:
            print total_text, total_href


        for i in range(10):
            print total_text[i]


pass


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()
