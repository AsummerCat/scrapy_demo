# -*- coding: utf-8 -*-
import scrapy


class DoubanSpidersSpider(scrapy.Spider):
    name = 'douban_spiders'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        # 需要抓取的逻辑
        movie_num = scrapy.Field()  # 序号
        introduce = scrapy.Field()  # 电影介绍
        star = scrapy.Field()  # 星级
        evaluate = scrapy.Field()  # 评论
        describe = scrapy.Field()  # 描述
