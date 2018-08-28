# -*- coding: utf-8 -*-


import scrapy
from wbs.items import DouBanItem

class DouBanSpider(scrapy.Spider):
	#设置name
	name = "douban"
	#设定域名
	allowed_domains = ["movie.douban.com"]
	#填写爬取地址
	start_urls = ["https://movie.douban.com/top250"]
	#编写爬取方法
	def parse(self, response):
		
		#先获取电影信息的div集合
		film_list = response.xpath('//div[@class="item"]')
		# 循环电影信息集合
		for film in film_list:
			# 导入item文件
			item = DouBanItem()
			# 开始解析单个电影信息
			# 获取电影排名
			item['film_serial_num'] = film.xpath('.//div[@class="pic"]/em/text()').extract_first()
			# 获取电影名称
			item['film_name'] = film.xpath('.//span[@class="title"]/text()').extract_first()
			# 获取电影评论内容url
			item['film_comment_url'] = film.xpath('.//div[@class="hd"]/a/@href').extract_first()
			# 获取电影简介
			content_list = film.xpath('.//p[@class=""]/text()').extract()
			# 对多行数据进行处理
			for content in content_list:
				item['film_introduction'] = ''.join(content.split())
			# 获取电影评分
			item['film_rating_score'] = film.xpath('.//span[@class="rating_num"]/text()').extract_first()
			# 获取电影评价数
			item['film_rating_num'] = film.xpath('.//div[@class="star"]/span[last()]/text()').extract_first()
			# 获取电影标签
			item['film_label'] = film.xpath('.//span[@class="inq"]/text()').extract_first()

			# 根据电影评论url获取评论数据
			comment_url = item['film_comment_url'] + 'comments?status=P'
			# yield scrapy.Request(comment_url, callback=self.parse_comment)
			#返回信息将数据yield到piplines中
			yield item

		# 获取下一页链接
		next_link = response.xpath('.//span[@class="next"]/link/@href').extract_first()
		if next_link != None:
			# 请求下一页规则
			yield scrapy.Request('https://movie.douban.com/top250' + next_link, callback=self.parse)

	def parse_comment(self, response):
		""" 获取电影评论数据 """

		print("评论区")
		comment_list = response.xpath('//div[@class="comment-item"]')
		# 遍历评论列表
		for comment in comment_list:
			item = FilmCommentItem()
			# 获取评论人昵称
			item['comment_nick_name'] = comment.xpath('.//div[@class="comment-info"]/h3/span[1]/a/text()').extract_first()

			yield item




