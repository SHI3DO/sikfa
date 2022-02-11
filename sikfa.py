import torch
import math

dtype = torch.float
device = torch.device('cpu')


def find(x: list, y: list, weightsnum: int, trainnum: int, learning_rate: float):
    x = torch.FloatTensor(x)
    y = torch.FloatTensor(y)

    coefficient_list = []
    for i in range(0, weightsnum):
        coefficient_list.append(torch.randn((), device=device, dtype=dtype, requires_grad=True))

    for k in range(trainnum):
        y_pred = 0
        for h in range(0, len(coefficient_list)):
            y_pred += coefficient_list[h]*x**h

        loss = (y_pred - y).pow(2).sum()
        if k % 100 == 99:
            print(k, loss.item())

        loss.backward()

        with torch.no_grad():
            for h in range(0, len(coefficient_list)):
                coefficient_list[h] -= learning_rate * coefficient_list[h].grad

                coefficient_list[h].grad = None

    for h in range(0, len(coefficient_list)):
        print(coefficient_list[h].item())