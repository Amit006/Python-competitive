from setup tools import setup

setup(
	name='HelloWorld',
	version='1.0',
	py_modules=['hello'],
	install_requirements=[
	'click',
	],
	entry_points='''
		[console_scripts]
		hello=hello:cli
	    ''',
)
