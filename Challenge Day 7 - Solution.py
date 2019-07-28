import torch

X = torch.Tensor([[1, 2], [3, 4]])
Y = torch.Tensor([[5, 6], [7, 8]])
Z = X.matmul(Y)
print(Z)
