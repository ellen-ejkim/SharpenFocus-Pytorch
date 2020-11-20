from torchvision import transforms, datasets
import torchvision

def get_mean_var_classes(name):
    name = name.split('_')[-1]
    if name == 'cifar10':
       return (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616), 10
    if name == 'cifar100':
       return (0.5071, 0.4865, 0.4409), (0.2673, 0.2564, 0.2762), 100
    elif name == 'stl10':
       return (0.4467, 0.43980, 0.4066), (0.2603, 0.2565, 0.2712), 10
    return None


def get_datasets(name):
    mean, var, num_classes = get_mean_var_classes(name)
    if name == 'cifar10':
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.RandomCrop(32, padding=4),
            torchvision.transforms.RandomHorizontalFlip(),
            torchvision.transforms.RandomRotation(15),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean, var)])
        transform_test = torchvision.transforms.Compose([torchvision.transforms.ToTensor(), torchvision.transforms.Normalize(mean, var)])
        train = datasets.CIFAR10(root='./data/', train=True, download=False, transform=transform_train)
        test = datasets.CIFAR10(root='./data/', train=False, download=False, transform=transform_test)
    elif name == 'cifar100':
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.RandomCrop(32, padding=4),
            torchvision.transforms.RandomHorizontalFlip(),
            torchvision.transforms.RandomRotation(15),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean, var)])
        transform_test = torchvision.transforms.Compose([torchvision.transforms.ToTensor(), torchvision.transforms.Normalize(mean, var)])
        train = datasets.CIFAR100(root='./data/', train=True, download=False, transform=transform_train)
        test = datasets.CIFAR100(root='./data/', train=False, download=False, transform=transform_test)
    elif name == 'stl10':
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.RandomCrop(96, padding=4),
            torchvision.transforms.RandomHorizontalFlip(),
            torchvision.transforms.RandomRotation(15),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean, var)])
        transform_test = torchvision.transforms.Compose([ torchvision.transforms.ToTensor(), torchvision.transforms.Normalize(mean, var)])
        train = datasets.STL10(root='./data/', split='train', download=False, transform=transform_train)
        test = datasets.STL10(root='./data/', split='test', download=False, transform=transform_test)
    return train, test, num_classes

