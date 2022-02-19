import requests


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers) # передаем в запрос словарь заголовков. В нем прописан юзер агент, чтобы сайт подумал, что в него зашли с браузера
    if response.status_code != 200:               # если не получили нормальный код успешного запроса, возвращаем хуй без масла
        return None
    return response.text                          # инача возрващаем хтмл странички


if __name__ == '__main__':
    print(get_html("https://anekdotovstreet.com/nacionalnosti/negry/"))
