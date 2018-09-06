import importlib
from zutils.backend import optional_import

def test_direct_import():
    from skimage import io as skimage_io_di
    skimage_io_di.imread

def test_backend_import():
    skimage_io_bi = optional_import('skimage.io')
    skimage_io_bi.imread
