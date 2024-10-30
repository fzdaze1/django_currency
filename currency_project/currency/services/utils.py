import requests
from django.conf import settings


def fetch_usd_to_rub():
    params = {
        'access_key': settings.EXCHANGE_API_KEY,
        'currencies': 'RUB',
        'format': 1
    }

    try:
        response = requests.get(settings.EXCHANGE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if 'quotes' in data and 'USDRUB' in data['quotes']:
            return data['quotes']['USDRUB']
        else:
            raise ValueError("Курс RUB не найден в ответе API")

    except (requests.RequestException, ValueError) as e:
        print(f"Ошибка при запросе API: {e}")
        return None
