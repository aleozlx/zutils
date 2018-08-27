import sys, re, heapq, logging
from importlib.util import find_spec, module_from_spec, LazyLoader
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(message)s', datefmt='%x %H:%M:%S')
logger = logging.getLogger('zutils')

specs = {
    'lycon': find_spec('lycon')
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
        sys.modules[module] = m
        return m

def select(symbol):
    if symbol in candidate_heaps:
        _, f = candidate_heaps[symbol][0]
        f.__name__ = symbol
        return f
    else:
        logger.warning('Function `{}` is not supported by any backend on system.'.format(symbol))

lycon = optional_import('lycon')

@candidate('read_resize')
def read_resize_00lycon(fname, image_resize, greyscale=False):
    """ read_resize() with lycon backend. """
    if greyscale:
        return lycon.resize(lycon.load(fname, lycon.Decode.GRAYSCALE),
            width=image_resize[1], height=image_resize[0])[:,:,0]
    else:
        return lycon.resize(lycon.load(fname),
            width=image_resize[1], height=image_resize[0])
