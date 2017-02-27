import requests
from bs4 import BeautifulSoup


def get_soup_from_url(url, params=None):
    '''
    url과 params를 사용해서 해당 url에 GET 요청 결과(HTML text)로
    BeautifulSoup 객체를 생성해서 반환
    :param url: GET 요청을 보낼 url string
    :param params: GET 요청 url 매개변수 dict
    :return: BeautifulSoup object
    '''
    # requests.get 요청을 본낸 결과(response 객체)를 r변수에 할당
    r = requests.get(url, params=params)
    # response 객체(r)에서 text 메소드를 사용해 내용을 html_doc변수에 할당
    html_doc = r.text

    # BeautifulSoup 객체를 생성, 인자는 html text
    soup = BeautifulSoup(html_doc, 'lxml')
    return soup
