# Sample Thrift service using Flask application
Sample Flask application that works as Thrift service. While Thrift python library itself provide its own built-in application to handle the Thrift requests, this is just a small experiment I did. 

This is based on [@BeanYoung's](https://gist.github.com/BeanYoung/8318363). The client is using PHP.

## Requirements
This sample is tested with

- GNU Make 3.81 (Or if you don't have, see simple commands in Makefile)
- Python 2.7
- Pip 8.0.0
- Virtualenv 14.0.0
- PHP 5.6

## Important Files
There are three important files to see.

1. `geometry.thrift` is the Thrift definition for Point struct and distance calculator service.
2. `application.py` is the Flask application source code.
3. `application.php` is the PHP client source code.

## Running The Sample
To initialize both Python and PHP service and client respectively, execute
the makefile.

```
make init
```

To run the Python service, execute

```
make run-python
```

To run the PHP client, execute

```
make run-php
```
