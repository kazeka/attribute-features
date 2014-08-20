import cv2
import numpy
import oct2py

def detect(fname):
    with open("/Developer/litl/features/attribute_names.txt") as fp:
        cats = fp.readlines()

    cats = numpy.array([cat.strip() for cat in cats])
    cats.shape = (1, 64)

    oc = oct2py.Oct2Py()
    _ = oc.addpath(oc.genpath("./"))
    _ = oc.run("pkg load image")

    codewords = oc.load_codewords()
    att_classifiers = oc.load_att_classifiers()

    im = oc.imread(fname)
    apect_r = 1024.0 / im.shape[1]
    dim = (1024, int(im.shape[0] * apect_r))

    resized = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
    bbox = numpy.array([1, 1, resized.shape[1], resized.shape[0]])
    pred = oc.extract_predictions(resized, bbox, att_classifiers, codewords)

    return sorted(zip(cats[pred > 0.25], pred[pred > 0.25]),
                  key=lambda x: x[1],
                  reverse=True)
