from math import sin, cos,tan

print("----- DESCOBRIR SENO ,COSSENO E TANGENTE -----")
n = float(input("Digite um ângulo: "))

s = sin(n)
c = cos(n)
t = tan(n)

print("Seno {:.2f}º, Cosseno {:.2f}º, Tangente {:.2f}º".
      format(s, c, t))

