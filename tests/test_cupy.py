import os, sys
import numpy as np
from numpy import testing as npt
from zutils.backend import select
from zutils.io import read_resize

ASSETS = lambda fname: os.path.join(os.path.dirname(__file__), 'assets', fname)

def test_sp_mean_cupy():
    sp_mean = select('sp_mean', backend='cupy')
    im_test = read_resize(ASSETS('beach24.png'), (224,224))[...,0]
    segments = np.load(ASSETS('beach_sp.npy'))
    y = sp_mean(im_test, segments)
    y_true = np.load(ASSETS('beach_sp_mean.npy'))
    npt.assert_allclose(y, y_true)
