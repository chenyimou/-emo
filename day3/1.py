import requests
import os
from bs4 import BeautifulSoup
import json

def get_movie_data():
    """爬取豆瓣电影排行榜数据并解析"""
    url = "https://movie.douban.com/chart"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    try:
        # 获取网页内容
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"请求成功，状态码: {response.status_code}")

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = []

        # 提取电影信息
        for item in soup.select('.indent table'):
            title = item.select_one('.nbg')['title']
            rating = item.select_one('.rating_nums').text
            details = item.select_one('.pl').text.strip()

            movies.append({
                'title': title,
                'rating': rating,
                'details': details
            })

        # 保存数据
        os.makedirs("/", exist_ok=True)
        with open(r"/douban_movies.json", "w", encoding="utf-8") as f:
            json.dump(movies, f, ensure_ascii=False, indent=2)

        print(f"成功爬取并保存了{len(movies)}部电影信息")
        return movies

    except Exception as e:
        print(f"爬取过程中发生错误: {str(e)}")
        return None

if __name__ == "__main__":
    get_movie_data()