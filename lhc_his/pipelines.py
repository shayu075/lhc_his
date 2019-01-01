# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi


class LhcHisPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            port=settings["MYSQL_PORT"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWD"],
            db=settings["MYSQL_DB"],
            use_unicode=True,
            charset="utf8",
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)

    def handle_error(self, failure):
        print(failure)

    def do_insert(self, cursor, item):
        # 更新操作
        find_sql = 'select id from lhc_result_record where id = %s'
        find_result = cursor.execute(find_sql, item['id'])
        if find_result > 0:
            update_sql = '''UPDATE lhc_result_record SET pm1 = %s, p1_sx = %s, pm2 = %s, p2_sx = %s, pm3 = %s, 
            p3_sx = %s, pm4 = %s, p4_sx = %s, pm5 = %s, p5_sx = %s, pm6 = %s, p6_sx = %s, tm = %s, sx = %s, ds = %s, 
            bs = %s, dx = %s, wx = %s, tt = %s, ws = %s, hds = %s, jy = %s, ms = %s, dw = %s, yy = %s, td = %s, jx = %s, 
            hb = %s, sex = %s, bh = %s, nn = %s, zhds = %s WHERE id = %s'''
            cursor.execute(update_sql, (item['pm1'], item['p1_sx'], item['pm2'],
                                        item['p2_sx'], item['pm3'], item['p3_sx'], item['pm4'],
                                        item['p4_sx'], item['pm5'], item['p5_sx'], item['pm6'],
                                        item['p6_sx'], item['tm'], item['sx'], item['ds'],
                                        item['bs'], item['dx'], item['wx'], item['tt'], item['ws'],
                                        item['hds'], item['jy'], item['ms'], item['dw'], item['yy'],
                                        item['td'], item['jx'], item['hb'], item['sex'], item['bh'],
                                        item['nn'], item['zhds'], item['id']))
        else:
            insert_sql = '''INSERT INTO lhc_result_record(id, year, month, day, qs, pm1, p1_sx, pm2, 
                         p2_sx, pm3, p3_sx, pm4, p4_sx, pm5, p5_sx, pm6, p6_sx, tm, sx, ds, bs, dx,
                         wx, tt, ws, hds, jy, ms, dw, yy, td, jx, hb, sex, bh, nn, zhds)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                    ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(insert_sql, (item['id'], item['year'], item['month'], item['day'],
                                        item['qs'], item['pm1'], item['p1_sx'], item['pm2'],
                                        item['p2_sx'], item['pm3'], item['p3_sx'], item['pm4'],
                                        item['p4_sx'], item['pm5'], item['p5_sx'], item['pm6'],
                                        item['p6_sx'], item['tm'], item['sx'], item['ds'],
                                        item['bs'], item['dx'], item['wx'], item['tt'], item['ws'],
                                        item['hds'], item['jy'], item['ms'], item['dw'], item['yy'],
                                        item['td'], item['jx'], item['hb'], item['sex'], item['bh'],
                                        item['nn'], item['zhds']))



