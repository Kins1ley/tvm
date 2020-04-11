import tvm
from tvm import relay

import numpy as np

from tvm.contrib.download import download_testdata
from tvm.relay.frontend.pytorch import get_graph_input_names

# PyTorch imports
import torch
import torchvision

model = torch.load("model/net_008.pth")

for k, v in model.items():
    print(k)
    print(v)

input_shape = [1, 24, 24]
input_data = torch.randn(input_shape)
scripted_model = torch.jit.trace(model, input_data)

#input_shape = [1, 28, 28]
#input_data = torch.randn(input_shape)
#scripted_model = torch.jit.trace(model, input_data).eval()

#from torchvision import transforms

#transform = transforms.ToTensor()

