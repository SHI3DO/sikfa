import torch

dtype = torch.float
device = torch.device('cpu')


def find(x: list, y: list, weightsnum: int, trainnum: int, learning_rate: float):
    x2 = torch.FloatTensor(x)
    y2 = torch.FloatTensor(y)

    coefficient_list = []
    for i in range(0, weightsnum):
        coefficient_list.append(torch.randn((), device=device, dtype=dtype, requires_grad=True))

    for k in range(trainnum):
        y_pred = 0
        for h in range(0, len(coefficient_list)):
            y_pred += coefficient_list[h] * x2 ** h

        loss = (y_pred - y2).pow(2).sum()
        if k % 10000 == 9999:
            print(k, loss.item())

        if not torch.isfinite(loss):
            print('non-finite loss, ending training')
            learning_rate = learning_rate / 10
            print(f'next learning_rate = {learning_rate}')
            print('restarting...')
            find(x, y, weightsnum, trainnum, learning_rate)
            exit(1)

        loss.backward()

        with torch.no_grad():
            for h in range(0, len(coefficient_list)):
                coefficient_list[h] -= learning_rate * coefficient_list[h].grad

                coefficient_list[h].grad = None

    print(f'loss = {loss.item()}')

    return coefficient_list
