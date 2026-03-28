import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x=np.array(x)
    mean= float(np.mean(x))
    median=float(np.median(x))

    counts = Counter(x)
    max_freq = max(counts.values())
    #thsi part of the cocde will work if there is a tie in the provided values such as[1,1,2,2]
    #mode = float(min(val for val, freq in counts.items() if freq == max_freq))

    #in case there is no such tie
    candidates = [val for val, freq in counts.items() if freq == max_freq]
    mode = float(candidates[0])
    return mean, median, mode
    pass