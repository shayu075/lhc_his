# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from lhc_his.spiders.tools import deal_tr
from lhc_his.items import LhcHisItem


class HisSpider(scrapy.Spider):
    name = 'his'
    allowed_domains = ['www.kj5588.com/']
    start_urls = ['http://www.kj5588.com/history/']

    def parse(self, response):
        # 开奖日期
        yield Request(url='http://www.kj5588.com/rq/', callback=self.insert_newest, dont_filter=True)
        # 开奖信息
        yield Request(url='http://www.kj5588.com/history/2019.html', callback=self.update_newest, dont_filter=True)

    def parse_detail(self, response):
        item_tr = response.css('.infolist')
        for x in item_tr:
            yield deal_tr(x)

    def insert_newest(self, response):
        x = response.css('h1::text').extract_first()
        qs = x[2:5]
        year = x[11:15]
        month = x[16:18]
        day = x[19:21]
        lhc_item = LhcHisItem()
        lhc_item['qs'] = qs
        lhc_item['id'] = year + month + day + qs
        lhc_item['year'] = year
        lhc_item['month'] = month
        lhc_item['day'] = day
        for i in range(6):
            lhc_item['pm' + str(i + 1)] = ''
            lhc_item['p' + str(i + 1) + '_sx'] = ''
        lhc_item['tm'] = ''
        lhc_item['sx'] = ''
        lhc_item['ds'] = ''
        lhc_item['bs'] = ''
        lhc_item['dx'] = ''
        lhc_item['wx'] = ''
        lhc_item['tt'] = ''
        lhc_item['ws'] = ''
        lhc_item['hds'] = ''
        lhc_item['jy'] = ''
        lhc_item['ms'] = ''
        lhc_item['dw'] = ''
        lhc_item['yy'] = ''
        lhc_item['td'] = ''
        lhc_item['jx'] = ''
        lhc_item['hb'] = ''
        lhc_item['sex'] = ''
        lhc_item['bh'] = ''
        lhc_item['nn'] = ''
        lhc_item['zhds'] = ''
        yield lhc_item

    def update_newest(self, response):
        x = response.css('.infolist')[1]
        yield deal_tr(x)

