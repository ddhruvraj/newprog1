import scrapy
# from intern1.intern1.items import
from scrapy.loader import ItemLoader
list=[]
class jobSpider(scrapy.Spider):
    name = "jobes"

    start_urls = ['https://www.careerguide.com/']

    def parse(self, response, **kwargs):
        for jobs in response.xpath('//div[@class="col-sm-12  col-md-6  col-lg-3 cards-Container nav-workandjob"]'):
            yield {
                'jobs':jobs.xpath('//div[@class="col-sm-12  col-md-6  col-lg-3 cards-Container nav-workandjob"]/div/div/p["\n"]').extract_first()
            }
