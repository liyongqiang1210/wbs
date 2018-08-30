#!/usr/bin/env python
# encoding: utf-8
import json
from time import sleep
from selenium import webdriver


def get_douban_cookies_by_login():
	""" 通过登录的方式获取豆瓣登录后的cookies """

	# 打开豆瓣登录页面
	# driver_path = 'E:\Program Files (x86)\python\Scripts\chromedriver.exe'
	driver_path = 'E:\python\Scripts\chromedriver.exe'
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
	
	sleep(20)
	
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


def get_douban_cookies_by_file():
	""" 通过从本地文件中读取方式获取登录后的cookies"""
	
	# 从文件中读取cookies
	with open("douban_cookies.json", "r", encoding='utf-8') as fp:
		# 解析json数据
		cookies = json.loads(fp.read())
		
	return cookies
