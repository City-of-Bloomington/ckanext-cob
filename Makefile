SASS := $(shell command -v sassc 2> /dev/null)

default: compile package

deps:
ifndef SASS
	$(error "sassc is not installed")
endif

clean:
	rm -Rf build

compile: deps
	cd ckanext/cob/public/css && sassc -mt compact screen.scss screen.css

package:
	if [ ! -d build ]; then mkdir build; fi
	rsync -rl --exclude-from=buildignore . ./build/ckanext-cob/
	cd build && tar czf ckanext-cob.tar.gz
