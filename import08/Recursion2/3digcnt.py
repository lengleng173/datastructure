def digcnt(num):
    if num==0:
        return 0
    return num%10+digcnt(num//10)

print(digcnt(173))