import torch
import numpy as np
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

data = [[1,2],[3,4]]
x_data = torch.tensor(data)

print("x_data: \n" ,x_data)

x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

rand_data = torch.rand(3,4)
print(f"Shape of tensor: {rand_data.shape}")
print(f"Datatype of tensor: {rand_data.dtype}")
print(f"Device tensor is stored on: {rand_data.device}")


#We load the FashionMNIST Dataset with the following parameters:
training_data = datasets.FashionMNIST(
    root="data", #root is the path where the train/test data is stored,
    train=True, #train specifies training or test dataset,
    download=True, #download=True downloads the data from the internet if it’s not available at root.
    transform=ToTensor()
)


transform and target_transform specify the feature and label transformations
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

'''We can index Datasets manually like a list: training_data[index]. We use matplotlib to visualize some samples in 
our training data.'''
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()