try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simulation of roulette',
    'author': 'Ankit Singh',
    'download_url': 'https://github.com/ankitsingh/roulette',
    'author_email': 'ankit.11235@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['roulette'],
    'scripts': [],
    'name': 'roulette'
}

setup(**config)