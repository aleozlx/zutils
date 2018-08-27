# zutils

Machine Learn / Computer Vision processing utility

* Able to read / resize / preprocess / postprocess in a documented, consistent, well-tested and performant manner.
* Provides building blocks for operationalized processing pipeline.
* Depends on several image processing or computer vision backends.
  * Select optimal (in logarithmic time) packages available.
  * Rely on testing to achieve sustainability.
* Lazy backend import.
* Source code is written in a way that won't make pylint scream.
* Big fan on open source community. To hell with proprietary b.s.

# Modules

## Usage

1. Check that zutils is exporting all APIs that you need  
  `python -m pytest -v tests/test_api.py`
2. Import APIs from `ztuils` module, like `from zutils import read_resize`

To check API backend selection:

`python -m zutils`

## zutils.io

