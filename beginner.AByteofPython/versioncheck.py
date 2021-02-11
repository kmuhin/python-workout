import sys
import warnings

if sys.version_info[0] < 4:
    warnings.warn("Need another version of Python", RuntimeWarning)
else:
    print("Good version")
