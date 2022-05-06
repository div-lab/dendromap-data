'''
    util.py - houses the code for random util functions
              for the data generation process
'''
import numpy as np
from scipy.cluster.hierarchy import linkage


class Dendrogram:
    def __init__(self, root=None):
        self.root = root
        self.cache = {}

    @property
    def leaves(self):
        leaves_key = "leaves"
        if leaves_key not in self.cache:
            self.cache[leaves_key] = get_leaves(self.root)

        return self.cache[leaves_key]

    def clear_cache(self):
        self.cache = {}

    def new_root(self, new_root):
        self.clear_cache()
        self.root = new_root

    @property
    def dict_format(self):
        return self.root

    def for_each_node(self, callback):
        def depth_first(parent):
            callback(parent)
            if parent["leaf"]:
                return
            for child in parent["children"]:
                depth_first(child)
        depth_first(self.root)

    def remove_attr(self, *name_attr):
        def _remove(node):
            for name in name_attr:
                if name in node:
                    del node[name]
        self.for_each_node(_remove)

    def export_as_json(self, filepath="default.json", indent=None):
        import json
        if "parent" in self.root:
            self.remove_attr("parent")
        with open(filepath, "w") as out:
            json.dump(self.root, out, indent=indent)


def get_leaves(parent):
    result = []

    def _leaves(node):
        if node["leaf"]:
            result.append(node)
            return
        for child in node["children"]:
            _leaves(child)
    _leaves(parent)
    return result


def make_node(data=None):
    dict_node = {}
    if data is not None:
        dict_node["data"] = data
    dict_node["leaf"] = False
    return dict_node


def hierarchical_cluster(features: np.ndarray, *args, **kwargs):
    clusters = linkage(features, *args, **kwargs)
    return clusters


def get_cluster_func(clusters):
    offset = len(clusters) + 1
    return lambda index: int(index - offset)


def merge_clusters_func(get_cluster_callback):
    return lambda node: [get_cluster_callback(node["data"][0]), get_cluster_callback(node["data"][1])]


def construct_dendrogram(clusters, connect_parent=False):
    get_cluster = get_cluster_func(clusters)
    # resolves which clusters to move from clusters
    get_merger = merge_clusters_func(get_cluster)

    def build(parent):
        resolve_merge = get_merger(parent)
        parent["children"] = [make_node(), make_node()]
        for i, child_idx in enumerate(resolve_merge):
            child = parent["children"][i]
            if connect_parent:
                child["parent"] = parent  # connect upwards
            child["merging_distance"] = round(parent["data"][2], 3)
            child["node_index"] = int(
                parent["data"][i])
            if child_idx < 0:
                child["instance_index"] = int(
                    parent["data"][i])
                child["leaf"] = True
            else:
                child["data"] = clusters[child_idx]
                parent["children"]
                build(child)

    dendrogram = Dendrogram()
    dendrogram.root = make_node(clusters[-1])
    dendrogram.root["node_index"] = len(clusters)*2

    if connect_parent:
        dendrogram.root["parent"] = None

    build(dendrogram.root)
    dendrogram.remove_attr("data")

    return dendrogram


def accumulate_up(leaves, callback):
    def _up(node):
        callback(node)
        if node["parent"] is None:
            return
        _up(node["parent"])

    _up(leaves)


def add_clusters_to_nodes(d: Dendrogram):
    cluster_key = "cluster"

    def init_arrays(node):
        node[cluster_key] = list()

    d.for_each_node(init_arrays)

    def merge(value):
        def _merge(node):
            node["cluster"].append(value)
        return _merge

    for leaf in d.leaves:
        accumulate_up(leaf, merge(leaf["instance_index"]))


def count_nodes(d: Dendrogram):
    node_count_key = "node_count"

    def init_zero_count(node):
        node[node_count_key] = 0

    d.for_each_node(init_zero_count)

    def count(node):
        node[node_count_key] += 1

    for leaf in d.leaves:
        accumulate_up(leaf, count)


if __name__ == "__main__":
    X = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[30])
    X = np.vstack((X, np.random.multivariate_normal(
        [0, 20], [[3, 1], [1, 4]], size=[20])))
    clusters = hierarchical_cluster(X, method="ward")
    d = construct_dendrogram(clusters, connect_parent=True)
    count_nodes(d)
    add_clusters_to_nodes(d)
    d.export_as_json("./test.json", indent=2)
