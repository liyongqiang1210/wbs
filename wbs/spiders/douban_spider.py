# -*- coding: utf-8 -*-

import time
import random
import scrapy
import json
from wbs.items import DouBanItem
from selenium import webdriver

class DouBanSpider(scrapy.Spider):
	#设置name
	name = 'douban'
	#设定域名
	allowed_domains = ['baidu.com','movie.douban.com','douban.com']
	#填写爬取地址
	start_urls = ['https://movie.douban.com/top250']

	def open_chrome(self, response):
		"""  """
		print('=================================>打开浏览器')
		driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
		driver = webdriver.Chrome(executable_path=driver_path)
		driver.get('https://movie.douban.com/top250')
		
		# 从本地文件中读取cookies
		cookies = self.get_douban_cookies()
		print('=================================>开始添加cookies')
		for cookie in cookies:
			driver.add_cookie({
					'domain': cookie['domain'],
					'name': cookie['name'],
					'value': cookie['value'],
					'path': '/',
					'expires': None
				})
		print('=================================>添加cookies成功')
					
		# 刷新当前页面
		driver.refresh()
		
		time.sleep(10)
		
		driver.quit()
		
	def get_douban_cookies(self):
		""" 通过从本地文件中读取方式获取登录后的cookies"""
		
		# 从文件中读取cookies
		with open("douban_cookies.json", "r", encoding='utf-8') as fp:
			# 解析json数据
			cookies = json.loads(fp.read())
			
		return cookies

	def get_douban_cookies_by_login(self):
		""" 通过登录的方式获取豆瓣登录后的cookies """

		# 打开豆瓣登录页面
		driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
		driver = webdriver.Chrome(executable_path=driver_path)
		driver.get('https://www.douban.com/accounts/login?source=movie')
		print('=================================>豆瓣登录页面已打开')

		# 获取登录输入框并填入值
		username = driver.find_element_by_id('email')
		username_input = input('请输入用户名:')
		username.send_keys(str(username_input))
		# 获取密码输入框并填入值
		password = driver.find_element_by_id('password')
		password_input = input('请输入密码:')
		password.send_keys(str(password_input))
		# 找到登录按钮
		login = driver.find_element_by_name('login')
		login.click()
		print('=================================>豆瓣用户登录成功')
		
		time.sleep(20)
		
		# 获取登录后的cookies并转换成json格式
		cookies = json.dumps(driver.get_cookies())
		print('=================================>获取用户登录后的cookies成功')
		
		# 将cookies保存到文件中
		with open('douban_cookies.json','w') as fp:
			# 清空文件内容
			fp.truncate()
			# 保存到文件
			fp.write(cookies)
			
		print('=================================>保存用户登录后的cookies成功')
		driver.quit()
		print('=================================>浏览器关闭成功')
		return cookies


	# 编写爬取方法
	def parse(self, response):
		""" """
		# self.get_douban_cookies()
		yield scrapy.Request(url=self.start_urls[0], callback=self.open_chrome)
		# 先获取电影信息的div集合
		# film_list = response.xpath('//div[@class="item"]')
		# # 循环电影信息集合
		# for film in film_list:
		# 	# 导入item文件
		# 	item = DouBanItem()
		# 	# 开始解析单个电影信息
		# 	# 获取电影排名
		# 	item['film_serial_num'] = film.xpath('.//div[@class="pic"]/em/text()').extract_first()
		# 	# 获取电影名称
		# 	item['film_name'] = film.xpath('.//span[@class="title"]/text()').extract_first()
		# 	# 获取电影评论内容url
		# 	item['film_comment_url'] = film.xpath('.//div[@class="hd"]/a/@href').extract_first()
		# 	# 获取电影简介
		# 	content_list = film.xpath('.//p[@class=""]/text()').extract()
		# 	# 对多行数据进行处理
		# 	for content in content_list:
		# 		item['film_introduction'] = ''.join(content.split())
		# 	# 获取电影评分
		# 	item['film_rating_score'] = film.xpath('.//span[@class="rating_num"]/text()').extract_first()
		# 	# 获取电影评价数
		# 	item['film_rating_num'] = film.xpath('.//div[@class="star"]/span[last()]/text()').extract_first()
		# 	# 获取电影标签
		# 	item['film_label'] = film.xpath('.//span[@class="inq"]/text()').extract_first()

		# 	# 根据电影评论url获取评论数据
		# 	comment_url = item['film_comment_url'] + 'comments?status=P'
		# 	# yield scrapy.Request(comment_url, callback=self.parse_comment)
		# 	#返回信息将数据yield到piplines中
		# 	yield item
		# 	time.sleep(random.randint(0,9) * 0.1)

		# # 获取下一页链接
		# next_link = response.xpath('.//span[@class="next"]/link/@href').extract_first()
		# if next_link != None:
		# 	# 请求下一页规则
		# 	yield scrapy.Request('https://movie.douban.com/top250' + next_link, callback=self.parse)

	def parse_comment(self, response):
		""" 获取电影评论数据 """

		print("评论区")
		comment_list = response.xpath('//div[@class="comment-item"]')
		# 遍历评论列表
		for comment in comment_list:
			comment_item = FilmCommentItem()
			# 获取评论人昵称
			comment_item['comment_nick_name'] = comment.xpath('.//div[@class="comment-info"]/h3/span[1]/a/text()').extract_first()

			yield comment_item




