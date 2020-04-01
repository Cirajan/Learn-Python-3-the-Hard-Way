try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'ex45Game',
        'auhtor': 'Chris Nicholas',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'nchris27@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex45Game'],
        'scripts': [],
        'entry_points': {
                'console_scripts': [
                    'ex45Game=ex45Game.text_game'
                ]
        },
        'name': 'ex45Game'
}

setup(**config)
