ENV=test
NAME=sample

build: #build openpyxl
	docker build -t openpyxl:1.0 .

run: # run openpyxl 
	docker run -v `pwd`:/tmp --rm -it openpyxl:1.0 /usr/local/bin/python3 /tmp/src/${ENV}/main.py

move: 
	cp ${NAME}.xlsx output.xlsx
	mv output.xlsx ~/Downloads