# Write your solution here
def times_ten(start_index: int, end_index: int):
    D = {}
    for i in range(start_index,end_index+1):
        D[i]= i*10
    return D



if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)