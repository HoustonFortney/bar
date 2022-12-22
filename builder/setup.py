from setuptools import setup

setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['yourscript'],
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
