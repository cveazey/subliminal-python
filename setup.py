from setuptools import setup

config = {
	'descripton': 'My Project',
	'author': 'My Name',
	'url': 'Who Knows',
	'download_url': 'Who knows',
	'author_email': 'My Email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['PACKAGE_NAME'],
	'scripts': [],
	'name': 'PROJECT_NAME'
}

setup(**config)
