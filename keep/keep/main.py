
#此文件用于从IDE启动 IDE调试
from scrapy import cmdline
cmdline.execute("scrapy crawl keep".split())

# cmdline.execute("scrapy crawl toutiao".split())