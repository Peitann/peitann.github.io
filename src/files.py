import json
import os
from utilities import convert_to_date, remove_duplicate_entries


def get_file_path():
    # Mendapatkan path file JSON
    dir_path = os.getcwd()
    return os.path.join(dir_path, "data", "republika_news.json")


def load_from_json(file_path):
    data = []
    try:
        # Memuat data yang sudah ada
        with open(file_path, 'r') as file:
            data = json.loads(file.read())
            file.close()
        return data
    except IOError:
        print("[PERINGATAN] Gagal memuat data yang sudah ada.")


def transform_data(data: list, file_path) -> list:
    # Memuat data yang sudah ada
    existing_data = load_from_json(file_path)
    if existing_data:
        data.extend(existing_data)
    # Mengurutkan dari yang terbaru (menurun) berdasarkan tanggal scraping
    data = sorted(data, reverse=True, key=lambda d: convert_to_date(d["waktu_scraping"]))
    # Menghapus entri duplikat
    data = remove_duplicate_entries(data, "judul")

    return data


def write_to_file(data, file_path):
    # Menulis ke file
    print("[INFO] Menyimpan berita utama ke data/replubika_news.json ...")
    try:
        with open(file_path, 'w') as file:
            file.writelines(data)
            file.close()
        print("[INFO] Berhasil menyimpan data ke file.")
    except IOError:
        print("[PERINGATAN] Gagal menyimpan data.")


def save_to_json(data: list, file_path):
    # Membersihkan data
    data = transform_data(data, file_path)
    # Mengonversi list dari dictionary menjadi objek JSON
    json_data = json.dumps(data)
    # Menyimpan data ke file
    write_to_file(json_data, file_path)
