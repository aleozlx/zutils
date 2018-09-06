import os, sys
import numpy as np
from zutils.io import read_resize

ASSETS = lambda fname: os.path.join(os.path.dirname(__file__), 'assets', fname)

def test_read_resize_shape():
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert im_test.shape == (224,224,3)

def test_read_resize_dtype():
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert im_test.dtype == np.dtype('u1')

def test_read_resize_range():
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert 178 < im_test.mean() < 180
