import random
n = 25
array = []

for i in range(n):
    if random.randint(0,1):
        array.append(i)

print(array)

x_int = input("Aké čislo chcete vyhľadať ? ")
x = int(x_int)
print(x)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

result = binary_search(array, x)

if result != -1:
    print("Číslo sa nachádza na poradí", str(result))
else:
    print("Čislo sa v poli nenachádza")
