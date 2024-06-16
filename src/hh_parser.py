import requests


def get_companies():
    """
        Получает имя компаний и их ID,
        :return: список словарей с информацией о компаниях
        """
    companies_data = {
        'Т - банк': 78638,
        'Яндекс': 1740,
        'Билайн': 4934,
        'Озон': 2180,
        'Банк ВТБ': 4181,
        'Газпромнефть': 39305,
        'Альфа-банк': 80,
        'СберТех': 3529,
        'ООО Зерокодер': 5856776,
        'Айтеко': 872178
    }

    data = []

    for company_name, company_id in companies_data.items():
        company_url = f"https://hh.ru/employer/{company_id}"
        company_info = {'company_id': company_id, 'company_name': company_name, 'company_url': company_url}
        data.append(company_info)

    return data

