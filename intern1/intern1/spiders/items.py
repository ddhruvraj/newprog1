# import scrapy
# from scrapy.loader.processors import MapCompose, TakeFirst
# from w3lib.html import remove_tags
#
#
# class JobItem(scrapy.Item):
#     job_text = scrapy.Field(
#         input_processor=MapCompose(remove_tags),
#         output_processor=TakeFirst()
#     )
