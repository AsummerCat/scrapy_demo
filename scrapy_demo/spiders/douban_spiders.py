# -*- coding: utf-8 -*-
import scrapy

'''
爬虫文件

'''


class DoubanSpidersSpider(scrapy.Spider):
    # 爬虫名称
    name = 'douban_spiders'
    # 允许的域名 爬虫
    allowed_domains = ['movie.douban.com']
    # 入口url,扔到调度器
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        print("请求成功")

