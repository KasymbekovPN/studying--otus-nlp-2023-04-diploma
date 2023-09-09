import torch


def get_torch_device():
    if torch.cuda.is_available():
        print(f'There are {torch.cuda.device_count()} GPU(s) available.')
        print(f'We will use the GPU: {torch.cuda.get_device_name(0)}')
        device = torch.device('cuda')
    else:
        print('No GPU available, using the CPU instead.')
        device = torch.device('cpu')
    return device
