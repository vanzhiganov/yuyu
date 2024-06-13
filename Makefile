pypi:
	python setup.py sdist

rpm: manpage
	python setup.py bdist --format=rpm

manpage:
	pandoc -s -tman README.md | gzip > yuyu.1.gz

clean:
	python setup.py clean
	rm yourtool.1