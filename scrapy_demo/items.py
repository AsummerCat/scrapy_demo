# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
抓取的节点信息
'''


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # # 需要抓取的逻辑
    movie_num = scrapy.Field()  # 序号
    movie_name = scrapy.Field()  # 电影名称
    introduce = scrapy.Field()  # 电影介绍
    star = scrapy.Field()  # 星级
    evaluate = scrapy.Field()  # 评论
    describe = scrapy.Field()  # 描述
    pass
