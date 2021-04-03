import scrapy

class RedditSpider(scrapy.Spider):
    name = "reddit"
    start_urls = ['https://www.reddit.com/']

    def parse(self, response):
        for title in response.css('h3'):

            yield {
                'title': title.css('::text').extract()
            }
