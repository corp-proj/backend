from django.http import HttpResponse
from crawling.naver.naver.spiders.rank import rank
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'backend', 'crawling', 'naver'))


def get_tag(request):
    if request.method == 'GET':
        result = rank.spider_results()
        print(result)
        
        return HttpResponse(result)
