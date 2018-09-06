import os, sys
import numpy as np
from zutils.io import select

ASSETS = lambda fname: os.path.join(os.path.dirname(__file__), 'assets', fname)

def test_read_resize_skimage_shape():
    read_resize = select('read_resize', backend='skimage')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert im_test.shape == (224,224,3)

def test_read_resize_skimage_dtype():
    read_resize = select('read_resize', backend='skimage')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert im_test.dtype == np.dtype('u1')

def test_read_resize_skimage_range():
    read_resize = select('read_resize', backend='skimage')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert 178 < im_test.mean() < 180
