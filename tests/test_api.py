import os, sys
import numpy as np
from zutils.io import read_resize

ASSETS = lambda fname: os.path.join(os.path.dirname(__file__), 'assets', fname)

def test_read_resize_shape():
    assert read_resize(ASSETS('beach24.png'), (224,224)).shape == (224,224,3)

def test_read_resize_dtype():
    assert read_resize(ASSETS('beach24.png'), (224,224)).dtype == np.dtype('u1')
