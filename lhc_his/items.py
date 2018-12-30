# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LhcHisItem(scrapy.Item):
    id = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()
    qs = scrapy.Field()
    pm1 = scrapy.Field()
    p1_sx = scrapy.Field()
    pm2 = scrapy.Field()
    p2_sx = scrapy.Field()
    pm3 = scrapy.Field()
    p3_sx = scrapy.Field()
    pm4 = scrapy.Field()
    p4_sx = scrapy.Field()
    pm5 = scrapy.Field()
    p5_sx = scrapy.Field()
    pm6 = scrapy.Field()
    p6_sx = scrapy.Field()
    tm = scrapy.Field()
    sx = scrapy.Field()
    ds = scrapy.Field()
    bs = scrapy.Field()
    dx = scrapy.Field()
    wx = scrapy.Field()
    tt = scrapy.Field()
    ws = scrapy.Field()
    hds = scrapy.Field()
    jy = scrapy.Field()
    ms = scrapy.Field()
    dw = scrapy.Field()
    yy = scrapy.Field()
    td = scrapy.Field()
    jx = scrapy.Field()
    hb = scrapy.Field()
    sex = scrapy.Field()
    bh = scrapy.Field()
    nn = scrapy.Field()
    zhds = scrapy.Field()

