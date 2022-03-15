
import json
from crawling.module import execute, related_keyword_w2v
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'backend', 'crawling'))
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.parse
from requests import Request, Session
import pprint

@swagger_auto_schema(
    operation_id="뉴스요약 & 관련키워드 조회",
    method="POST",
    operation_description="뉴스요약과 함께 키워드 조회",
    responses={200: openapi.Response("OK",)},


    request_body=openapi.Schema(
        '뉴스전문',
        type=openapi.TYPE_OBJECT,
        properties={
            'news' : openapi.Schema('뉴스 본문', type='string'),
            'key' : openapi.Schema('키워드', type='string')},
        required=['news'])
    )
@api_view(['POST'])
def get_tag(request):

    request = json.loads(request.body)
    news = request['news']
    keyword = request['key']


    data = related_keyword_w2v(keyword, news)  


    # 요약 api
    s = Session()

    headers = {
        'Authorization' : "Basic a3VzaXRtczp6ZXN0QDQybWFydQ=="
    }
    payload = {
        'net_input':[{
            'article':news
        }],
        'extractive':False
    }
    url = "http://kr.textsum.42maru.com/predict"

    req=Request('POST', url, data=json.dumps(payload), headers=headers)

    prepped = req.prepare()
    res=s.send(prepped)
    summarized = res.json()['summaries']           #결과값 받기

    keyword_array = []
    for arr in data:
        keyword_array.append(arr[0])

    return Response({"summarized":summarized, "data":keyword_array})


@swagger_auto_schema(
    operation_id="키워드 뉴스 조회",
    method="GET",
    operation_description="키워드 맞춤 뉴스 조회",
    responses={200: openapi.Response("OK",)},
    manual_parameters=[
        openapi.Parameter('query', openapi.IN_QUERY, type='string')],
    )
@api_view(['GET'])
def get_news(request):
    query = request.query_params.get('query', None)

    query = urllib.parse.quote(query)

    data = execute(query)

    return Response(data)