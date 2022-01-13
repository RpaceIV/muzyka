SHELL := /bin/bash

start:
	python3 src/muzyka_start.py

generate:
	python3 src/muzyka_generate.py

web:
	source src/web/env/bin/activate
	python3 src/web/app.py

clean:
	rm datasets/csv_data/song_data_out.csv
