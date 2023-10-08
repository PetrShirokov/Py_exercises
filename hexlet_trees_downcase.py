from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile
import copy


def downcase_file_names(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        new_name = name.lower()
        return mkfile(new_name, new_meta)
    children = get_children(node)
    new_children = list(map(downcase_file_names, children))
    new_tree = mkdir(name, new_children, new_meta)
    return new_tree

tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])
new_tree = downcase_file_names(tree)
print(tree)
print(new_tree)