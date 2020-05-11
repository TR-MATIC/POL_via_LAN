# packages
from lib_class import Climatix

# defs

# const

# code
pol69u = Climatix()
pol69u.load_config()
pol69u.climatix_auth()
nodes_list_1 = pol69u.explore_view_node("NgAAAAAA", 0)
for node_1 in nodes_list_1:
    nodes_list_2 = pol69u.explore_view_node(node_1, 4)
    for node_2 in nodes_list_2:
        nodes_list_3 = pol69u.explore_view_node(node_2, 8)
        for node_3 in nodes_list_3:
            pol69u.explore_view_node(node_3, 12)
