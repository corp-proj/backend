## 큐시즘 기업프로젝트 - 42MARU 5조 Backend

-------
### [Develpment Requirements]  

- **IDE**  
VScode is recommended but whatever you prefer.. ;)  

- **Python 3.9, Pipenv**  
Using pipenv for package management and virtual environment.  
Project is based on Python 3.9  

Run pipenv virtual environment by command ```pipenv shell ```
Install all requirements by command ```pipenv intall```

--------
<br>  

### [API 명세]
[API swagger 개발 문서 바로가기](http://3.37.205.195:8000/swagger/)  
<br>

- GET /api/news?query=선호키워드  
    - 쿼리 파라미터로 받은 유저의 선호 키워드로(ex.코로나,대선,경제 등) 네이버 뉴스를 크롤링 하여 반환하는 api.
    - 최대 7개 반환함.
    - 크롤링 프레임워크로 scrapy 사용.

<br>

- POST /api/hashtag
    - 뉴스 전문과 선호 키워드를 받아서 42마루 뉴스요약api의 결과값과 해시태그 추출 결과 반환.
    - 해시태그(또는 키워드) 추출 모델로 word2vec 사용.
    - 짧은 인터넷 뉴스의 영향으로 선호키워드와 뉴스 전문 사이의 연관성이 적을 경우 해시태그 추출이 안될 수 있음. ( 이 경우 빈배열 반환 )