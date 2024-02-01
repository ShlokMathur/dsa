
import keyword


def search(key):
    arr = [1, 2, 3, 5, 7, 8, 9, 5]
    print("Length of the array:", len(arr))

    for i in range(len(arr)):
        if arr[i] == key:
            return f"Key found: {arr[i]}"
    
    return "Key not found"

# Example usage
key = int(input("Enter the key: "))
result = search(key)
print(result)
