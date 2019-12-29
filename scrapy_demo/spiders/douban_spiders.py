# -*- coding: utf-8 -*-
import scrapy
# 导入item抓取的节点信息
from scrapy_demo.items import ScrapyDemoItem

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

    # 解析 用xPath
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i in movie_list:
            # 遍历数据 放入节点中
            douban_item = ScrapyDemoItem()
            # 当前目录下    xpath 前面+.
            douban_item['movie_num'] = i.xpath("./div[@class='item']//em/text()").extract_first()
            print(douban_item["movie_num"])
