DEFAULT=run

SOURCE_DIR:=./src

init:
	pip install -r ./requirements.txt
	python -m nltk.downloader stopwords

run:
	python ${SOURCE_DIR}/main.py --path ${PATH}

lint:
	pylint ${SOURCE_DIR}

.PHONY: init run lint