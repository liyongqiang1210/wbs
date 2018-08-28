# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouBanItem(scrapy.Item):
	""" 豆瓣电影信息 """

	# 电影名
	film_name = scrapy.Field()
	# 电影简介
	film_introduction = scrapy.Field()
	# 电影评论url
	film_comment_url = scrapy.Field()
	# 评分
	film_rating_score = scrapy.Field()
	# 评价数
	film_rating_num = scrapy.Field()
	# 电影标签
	film_label = scrapy.Field()
	# 电影排序
	film_serial_num = scrapy.Field()

class FilmCommentItem(scrapy.Item):
	""" 电影评论信息 """
	
	# 评论人昵称
	comment_nick_name = scrapy.Field()
	# 评论内容
	comment_content = scrapy.Field()

		
	
