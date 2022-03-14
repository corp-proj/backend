from django.http import HttpResponse
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from crawling.naver.naver.spiders import rank


#scrapyd = ScrapydAPI('http://localhost:6800')

def get_tag(request):
    if request.method == 'GET':
        process = CrawlerRunner(get_project_settings())
        results= process.crawl(rank.rank)   #type이


        print(type(results))
        return HttpResponse('none')