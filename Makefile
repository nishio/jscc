DEFAULT: server client

client: closure_library closure_compiler

closure_library:
	svn checkout http://closure-library.googlecode.com/svn/trunk/ closure-library
	mkdir client/thirdparty
	mv closure-library client/thirdparty

closure_compiler:
	wget http://closure-compiler.googlecode.com/files/compiler-latest.zip
	mv compiler-latest.zip client/thirdparty
	cd client/thirdparty; unzip compiler-latest.zip

server: highcharts

highcharts:
	wget http://www.highcharts.com/downloads/zips/Highcharts-2.2.1.zip
	-mkdir -p server/static/thirdparty/Highcharts
	mv Highcharts-2.2.1.zip server/static/thirdparty/Highcharts
	cd server/static/thirdparty/Highcharts; unzip Highcharts-2.2.1.zip

