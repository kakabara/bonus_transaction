import os
import yaml

CONFIG_FILE = 'config.yml'

if os.environ.get('config'):
    CONFIG_FILE = os.environ.get('config')

config = {}

try:
    with open(CONFIG_FILE, 'r') as ymlfile:
        config = yaml.load(ymlfile)
except FileNotFoundError as e:
    raise('Config file {} does not exists'.format(CONFIG_FILE))