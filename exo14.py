def facto (n):
    #fonction reccursive
    if n == 0:
        return 1
    else:
        return n * facto(n-1)
    
n=int(input("Entrez un nombre :"))
print(facto(n))  