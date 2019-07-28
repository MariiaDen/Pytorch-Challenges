import torch

x = torch.arange(12).view(2, 2, 3)
print(x[0, :1, :] @ x[1, :, :].t())
