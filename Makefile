SASS := $(shell command -v sassc 2> /dev/null)

default: compile

deps:
ifndef SASS
	$(error "sassc is not installed")
endif

compile: deps
	cd ckanext/cob/public/css && sassc -mt compact main.scss main.css
