compile :
	python setup.py bdist_wheel
install :
	pip install dist/number_to_words-0.1.1-py3-none-any.whl
upload :
	python -m twine upload dist/number_to_words-0.1.2-py3-none-any.whl
