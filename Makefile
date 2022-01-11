SHELL := /bin/bash

run:
	python3 src/muzyka_genreate.py

web:
	source src/web/env/bin/activate
	python3 src/web/app.py

clean:
	rm datasets/csv_data/song_dataset_out.csv
