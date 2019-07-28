import matplotlib.pyplot as plt
import torch

x = torch.linspace(1, 10, 100)
y = torch.sin(x)
plt.plot(x.numpy(), y.numpy())
