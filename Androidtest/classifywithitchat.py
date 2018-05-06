from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import itchat, time
import scripts.label_image as li
from itchat.content import *
import argparse
import sys
import time
import numpy as np
import tensorflow as tf

itchat.auto_login(hotReload=True)
def receive(msg):
    msg.download(msg.fileName)
    file_name = ""
    model_file = "tf_files/retrained_graph.pb"
    label_file = "tf_files/retrained_labels.txt"
    input_height = 224
    input_width = 224
    input_mean = 128
    input_std = 128
    input_layer = "input"
    output_layer = "final_result"

    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="msg.fileName")
    parser.add_argument("--graph", help="tf_files/retrained_graph.pb")
    parser.add_argument("--labels", help="name of file containing labels")
    parser.add_argument("--input_height", type=int, help="input height")
    parser.add_argument("--input_width", type=int, help="input width")
    parser.add_argument("--input_mean", type=int, help="input mean")
    parser.add_argument("--input_std", type=int, help="input std")
    parser.add_argument("--input_layer", help="name of input layer")
    parser.add_argument("--output_layer", help="name of output layer")
    args = parser.parse_args()

    args.graph="tf_files/retrained_graph.pb"
    args.image=msg.fileName
    if args.graph:
        model_file = args.graph
    if args.image:
        file_name = args.image

    graph = li.load_graph(model_file)
    t = li.read_tensor_from_image_file(file_name,
                                    input_height=input_height,
                                    input_width=input_width,
                                    input_mean=input_mean,
                                    input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess:
        start = time.time()
        results = sess.run(output_operation.outputs[0],
                        {input_operation.outputs[0]: t})
        end=time.time()
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = li.load_labels(label_file)

    print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))

    for i in top_k:
        print(labels[i], results[i])
    itchat.send(labels[top_k[0]], toUserName='filehelper')
    itchat.send(str(results[top_k[0]]), toUserName='filehelper')
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
        
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])        
def download_files(msg):
    receive(msg)    
    return '%s received' % msg['Type']

itchat.run()