BUILD_LOG := .build.log
VERSION_FILE := src/sximada/djangoutils/__init__.py


.PHONY: bump
bump:
	@## make bump version=VERSION
	@#
	@# Bump version number.

	if [ "$(version)" == "" ]; then echo "You must specify the version.\nex) make bump version=VERSION"; exit 1; fi
	sed -i -e "s/$(shell make version)/$(version)/" $(VERSION_FILE)
	git diff $(VERSION_FILE)
	make version
	git commit -m "bump version to $(version)" $(VERSION_FILE)

.PHONY: production
production:
	@# deploy to pypi server
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm dist/*

.PHONY: staging
staging:
	@# deploy to testpypi server
	python setup.py sdist bdist_wheel
	twine upload -r testpypi sdist bdist_wheel dist/*
	rm dist/*

.PHONY: version
version:
	@if [ -e $(BUILD_LOG) ]; then rm -f $(BUILD_LOG); fi
	@python setup.py build 2> $(BUILD_LOG) 1> /dev/null
	@if [ -s $(BUILD_LOG) ]; then cat $(BUILD_LOG); exit 1; fi
	@grep "^Version" `gfind -name PKG-INFO` | cut -d " " -f 2

.PHONY: docs
docs:
	@## make docs ouput=OUTPUT_DIR
	cd docs; make dirhtml
	if [ $(output) ]; then \
		mkdir -p $(output); \
		tar -c docs/build/dirhtml -C docs/build/dirhtml "./" | tar xfp - -C $(output); \
	fi
