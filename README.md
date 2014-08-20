Attribute Features
==================

attribute-features is a Python wrapper around Matlab/C++ attribute-based object
recognition code from http://vision.cs.uiuc.edu/attributes/.


Installing
----------

To use the python wrapper, you need to install Octave, Octave's img package, and
Python's oct2py package. Attribute features can then be extracted from image
by passing the filename to `attributes.detect`.


(Re-) Building MEX-Files
------------------------

In case of segmentation faults during detection, re-building MEX-files is the
first thing to try. Building MEX-files requires `mkoctfile` Octave utility, if
it's not part of default Octave package for your distribution it can be found
under octave-devel or such. There are four files to build:

* feature_extraction/code/textons/anigauss_mex.c (the result .mex then needs to
    be linked to feature_extraction/code/textons/anigauss.mex)
* feature_extraction/code/features.c
* feature_extraction/code/getNearest_mex.c
* feature_extraction/code/resize.cc


Running Prediction Demo
-----------------------

prediction_demo.m needs to know where the VOC 2008 data is. This data is best
downloaded from http://pascallin.ecs.soton.ac.uk/challenges/VOC/voc2008/VOCtrainval_14-Jul-2008.tar.
