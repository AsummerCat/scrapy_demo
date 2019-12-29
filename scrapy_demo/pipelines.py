# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


'''
管道获取爬到的数据处理
例如: 保存数据库 或者文件

需要开启settings.py 的 ITEM_PIPELINES

'''


class ScrapyDemoPipeline(object):
    def process_item(self, item, spider):
        data = dict(item)
        print("输出-------------------------")
        print(item["describe"])
        return item
