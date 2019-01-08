import urllib3
from bs4 import BeautifulSoup



if __name__ == "__main__":
	parser = CurrencyParser(debug=True)
	a = parser.run()
	print(a)
