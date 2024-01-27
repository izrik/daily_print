#!/usr/bin/env python3

from jinja2 import Template


def main():
    with open('template.html') as f:
        template = Template(f.read())
        items = [
            'Do the dishes',
            'Check the mail',
            'Buy stamps',
        ]
    print(template.render(items=items))


if __name__ == '__main__':
    main()
