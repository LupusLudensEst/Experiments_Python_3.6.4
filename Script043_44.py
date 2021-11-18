# Web data extraction = 1. Crawling; 2. Scraping; 3. Parsing.
# Library Python Requests, Beautiful Soup

# Mechanize for Python2
# pip install requests
# python -u install --upgrade pip
# pip install beautifulsoup4

"""
pip help - помощь по доступным командам.

pip install package_name - установка пакета(ов).

pip uninstall package_name - удаление пакета(ов).

pip list - список установленных пакетов.

pip show package_name - показывает информацию об установленном пакете.

pip search - поиск пакетов по имени.

pip --proxy user:passwd@proxy.server:port - использование с прокси.

pip install -U - обновление пакета(ов).

pip install --force-reinstall - при обновлении, переустановить пакет, даже если он последней версии.
"""


# import requests
# r = request.get("https://www.google.de/search?source=hp&ei=SWhTWoCGO-ywjwSBxoGgCw&q=%D1%80%D0%B0%D0%B7%D1%83%D0%BC%D0%BD%D0%B0%D1%8F+%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C&oq=%D1%80%D0%B0%D0%B7%D1%83%D0%BC%D0%BD%D0%B0%D1%8F+%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C&gs_l=psy-ab.3..0i19k1l8j0i22i30i19k1l2.11061.20451.0.21443.29.19.2.3.3.0.744.3535.3-2j2j2j1.7.0....0...1c.1.64.psy-ab..17.12.3990...0j46j0i13k1j0i13i30k1j0i30k1j0i13i5i10i30k1j0i131k1j0i46k1.0.-t1FGDvS-iA")
# print(r)
# r.encoding
# r.headers
# r.text
