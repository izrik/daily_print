#!/usr/bin/env python3
import argparse
import os
import sys

from jinja2 import Template
from xhtml2pdf import pisa


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', choices=('html', 'pdf'),
                        default='html')
    parser.add_argument('--html', action='store_const',
                        const='html', dest='format')
    parser.add_argument('--pdf', action='store_const',
                        const='pdf', dest='format')
    parser.add_argument('--name')
    parser.add_argument('items', nargs='*')
    parser.add_argument('--dot', '-d', action='append', nargs='+')
    parser.add_argument('--check', '-c', action='append', nargs='+')

    args = parser.parse_args()

    with open('template.html') as f:
        template = Template(f.read())
    items = []
    if args.items:
        items.extend(args.items)
    if args.check:
        for list_ in args.check:
            items.extend(list_)
    dot_items = []
    if args.dot:
        for list_ in args.dot:
            dot_items.extend(list_)
    heading = 'Tasks for today'
    if args.name:
        heading = f'{args.name}\'s tasks for today'
    html = template.render(items=items, heading=heading, dot_items=dot_items)
    if args.format == 'html':
        print(html)
    elif args.format == 'pdf':
        with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
            pisa.CreatePDF(html, dest=stdout)
    else:
        raise Exception(f'Unknown format "{args.format}"')


if __name__ == '__main__':
    main()
