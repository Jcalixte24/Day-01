a=int(input("entrez un nommbre :"))
b=int(input("entrez un nommbre :"))
c=int(input("entrez un nommbre :"))
if a>b and a>c :
    print(a,"est le plus grand")
elif b>a and b>c :
    print(b,"est le plus grand")
elif c>a and c>b :
    print(c,"est le plus grand")
elif a==b and a>c :
    print(a,"et",b,"sont les plus grand")
elif a==c and a>b :
    print(a,"et",c,"sont les plus grand")
elif b==c and b>a :
    print(b,"et",c,"sont les plus grand")
else :
    print("ils sont tous égaux")