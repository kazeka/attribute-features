# coding:utf-8

import cv2
import numpy
import oct2py
import os

def detect(fname):
    attribute_names = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   "attribute_names.txt")

    with open(attribute_names) as fp:
        cats = fp.readlines()

    cats = numpy.array([cat.strip() for cat in cats])
    cats.shape = (1, 64)

    oc = oct2py.Oct2Py()
    _ = oc.addpath(oc.genpath("./"))
    _ = oc.eval("pkg load image")

    codewords = oc.load_codewords()
    att_classifiers = oc.load_att_classifiers()

    im = oc.imread(fname)
    aspect_r = 1024.0 / im.shape[1]
    dim = (1024, int(im.shape[0] * aspect_r))

    if aspect_r > 1.:
        im = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)

    bbox = numpy.array([1, 1, im.shape[1], im.shape[0]])
    pred = oc.extract_predictions(im, bbox, att_classifiers, codewords)

    return sorted(zip(cats[pred > 0.25], pred[pred > 0.25]),
                  key=lambda x: x[1],
                  reverse=True)
