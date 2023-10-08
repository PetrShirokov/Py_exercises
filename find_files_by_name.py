import hexlet
from hexlet import fs
from hexlet.fs import is_file, is_directory, mkdir, mkfile
from hexlet.fs import get_name, get_children
import os

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


def find_files_paths(tree, substr):
    ancestry = ''
    def walk(node, ancestry):
        name = get_name(node)
        ancestry = os.path.join(ancestry, name)
        children = get_children(node)
        if is_file(node) and (substr in name):
            return ancestry
        file_names = map(lambda child: walk(child, ancestry),
        children)
        return fs.flatten(file_names)
    return walk(tree, ancestry)

print(find_files_paths(tree, 'co'))
    