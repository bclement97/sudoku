.PHONY: all install clean

all: install

install:
	pip install -r requirements.txt

clean:
	pip uninstall -r requirements.txt