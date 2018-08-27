# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouBanItem(scrapy.Item):
	
	# 电影名
	film_name = scrapy.Field()
	# 电影简介
	film_introduction = scrapy.Field()
	# 评分
	film_rating_score = scrapy.Field()
	# 评价数
	film_rating_num = scrapy.Field()
	# 电影标签
	film_label = scrapy.Field()
	# 电影排序
	film_serial_num = scrapy.Field()
	
