# -*- coding: utf-8 -*-


import scrapy
from wbs.items import DouBanItem

class WeiBoSpider(scrapy.Spider):
	#设置name
	name = "weibo"
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
			#返回信息将数据yield到piplines中
			yield item

		# 获取下一页链接
		next_link = response.xpath('.//span[@class="next"]/link/@href').extract_first()
		if next_link != None:
			# 请求下一页规则
			yield scrapy.Request('https://movie.douban.com/top250' + next_link, callback=self.parse)
			# print('下一页：https://movie.douban.com/top250' + next_link)



