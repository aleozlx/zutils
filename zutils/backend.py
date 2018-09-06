import sys, re, heapq, logging, warnings
from importlib.util import find_spec, module_from_spec, LazyLoader
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] zutils: %(message)s', datefmt='%x %H:%M:%S')
logger = logging.getLogger('zutils')

specs = {
    'lycon': find_spec('lycon'),
    'skimage': find_spec('skimage'),
    'skimage.io': find_spec('skimage.io'),
    'skimage.transform': find_spec('skimage.transform'),
    'numpy': find_spec('numpy'),
    'cupy': find_spec('cupy')
}

candidate_heaps = dict()
rule_candidate = re.compile(r'^(?P<symbol>\w+)_(?P<priority>\d{2})(?P<backend>\w+)$')

def inject(symbol, f, priority):
    if symbol not in candidate_heaps:
        candidate_heaps[symbol] = list()
    heapq.heappush(candidate_heaps[symbol], (priority, f))

def candidate(symbol):
    def candidate_decorator(f):
        m = rule_candidate.match(f.__name__)
        if m and symbol == m.group('symbol'):
            if specs[m.group('backend')]:
                inject(symbol, f, int(m.group('priority')))
        else:
            raise Exception('Malformed candidate function name: {}'.format(f.__name__))
        return f
    return candidate_decorator

def optional_import(module):
    spec = specs.get(module)
    if spec:
        m = module_from_spec(spec)
        loader = LazyLoader(spec.loader)
        loader.exec_module(m)
        # Some modules may dump massive useless logs during import
        #   ... looking at skimage
        logging.getLogger().setLevel(logging.CRITICAL)
        sys.modules[module] = m
        logging.getLogger().setLevel(logging.INFO)
        logger.info('Found {}'.format(module))
        return m

def select(symbol, backend = None):
    """ Select implementation from specific backend or top of candidate heap. """
    if symbol in candidate_heaps:
        if backend is None:
            _, f = candidate_heaps[symbol][0]
            # f.__name__ = symbol
            return f
        else:
            # print(candidate_heaps[symbol][0][1].__name__)
            _, f = next(filter(lambda f_tuple: f_tuple[1].__name__.endswith(backend), candidate_heaps[symbol]))
            return f
    else:
        warnings.warn('Function `{}` is not supported by any backend on system.'.format(symbol), RuntimeWarning)

lycon = optional_import('lycon')
skimage = optional_import('skimage')
skimage_transform = optional_import('skimage.transform')
skimage_io = optional_import('skimage.io')
np = optional_import('numpy')
cp = optional_import('cupy')

@candidate('read_resize')
def read_resize_00lycon(fname, image_resize, greyscale=False):
    """ read_resize() with lycon backend. """
    if greyscale:
        return lycon.resize(lycon.load(fname, lycon.Decode.GRAYSCALE),
            width=image_resize[1], height=image_resize[0])[:,:,0]
    else:
        return lycon.resize(lycon.load(fname),
            width=image_resize[1], height=image_resize[0])

@candidate('read_resize')
def read_resize_01skimage(fname, image_resize, greyscale=False):
    return skimage_transform.resize(skimage_io.imread(fname, as_grey=greyscale), image_resize) * 255.0

@candidate('sp_mean')
def sp_mean_00cupy(image, segments):
    pass
