import requests

import parser

WEBTOON_ID = 651673

# soup = get_soup_from_naver_webtoon_by_page('690502')
# episode_list = get_episode_list_from_page(soup)
# print(episode_list)

# r = parser.get_webtoon_recent_episode_number(WEBTOON_ID)
# print(r)


# parser.get_webtoon_episode_list(WEBTOON_ID)

# result = parser.get_episode_list_from_page(WEBTOON_ID)
# for item in result:
#     print(item)
result = parser.get_episode_list_from_page(WEBTOON_ID)


def save_file_from_url(path, url):
    # stream=True는 곧바로 파일을 다운로드 받지 않음을 의미
    r = requests.get(url, stream=True)
    # 요청이 성공적으로 완료되었을 경우(코드200)
    if r.status_code == 200:
        # 인자로 주어진 path의 파일을 열고 1024byte단위로 파일을 다운받아 기록함
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)


# 모든 리스트 html파일로 출력
# result = parser.get_webtoon_episode_list(WEBTOON_ID)
with open('webtoon.html', 'wt') as f:
    # thumbnail디렉토리가 존재하지 않을경우 생성
    import os

    if not os.path.exists('thumbnails'):
        os.makedirs('thumbnails')

    f.write('<html><head><meta charset="UTF-8"></head><body>')
    for item in result:
        # 파일을 저장할 path문자열
        # thumbnail/thumb_143.jpg
        path = os.path.join('thumbnails', 'thumb_{}{}'.format(item['no'], item['file_ext']))

        # 저장할 path와 이미지 url을 함수 인자로 넘김 (썸네일 이미지 파일 저장)
        save_file_from_url(path, item['url_img_thumbnail'])
        f.write('''
            <div>
                <img src="{path}">
                <a href="http://comic.naver.com{href}">{title}</a>
                | <span>{created}</span>
            </div>'''.format(
            path=path,
            href=item.get('link', '#'),
            title=item['title'],
            created=item['created']
        ))
    f.write('</body></html>')


# 딕셔너리 링크없을때 예외처리
# href=item.get('link', '#')

# result = parser.get_webtoon_episode_list_by_range(WEBTOON_ID, 27, 42)
