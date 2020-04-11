from __future__ import absolute_import, print_function

import tvm
from tvm import te
import numpy as np


# declare a matrix element-wise multiply
A = te.placeholder((1, ), name='A')
C = te.compute((1, ), lambda i: A[i], name='C')

s = te.create_schedule([C.op])
# lower will transform the computation from definition to the real
# callable function. With argument `simple_mode=True`, it will
# return you a readable C like statement, we use it here to print the
# schedule result.
print(tvm.lower(s, [A, C], simple_mode=True))
