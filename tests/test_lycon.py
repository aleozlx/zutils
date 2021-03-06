import os, sys
import numpy as np
from zutils.backend import select

ASSETS = lambda fname: os.path.join(os.path.dirname(__file__), 'assets', fname)

def test_read_resize_lycon_shape():
    read_resize = select('read_resize', backend='lycon')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert im_test.shape == (224,224,3)

def test_read_resize_lycon_dtype():
    read_resize = select('read_resize', backend='lycon')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert im_test.dtype == np.dtype('u1')

def test_read_resize_lycon_range():
    read_resize = select('read_resize', backend='lycon')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))
    assert 178 < im_test.mean() < 180
