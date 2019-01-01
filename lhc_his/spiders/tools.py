from lhc_his.items import LhcHisItem


def deal_tr(x):
    lhc_item = LhcHisItem()
    lhc_td = x.css('td')
    year_month_day = lhc_td[0].css('::text').extract_first().strip().split('-')
    qs = lhc_td[1].css('::text').extract_first().strip().replace('期', '')
    lhc_item['id'] = year_month_day[0] + year_month_day[1] + year_month_day[2] + qs
    lhc_item['year'] = year_month_day[0]
    lhc_item['month'] = year_month_day[1]
    lhc_item['day'] = year_month_day[2]
    lhc_item['qs'] = qs
    pm1_6 = lhc_td[2].css('.p')
    for i in range(6):
        tmp = pm1_6[i].css('div::text').extract()
        lhc_item['pm' + str(i + 1)] = tmp[0].strip()
        lhc_item['p' + str(i + 1) + '_sx'] = tmp[1].strip()
    lhc_item['tm'] = lhc_td[3].css('div[class*=hm]::text').extract_first().strip()
    lhc_item['sx'] = lhc_td[4].css('::text').extract_first().strip()
    lhc_item['ds'] = lhc_td[5].css('::text').extract_first().strip()
    lhc_item['bs'] = lhc_td[6].css('::text').extract_first().strip()
    lhc_item['dx'] = lhc_td[7].css('::text').extract_first().strip()
    # 五行缺位
    yuan_wx = lhc_td[8].css('::text').extract_first().strip()
    wx_bws = 1
    lhc_item['wx'] = '缺'
    if yuan_wx in ('金', '木', '水', '火', '土'):
        wx_bws = 0
        lhc_item['wx'] = yuan_wx
    lhc_item['tt'] = lhc_td[9 - wx_bws].css('::text').extract_first().strip().replace('头', '')
    lhc_item['ws'] = lhc_td[10 - wx_bws].css('::text').extract_first().strip().replace('尾', '')
    hds = lhc_td[11 - wx_bws].css('::text').extract()
    lhc_item['hds'] = hds[0] + hds[1][1]
    lhc_item['jy'] = lhc_td[12 - wx_bws].css('::text').extract_first().strip()
    lhc_item['ms'] = lhc_td[13 - wx_bws].css('::text').extract_first().strip().replace('门', '')
    lhc_item['dw'] = lhc_td[14 - wx_bws].css('::text').extract_first().strip().replace('段', '')
    lhc_item['yy'] = lhc_td[15 - wx_bws].css('::text').extract_first().strip()
    lhc_item['td'] = lhc_td[16 - wx_bws].css('::text').extract_first().strip()
    lhc_item['jx'] = lhc_td[17 - wx_bws].css('::text').extract_first().strip()
    lhc_item['hb'] = lhc_td[18 - wx_bws].css('::text').extract_first().strip()
    lhc_item['sex'] = lhc_td[19 - wx_bws].css('::text').extract_first().strip()
    lhc_item['bh'] = lhc_td[20 - wx_bws].css('::text').extract_first().strip()
    lhc_item['nn'] = lhc_td[21 - wx_bws].css('::text').extract_first().strip()
    zhds = lhc_td[22 - wx_bws].css('::text').extract()
    lhc_item['zhds'] = zhds[0].strip() + zhds[1].strip()
    return lhc_item

