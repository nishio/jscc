DEFAULT: server client

client: closure_library closure_compiler

closure_library: client/thirdparty/closure-library

client/thirdparty/closure-library:
	svn checkout http://closure-library.googlecode.com/svn/trunk/ closure-library
	mkdir client/thirdparty
	mv closure-library client/thirdparty

closure_compiler: client/thirdparty/compiler.jar

client/thirdparty/compiler.jar:
	wget http://closure-compiler.googlecode.com/files/compiler-latest.zip
	mv compiler-latest.zip client/thirdparty
	cd client/thirdparty; unzip compiler-latest.zip

server: highcharts

highcharts: server/static/thirdparty/Highcharts/js

server/static/thirdparty/Highcharts/js:
	wget http://www.highcharts.com/downloads/zips/Highcharts-2.2.1.zip
	-mkdir -p server/static/thirdparty/Highcharts
	mv Highcharts-2.2.1.zip server/static/thirdparty/Highcharts
	cd server/static/thirdparty/Highcharts; unzip Highcharts-2.2.1.zip

# for easy development
quickstart:
	-rm -rf qssample
	python quickstart.py
	cd qssample; make compile