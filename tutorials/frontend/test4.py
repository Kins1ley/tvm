import tvm
from tvm import relay

import numpy as np

from tvm.contrib.download import download_testdata
from tvm.relay.frontend.pytorch import get_graph_input_names

# PyTorch imports
import torch
import torchvision

######################################################################
# Load a pretrained PyTorch model
# -------------------------------
model_name = 'resnet18'
model = getattr(torchvision.models, model_name)(pretrained=True)

model_dict = model.state_dict()

# We grab the TorchScripted model via tracing
input_shape = [1, 3, 224, 224]
input_data = torch.randn(input_shape)
scripted_model = torch.jit.trace(model, input_data).eval()

for k, v in model_dict.items():
    print(k)
