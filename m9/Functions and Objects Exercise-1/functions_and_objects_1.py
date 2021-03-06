#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, f):
    for [i, j] in enumerate(L):
        L[i] = f(j)
    return L

def abs(n_inp):
    if n_inp >= 0:
        return n_inp
    return n_inp*-1

def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
