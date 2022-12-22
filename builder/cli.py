import itertools
import json
from functools import lru_cache
from glob import glob

import click
import yaml


def get_all_drinks():
    drink_files = glob('drinks/*.yaml')
    for drink_file_name in drink_files:
        with open(drink_file_name) as drink_file:
            yield yaml.safe_load(drink_file)


@lru_cache()
def list_all_drinks():
    return list(get_all_drinks())


def get_drink(drink_name):
    for drink in list_all_drinks():
        if drink['name'] == drink_name:
            return drink
    raise KeyError('Drink %s not known', drink_name)


def build_drink_description(drink):
    return {
        'name': drink['name'],
        'components': sum(drink['ingredients'].values(), []),
    }


def _build_menu(menu):
    sections = []
    for section_name, section in menu.items():
        section = {
            'name': section_name,
            'description': section['description'],
            'drinks': [build_drink_description(get_drink(drink_name)) for drink_name in section['drinks']],
        }
        sections.append(section)

    return {
        'sections': sections,
    }


def _build_shopping_list(menu):
    all_drinks = list(itertools.chain.from_iterable(section['drinks'] for section in menu.values()))
    all_drink_ingredients = [get_drink(drink_name)['ingredients'] for drink_name in all_drinks]

    shopping_list = {}
    shopping_list_categories = ['booze', 'fresh', 'pantry', 'garnish']
    for category in shopping_list_categories:
        ingredients = set(sum((drink_ingredients.get(category, []) for drink_ingredients in all_drink_ingredients), []))
        shopping_list[category] = sorted(ingredients)

    return shopping_list


@click.command()
@click.option('--menu', default='current_menu.yaml', help='Menu file to build')
@click.option('--output', default='display/src/data/menu.json', help='Output file')
def build_menu(menu, output):
    with open(menu) as menu_file:
        menu = yaml.safe_load(menu_file)
    menu = _build_menu(menu)
    with open(output, 'w') as output_file:
        json.dump(menu, output_file, indent=4)


@click.command()
@click.option('--menu', default='current_menu.yaml', help='Menu file to build')
@click.option('--output', default='display/public/shopping_list.json', help='Output file')
def build_shopping_list(menu, output):
    with open(menu) as menu_file:
        menu = yaml.safe_load(menu_file)
    shopping_list = _build_shopping_list(menu)
    with open(output, 'w') as output_file:
        json.dump(shopping_list, output_file, indent=4)
