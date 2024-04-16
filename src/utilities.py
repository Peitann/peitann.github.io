import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def convert_to_date(date_str: str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


def parse_content(html_element):
    return html_element.text.strip()


def fetch_html_content(url):
    # headers permintaan
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    # mendapatkan konten html
    print(f'[INFO] Mengambil konten html dari: {url} ...')
    response = requests.get(url, headers=headers)
    if response.status_code == 200 or response.reason == "OK":
        print("[INFO] Sukses mengambil konten html.")
        html_content = BeautifulSoup(response.text, "html.parser")
        return html_content
    else:
        raise Exception(f'[ERRO] Gagal mengambil data dari {url} dengan kode status: {response.status_code}. {response.raise_for_status()}')


def extract_headlines(html_content):
    return html_content.find_all("div", class_="max-card__title")


def parse_headlines(headlines):
    parsed_data = []
    # parse headline
    for headline in headlines:
        # dapatkan judul
        title = parse_content(headline.find("h2", {"class": re.compile('headline-*')}))
        # dapatkan kategori dan waktu publikasi
        info = parse_content(headline.find("div", {"class": "date date-item__headline"}))
        # lampirkan ke dalam kamus
        parsed_data.append({
            "judul": title,
            "kategori": info.split('-')[0].strip(),
            "waktu_publish": info.split('-')[1].strip(),
            "waktu_scraping": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        })

    return parsed_data


def remove_duplicate_entries(data: list, key) -> list:
    seen_keys = set()
    unique_data = []
    # perulangan data yang ada
    for entry in data:
        # jika data saat ini tidak tersedia dalam seen_keys maka tambahkan
        if entry[key] not in seen_keys:
            unique_data.append(entry)
            seen_keys.add(entry[key])
    return unique_data
