from enum import Enum

class Hyper(Enum):
    UNKNOWN = -2
    AMBIGUOUS = -1
    SINGLE_GRAY = 0             # HW ----------- 2D
    GRAY = 1                    # NHW -------------- 3D
    SINGLE_RGB = 2              # HWK -------------- 3D
    RGB = 3                     # NHWK ----------------- 4D
    SINGLE_HYPER = 4            # HWK -------------- 3D
    HYPER = 4                   # NHWK ----------------- 4D
    SINGLE_SUPERPIXEL = 5       # P -------- 1D
    SINGLE_HYPER_SUPERPIXEL = 6 # PK ----------- 2D
    HYPER_SUPERPIXEL = 7        # NPK -------------- 3D

    @staticmethod
    def deduce(raw_shape, default = False):
        dim = len(raw_shape)
        if dim == 4:
            if raw_shape[-1] == 3:
                return Hyper.RGB
            else:
                return Hyper.HYPER
        elif dim == 3:
            if raw_shape[-1] == 3:
                return Hyper.SINGLE_RGB
            elif default:
                return Hyper.SINGLE_HYPER
            else:
                return Hyper.AMBIGUOUS
        elif dim == 2:
            if default:
                return Hyper.SINGLE_GRAY
            else:
                return Hyper.AMBIGUOUS
        elif dim == 1:
            return Hyper.SINGLE_SUPERPIXEL
        else:
            return Hyper.UNKNOWN

    @staticmethod
    def deduce_batch(raw_shape, default = False):
        dim = len(raw_shape)
        if dim == 4:
            if raw_shape[-1] == 3:
                return Hyper.RGB
            else:
                return Hyper.HYPER
        elif dim == 3:
            if default:
                return Hyper.GRAY
            else:
                return Hyper.AMBIGUOUS
        else:
            return Hyper.UNKNOWN

    @staticmethod
    def deduce_single(raw_shape, default = False):
        dim = len(raw_shape)
        if dim == 3:
            if raw_shape[-1] == 3:
                return Hyper.SINGLE_RGB
            else:
                return Hyper.SINGLE_HYPER
        elif dim == 2:
            if default:
                return Hyper.SINGLE_GRAY
            else:
                return Hyper.AMBIGUOUS
        elif dim == 1:
            return Hyper.SINGLE_SUPERPIXEL
        else:
            return Hyper.UNKNOWN
