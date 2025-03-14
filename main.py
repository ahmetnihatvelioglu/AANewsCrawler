import time
from crawler import Crawler

crawler = Crawler()

start = time.time()
crawler.get_news( 3313902,  3313935)
crawler.save_news()
end = time.time()

print(end-start)