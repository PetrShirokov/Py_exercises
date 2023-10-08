from hexlet import fs
import copy


def change_owner(node, owner):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    new_meta['owner'] = owner
    if fs.is_file(node):
        return fs.mkfile(name, new_meta)
    children = fs.get_children(node)
    new_children = list(map(lambda child: change_owner(child, owner), children))
    new_tree = fs.mkdir(name, new_children, new_meta)
    return new_tree


def dfs_print_meta(node):
    print(fs.get_meta(node))
    if fs.is_file(node):
        return
    children = fs.get_children(node)
    list(map(dfs_print_meta, children))

tree = fs.mkdir('/', 
[fs.mkdir('etc', [
    fs.mkfile('bashrc', {'owner': 'bas'}),
    fs.mkfile('consul.cfg', {'owner': 'rvv'})
    ]),
fs.mkfile('hexletrc', {'owner': 'lau'})],
{'owner': 'root'})

print(tree)
new_tree = change_owner(tree, 'shpu')
print(new_tree)
print(dfs_print_meta(tree))
print()
print(dfs_print_meta(change_owner(tree, 'shpu')))