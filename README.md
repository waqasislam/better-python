<p align="center">
  <img src="https://raw.githubusercontent.com/waqasislam/better-python/main/docs/logo.png">
</p>

---

A fork of [CodeWithSwastik's](https://github.com/CodeWithSwastik) better-python. (will be renamed)

Better-python is a libary designed to add more functionality to python3.
Check some examples below.

### Installation

```bash
pip3 install git+https://github.com/waqasislam/better-python.git --upgrade
```

### Example

```python
from betterpython import modify
@modify(str, list, tuple)
def __invert__(self):
  return self[::-1]
```

### Same example in fprbiddenfruit

```python
from forbiddenfruit import curse
def __invert__(self):
  return self[::-1]

curse(str,'__invert__',__invert__)
curse(list,'__invert__',__invert__)
curse(tuple,'__invert__',__invert__)import torch

x = torch.eye(3, requires_grad=True)
y = torch.tensor([[2.0,0,-2.0]], requires_grad=True)
z = y.matmul(x).sum()
z.backward()

print(x.grad)  # dz/dx
print(y.grad)  # dz/dy
```

## Want to modify strings fast?

Better-python is perfect at that. You can make your own modifier functions.

### UWU Example

```python
from betterpython import modify
@modify(str)
@property
def uwu(self):
    self.replace('l', 'w')
print('hello'.uwu())
#--OUTPUT:
#'hewwo'

```

All though this looks small its just a little example of what better-python can do.

### Running tests

```bash
echo "in progress"
```

### TODO (updated)

- ~~ Add more list functionality

### Important Notice!

This is not a repo to replace CodeWithSwastik's better-python. It will probably be made into a pull request into the original github repo. [Original](https://github.com/CodeWithSwastik/better-python) Join the TCA discord server: https://discord.gg/TXF3hBj
