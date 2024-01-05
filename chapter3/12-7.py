array = list(map(int, input()))

if sum(array[:len(array)//2]) == sum(array[len(array)//2:]):
    print("LUCKY")

else:
    print("READY")