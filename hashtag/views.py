from django.http import HttpResponse
from crawling.module import execute, related_keyword_w2v
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'backend', 'crawling'))


def get_tag(request):
    if request.method == 'GET':
        data = execute("사회")
        
        return HttpResponse(data)
