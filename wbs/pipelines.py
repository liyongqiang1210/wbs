# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from wbs import settings

class WbsPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
	"""操作数据库类"""

	def __init__(self):
		
		# 打开数据库连接
		self.connect = pymysql.connect(
			host=settings.MYSQL_HOST,
			db=settings.MYSQL_DBNAME,
			user=settings.MYSQL_USER,
			password=settings.MYSQL_PASSWORD,
			charset='utf8',
			use_unicode=True)
		# 创建cur游标对象
		self.cursor = self.connect.cursor()

	# pipelines组件默认调用
	def process_item(self, item, spider):
		try:
			# 使用execute()方法执行SQL语句
			self.cursor.execute()
			# 提交到数据库
			self.connect.commit()
		except Exception as e:
			# 发生错误数据回滚
			self.connect.rollback()
		return item

	def close_spider(self, spider):
		self.connect.close()
		
