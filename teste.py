from math import hypot
cto = float(input("Digite o cateto oposto "))
cta = float(input("Digite o cateto adjacente "))
tangente1 = hypot(cto, cta)
print("A medidade da tangente é {}".format(tangente1))