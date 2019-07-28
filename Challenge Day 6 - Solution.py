import torch

a = torch.arange(1, 26)
a = torch.reshape(a,(5, 5))
print(a.tril())
