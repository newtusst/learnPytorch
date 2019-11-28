import torch
import torchvision
import numpy as np

print(torch.__version__)
print(torch.cuda.is_available())
print(torchvision.__version__)


a=torch.ones(5)
print(a)
print(a.size())
b=a.numpy()
print(b)
print(b.shape)
c=torch.from_numpy(b)
np.add(b,1,out=b)
print(b)
print(c)

if torch.cuda.is_available():
    a=a.cuda()
    print(a)
