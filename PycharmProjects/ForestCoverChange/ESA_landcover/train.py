

from __future__ import print_function
from __future__ import division
import os
import sys
import torch
import argparse
from model import *
from training_functions import *

if __name__ == '__main__':

    # parse
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', dest='function', default='train_net')
    parser.add_argument('--images', dest='images', default=None)
    parser.add_argument('--labels', dest='labels', default=None)
    parser.add_argument('--block_size', dest='block_size', type=int, default=256)
    parser.add_argument('--input_size', dest='input_dim', type=int, default=64)
    parser.add_argument('--workers', dest='workers', type=int, default=4)
    parser.add_argument('-p', '--pretrained_model', dest='pre_model', default=None)
    parser.add_argument('--save_data', dest='save_data', default=None)
    parser.add_argument('-s', '--save_dir', dest='save_dir', default=None)
    parser.add_argument('--summary_dir', dest='summary_dir', default=None)
    parser.add_argument('-b', '--batch_size', dest='batch_size', type=int, default=4)
    parser.add_argument('-l', '--lr', dest='lr', type=float, default=1e-3)
    parser.add_argument('-log', '--log_after', dest='log_after', type=int, default=10)
    parser.add_argument('-c', '--cuda', dest='cuda', type=int, default=0)
    parser.add_argument('--device', dest='device', type=int, default=0)
    args = parser.parse_args()

    function = args.function
    images = args.images
    labels = args.labels
    block_size = args.block_size
    input_dim = args.input_dim
    workers = args.workers
    pre_model = args.pre_model
    save_data = args.save_data
    save_dir = args.save_dir
    sum_dir = args.summary_dir
    batch_size = args.batch_size
    lr = args.lr
    log_after = args.log_after
    cuda = args.cuda
    device = args.device

    function_to_call = eval(function)
    net = UNet(input_channels=13, num_classes=23)

    # model, images, labels, block_size, input_dim, workers, pre_model,save_dir,
    #       sum_dir, batch_size, lr, log_after, cuda, device
    function_to_call(model=net, images=images, labels=labels, block_size=block_size, input_dim=input_dim,
                     workers=workers, pre_model=pre_model, save_data=save_data, save_dir=save_dir,
                     sum_dir=sum_dir, batch_size=batch_size, lr=lr, log_after=log_after, cuda=cuda, device=device)
















