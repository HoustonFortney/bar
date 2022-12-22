from setuptools import setup

setup(
    name='menu-builder',
    version='0.1.0',
    install_requires=[
        'Click',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'build-menu = cli:build_menu',
            'build-shopping-list = cli:build_shopping_list',
        ],
    },
)
