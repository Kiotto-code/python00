all: main

main:
	pip install --upgrade pip
	pip install -r requirement.txt
	python3 setup.py sdist bdist_wheel
	pip install ./dist/ft_package-0.0.1.tar.gz 
# pip install dist/ft_package-0.0.1-py3-none-any.whl
clean:
	pip uninstall ft_package

fclean:
	rm -rf build dist ft_package.egg-info ft_package-0.0.1.dist-info

.PHONY:	dist clean