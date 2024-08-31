import requests
from urllib.parse import quote


def search_request(string):
    encoded_query = quote(string)

    url = f"https://search.wb.ru/exactmatch/ru/common/v7/search?ab_testing=false\
    &appType=1&curr=rub&dest=-1257786&page=1&query={encoded_query}&resultset=catalog\
    &sort=popular&spp=30&suppressSpellcheck=false"

    params = {
        "ab_testing": "false",
        "appType": "1",
        "curr": "rub",
        "dest": "-1257786",
        "page": "1",
        "query": encoded_query,
        "resultset": "catalog",
        "sort": "popular",
        "spp": "30",
        "suppressSpellcheck": "false"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Connection": "keep-alive",
        "Host": "search.wb.ru",
        "Origin": "https://www.wildberries.ru",
        "Referer": f"https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search={encoded_query}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "x-queryid": "qid390109941172495968220240831122825"
    }

    response = requests.get(url, headers=headers, params=params)

    return response


def data_processor(data, article):
    for index, product in enumerate(data['data']['products']):
        if product['id'] == article:
            return (index + 1) if index < 5000 else None
    else:
        return None


def article_position(string, article):
    response = search_request(string)
    return data_processor(response.json(), article)



