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

    # 默认解析 用xPath
    def parse(self, response):
        ## xpath解析 最外层需要// ->里面就可以用/ 不然可能存在解析问题
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i in movie_list:
            # 遍历数据 放入节点中
            douban_item = ScrapyDemoItem()
            # 当前目录下    xpath 前面+.

            # 序号
            douban_item['movie_num'] = i.xpath(".//div[@class='item']//em/text()").extract_first()
            # 电影名称
            douban_item['movie_name'] = i.xpath(
                ".//div[@class='item']//div[@class='hd']/a//span[1]/text()").extract_first()

            # 电影简介 多行数据处理
            content = i.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                douban_item['introduce'] = "".join(i_content.split())

            # 星级
            douban_item['star'] = i.xpath(".//span[@class='rating_num']/text()").extract_first()

            # 评论
            douban_item['evaluate'] = i.xpath(".//div[@class='star']/span[4]/text()").extract_first()

            # 描述
            douban_item['describe'] = i.xpath(".//p[@class='quote']/span/text()").extract_first()
            # 传输数据进入管道
            yield douban_item
        # 下一页
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            # 提交管道进行 下一页处理
            yield scrapy.Request("http://movie.douban.com/top250" + next_link, callback=self.parse)
