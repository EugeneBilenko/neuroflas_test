**RUNNING PROJECT LOCALLY**

In current folder make these commands:

1) Create virtual environment if not exists:
```
	virtualenv -p python3 venv
```
2) Activate virtual environment
```
	source venv/bin/activate
```
3) ***IMPORTANT***: install next libraries before the installing requirements to avoid mysql errors:
```
	sudo apt-get install python-dev python3-dev
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install python3-mysqldb
```
4) Set up all required packages  from `requirements.txt` file:
```
	pip install -r requirements.txt
```
5) Run database migrations
```
	python manage.py migrate
```

6) Fill currency codes
```
    python manage.py fill_currency_codes
```

7) Scrape currency exchange data
```
    python manage.py initial_scrape_data
```

8) Finally, start the project:
```
	python manage.py runserver
```

9) actual routes
```
    http://localhost:8000/converter/?from=UAH&to=USD&amount=17.4
```