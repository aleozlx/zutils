# zutils

Machine Learning / Computer Vision processing utility

[![Travis CI Build Status](https://travis-ci.org/aleozlx/zutils.svg?branch=master)](https://travis-ci.org/aleozlx/zutils)

* Able to read / resize / preprocess / postprocess batches of images in a documented, consistent, tested and performant manner.
* Provides building blocks for operationalized processing pipeline.
* Depends on several image processing or computer vision backends.
  * Select optimal (in logarithmic time) packages available.
  * Rely on testing to achieve sustainability.
* Lazy backend import to accelerate launch time.
* Source code is written in a way that won't make pylint scream.

## Usage

1. Check that zutils is exporting all APIs that you need  
  `python -m pytest -v tests/test_api.py`
2. Import APIs from `ztuils` module, like `from zutils.io import read_resize`

To check API backend selection:

`python -m zutils`

## Modules

### zutils.io

* `read_resize(fname, image_resize, greyscale=False)`

## TODO

* [ ] refine documentation
