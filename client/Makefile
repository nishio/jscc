# settings for this project
CLOSURE_LIB = ../client/thirdparty/closure-library
CALCDEPS = $(CLOSURE_LIB)/closure/bin/calcdeps.py
CLOSURE_BUILDER = $(CLOSURE_LIB)/closure/bin/build/closurebuilder.py
CLOSURE_COMPILER = ../client/thirdparty/compiler.jar
LIBPATH = js $(CLOSURE_LIB)
ENTRYPOINT = static/main.js
EXTERNS = ../common/externs/nhiro.js

# automatic settings
LIBPATH_FOR_CALCDEPS = $(patsubst %,-p %, $(LIBPATH))
LIBPATH_FOR_BUILDER = $(patsubst %,--root="%", $(LIBPATH))
EXTERNS_FOR_BUILDER = $(patsubst %,--compiler_flags="--externs=%", $(EXTERNS))

# targets
deps: deps.js deps.txt

deps.js:
	$(CALCDEPS) -i $(ENTRYPOINT) -o deps $(LIBPATH_FOR_CALCDEPS) > deps.js

deps.txt:
	$(CALCDEPS) -i $(ENTRYPOINT) -o list $(LIBPATH_FOR_CALCDEPS) > deps.txt

watch: deps.txt
	./build.sh
	cat deps.txt | xargs watchmedo shell-command --command="./build.sh" &

lint: deps.txt
	-cat deps.txt | xargs gjslint > new_lint.log 2> /dev/null
	mv new_lint.log lint.log
	cat lint.log

compile: deps.js
	-$(CLOSURE_BUILDER) \
	    --namespace="main.main" \
	    $(LIBPATH_FOR_BUILDER) \
	    $(EXTERNS_FOR_BUILDER) \
	    --output_mode=compiled --compiler_jar="$(CLOSURE_COMPILER)" \
	    -f --compilation_level=ADVANCED_OPTIMIZATIONS \
	    -f --warning_level=VERBOSE \
	    -f --jscomp_warning=visibility \
	    --compiler_flags="--js=deps.js" \
	    > /dev/null 2> new_compile.log
	mv new_compile.log compile.log
	cat compile.log

report:
	@cat lint.log
	@cat compile.log
	python client.py
