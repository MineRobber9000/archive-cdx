.PHONY: publish

publish: README.rst
	python3 setup.py sdist upload

README.rst: README.md
	pandoc --from markdown --to rst < README.md > README.rst
