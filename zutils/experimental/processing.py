import numpy as np

def sp_backfill(u, segments):
    N_segments = np.max(segments)+1
    u = np.resize(u, N_segments)
    r = np.empty(segments.shape)
    for m in range(N_segments):
        r[segments == m] = u[m]
    return r
