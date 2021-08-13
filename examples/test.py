from betterpython.Eye import modify
@modify(int)
def __add__(self, other):
    if isinstance(other,str):
        return self + int(other)
    else:
        return - (-other)
print(10 + '1')