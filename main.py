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

    args = parser.parse_args()

    with open('template.html') as f:
        template = Template(f.read())
        items = [
            'Do the dishes',
            'Check the mail',
            'Buy stamps',
        ]
    html = template.render(items=items)
    if args.format == 'html':
        print(html)
    elif args.format == 'pdf':
        with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
            pisa.CreatePDF(html, dest=stdout)
    else:
        raise Exception(f'Unknown format "{args.format}"')


if __name__ == '__main__':
    main()
