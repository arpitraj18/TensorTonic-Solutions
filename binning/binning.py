import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values=np.array(values)
    min=np.min(values)
    max=np.max(values)
    if min==max:
        return [0]*len(values)
    else:
        w=(max-min)/num_bins
    bin=np.minimum(np.floor((values-min)/w),num_bins-1)
    return bin.tolist()