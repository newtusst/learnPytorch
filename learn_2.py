import torch
import torchvision

x=torch.FloatTensor([1,2,3])
if isinstance(x,torch.Tensor):
    print('true')