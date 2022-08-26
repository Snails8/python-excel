ENV=test

build: #build openpyxl
	docker build -t openpyxl:1.0 .

run: # run openpyxl 
	docker run -v `pwd`:/tmp --rm -it openpyxl:1.0 /usr/local/bin/python3 /tmp/src/${ENV}/main.py

move:
	cp test.xlsx sample.xlsx
	mv sample.xlsx ~/Downloads