import os,sys
tempdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,tempdir+"/heterocl")

import heterocl as hcl

hcl.init()

A = hcl.placeholder((10,))
B = hcl.placeholder((10,))

def quantization(A):

    return hcl.compute(A.shape, lambda x: hcl.tanh(A[x]), "B")

sm = hcl.create_scheme([A], quantization)
sm_B = quantization.B