import torch

X = torch.Tensor(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [6, 4, 2, 0]])
print(X.cumsum(dim=0))
