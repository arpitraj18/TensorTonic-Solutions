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
    """
    ### LESSONS LEARNED / ERROR LOG:
    
    1. SYNTAX: 
       - Mistake: Using {} and () like JavaScript/C++.
       - Fix: Python uses colons (:) and indentation to define code blocks.
    
    2. SCALAR VS LIST MULTIPLICATION:
       - Mistake: 0 * len(values) -> returns the integer 0.
       - Fix: [0] * len(values) -> returns a list of zeros [0, 0, 0...].
    
    3. ELEMENT-WISE COMPARISON:
       - Mistake: np.min(array, limit) -> interpret 'limit' as an 'axis' and crashed.
       - Fix: np.minimum(array, limit) -> compares each element to the limit.
    
    4. THE FLOOR & BOUNDARY PROBLEM:
       - Mistake: Forgetting that max_value / width equals num_bins (out of bounds).
       - Fix: Use np.floor() to get the index and np.minimum(..., num_bins - 1) 
              to clamp the maximum value into the top bin.
    """
