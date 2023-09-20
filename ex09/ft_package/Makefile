all: main

main: dist

# dist:
# 	python3 ../setup.py sdist bdist_wheel
# 	pip install ../dist/ft_package-0.0.1.tar.gz 
# flit build
# python3 setup.py sdist bdist_wheel

clean:
	pip uninstall ft_package

fclean:
	rm -rf build dist ft_package.egg-info ft_package-0.0.1.dist-info

.PHONY:	dist clean
# all: main

# main: dist
# 	python3 -m pip install --upgrade pip setuptools wheel 
# 	pip install -r requirement.txt
# 	pip install --upgrade . --target=/Users/yichan/work/Python/ex09

# dist:
# 	python3 setup.py sdist bdist_wheel --dist-dir=/Users/yichan/work/Python/ex09

# clean:
# 	pip uninstall ft_package

# .PHONY:	dist clean