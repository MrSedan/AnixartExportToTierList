import logging

import requests

BASE_URL = "https://shikimori.one/api/graphql"


def get_image_url(name: str) -> str:
    variables = {"name": name, "limit": 1}
    query = """
    query($name: String, $limit: Int!) {
        animes(search: $name, limit: $limit, kind: "!special") {
            id
            name
            russian
            japanese
            english
            poster { id originalUrl mainUrl }
        }
    }
    """
    headers = {'User-Agent': 'AnixartTierList'}
    response = requests.post(
        BASE_URL, json={'query': query, 'variables': variables}, headers=headers)
    if response.status_code != 200:
        logging.error(f'Не удалось получить ссылку на изображение для: {name}')
        return ""
    data = response.json()
    pic_url = data['data']['animes'][0]['poster']['originalUrl']
    return pic_url


def download_image(url: str, name: str, save_folder: str = './animes'):
    try:
        # User agent for right image save
        img_data = requests.get(url, headers={
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}).content
        with open(f"{save_folder}/{name}.jpeg", 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print(e)
        logging.error(f'Не удалось скачать изображение для: \'{
                      name}\' по ссылке: {url}')


if __name__ == '__main__':
    url = get_image_url(
        "Kimi no koto ga daidaidaidaidai suki na 100-nin no Kanojo")
    download_image(
        url, "Kimi no koto ga daidaidaidaidai suki na 100-nin no Kanojo")
