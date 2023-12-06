
checkstyle:
	flake8 *.py

test:
	pytest

clean:
	rm -r __pycache__
