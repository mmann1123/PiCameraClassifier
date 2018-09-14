from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import numpy as np
import tensorflow as tf


def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()
    with open(model_file, "rb") as f:
	graph_def.ParseFromString(f.read())
    with graph.as_default():
	tf.import_graph_def(graph_def)
    return graph


