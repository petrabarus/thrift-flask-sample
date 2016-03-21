init:
	echo "Installing Python Dependencies"
	virtualenv -p python2 env
	./env/bin/pip install -r requirements.txt
	echo "Installing PHP Dependencies"
	curl -sS https://getcomposer.org/installer | php
	./composer.phar install

run-python: FORCE
	echo "Running python service"
	./env/bin/python application.py

run-php: FORCE
	php application.php

thrift: FORCE
	thrift -version
	thrift -r --gen py geometry.thrift
	thrift -r --gen php:oop,validate geometry.thrift


FORCE:
