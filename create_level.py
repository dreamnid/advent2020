#!/usr/bin/env python3

import argparse
import os
from pathlib import Path
import sys


parser = argparse.ArgumentParser(description='Create a level')
parser.add_argument('level', type=int)

args = parser.parse_args()

level = args.level
level_name = '%02d' % level

try:
    os.mkdir(level_name)
    print(f'Created: "{level_name}" directory')
except OSError:
    pass

script_file = os.path.join(level_name, '{}.py'.format(level))

# Safe guard that we don't accidentally write over good code
if os.path.isfile(script_file):
    print('Error - file exists')
    sys.exit(1)

with open(script_file, 'w') as fh:
    template_vars = {
        'level' : level,
    }

    with open('level.py.tmpl') as tmpl_fh:
        contents = tmpl_fh.read().format(**template_vars)

    fh.write(contents)

os.chmod(script_file, 0o755)
print(f'Created: {script_file}')

# Create empty input file
Path(os.path.join(level_name, '{}-input.txt'.format(level))).touch()
Path(os.path.join(level_name, '{}a-example.txt'.format(level))).touch()
print(f'Created dummy input files')

print('Finished!')
