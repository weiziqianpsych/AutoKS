#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import rcParams
import networkx as nx


def draw_pic(graph, filename=None):
    nx.draw(graph,
            node_size=300,
            node_color='#ffebcd',
            edge_color='#7ab8cc',
            with_labels=True)
    rcParams['font.sans-serif'] = ['SimHei']
    rcParams['font.family'] = 'sans-serif'
    if not filename:  # draw & show only
        plt.show()
    else:  # save as filename.png, and do not show picture
        plt.savefig("{}.png".format(filename), format="PNG", dpi=300)
