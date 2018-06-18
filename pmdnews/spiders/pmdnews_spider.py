import scrapy


class PMDNews(scrapy.Spider):
    name = "pmdnews"

    start_urls = [
        'http://www.pmdnews.lk/archives/'
    ]

    def parse(self, response):
        for article in response.css('article article'):
            yield {
                'title': article.css('h2 a::text').extract_first(),
                'content': article.css('article div.entry-content p::text').extract_first(),
                'link': article.css('h2 a::attr(href)').extract_first()

            }
        
        next_page = response.css('nav')[-2].css('a::attr(href)')[-1].extract()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)