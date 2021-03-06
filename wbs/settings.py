# -*- coding: utf-8 -*-

# Scrapy settings for wbs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wbs'

SPIDER_MODULES = ['wbs.spiders']
NEWSPIDER_MODULE = 'wbs.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wbs.middlewares.WbsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 开启middlewares中间件,(在这里设置代理IP和设置user-agent)
DOWNLOADER_MIDDLEWARES = {
   # 'wbs.middlewares.WbsDownloaderMiddleware': 543,
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
   'wbs.middlewares.MyUserAgentMiddleware': 543, # 更换user_agent类
   'wbs.middlewares.MyCookiesMiddleware': 545, # 更换cookies类
   'wbs.middlewares.MyProxyMiddleware': 542, # 更换ip
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 开启pipelines组件
ITEM_PIPELINES = {
    'wbs.pipelines.WbsPipeline': 300, # 默认类
    # 'wbs.pipelines.MysqlPipeline': 301, # 操作mysql数据库类
}


# Mysql数据库的配置信息 
MYSQL_HOST = '127.0.0.1' # 数据库IP地址
MYSQL_DBNAME = 'lyq_db' # 数据库名字
MYSQL_USER = 'root' # 数据库账号
MYSQL_PASSWORD = 'root' # 数据库密码
MYSQL_PORT = 3306 # 数据库端口


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 开启日志
# LOG_LEVEL = 'DEBUG'
# 日志保存路径
# LOG_FILE = './douban_log.log'

#是否启用日志（创建日志后，不需开启，进行配置）
# LOG_ENABLED=False  #（默认为True，启用日志）
 
#日志编码
# LOG_ENCODING='utf-8'
 
#如果是True ，进程当中，所有标准输出（包括错误）将会被重定向到log中
#例如：在爬虫代码中的 print（）
# LOG_STDOUT=True  #(默认为False)
