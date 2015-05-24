test:
	python -m doctest inject.py
	python -m unittest discover

doc:
	doc2md.py -t 'Simple dependency injection' -a inject.py  > README.md