import datetime
import json
import os
from mcelhaneyhelpers import Logger


def generate_text_file_with_timestamp(base_name):
    file_name = base_name + '.' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt'
    return file_name


def list_to_dict(input_list):
    i = iter(input_list)
    d = dict(zip(i, i))
    return d


def make_dir_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def read_json_return_dict(file):
    with open(file) as f:
        payload = json.load(f)
    return payload
