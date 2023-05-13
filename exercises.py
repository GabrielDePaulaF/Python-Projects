#A-)
c=float(input('escreva a temperatura em Graus Celsius:\n'))
f=(9*c+160)/5
print('Resultado da temperatura em Fahrenheit: ',f)

#B-)
f=float(input ('escreva a temperatura em Graus Fahrenheit:\n'))
c=(f-32)*(5/9)
print('Resultado da temperatura em Celsius: ',c)

#C-)
r=float(input('Digite o Raio da lata:'))
a=float(input('Digite a Altura da lata:'))
v=3.14159*r**2*a
print('O volume da lata é igual a:',v)

#D-)
t=float(input('Digite o tempo da viagem:\n'))
v=float(input('Digite a velocidade:\n'))
d=v*t
l=d/12
print('Velocidade:  {}km/h | Tempo da viagem: {}H | Distancia Total: {}Km | Litros gastos: {}L'.format(v,t,d,l))

#E-)
v=float(input('Digite o valor da prestação:\n'))
p=float(input('Tempo da prestação:\n'))
t=float(input('Informe a taxa da prestação:\n'))
a=(v+(v*t/100)*p)
print('Valor da prestação em atraso é de R$:',a)


#F-)
a=float(input('Digite um valor para A:\n'))
b=float(input('Digite um valor para B:\n'))
b2=b
b=a
a=b2
print('Valor de A:{}  |  Valor de B: {}'.format(a,b))

#G-)
a=float(input('Digite um valor para A:\n'))
b=float(input('Digite um valor para B:\n'))
c=float(input('Digite um valor para C:\n'))
d=float(input('Digite um valor para D:\n'))
ab=a+b
ac=a+c
ad=a+d
bc=b+c
bd=b+d
cd=c+d
avb=a*b
avc=a*c
avd=a*d
bvc=b*c
bvd=b*d
cvd=c*d
print('|A+B= {}|A+C= {}|A+D= {}|B+C= {}|B+D= {}|C+D= {}|\n'.format(ab,ac,ad,bc,bd,cd))
print('|A*B= {}|A*C= {}|A*D= {}|B*C= {}|B*D= {}|C*D= {}|'.format(avb,avc,avd,bvc,bvd,cvd))

#H-)
c=float(input('Digite o comprimento da caixa:\n'))
l=float(input('Digite a largura da caixa:\n'))
a=float(input('Digite a altura da caixa:\n'))
v=c*l*a
print('O volume da caixa é igual a:',v)

#I-)
a=int(input('Digite o numero que deseja:\n'))
x=a**2
print('O valor do numero digitado ao quadrado é: ',x)

#J-)
a=int(input('Digite o numero que deseja para A:\n'))
b=int(input('Digite o numero que deseja para B:\n'))
a2=a**2
b2=b**2
r=b2-a2
print('Diferença entre os dois valores digitados elevado ao quadrado:',r)

#K-)
c=float(input('Digite o valor do dolar:\n'))
d=float(input('Quantos dolares você possui:\n'))
b=d/c
print('Valor do dolar pra brl:',b)

#L-)
c=float(input('Digite o valor do BRL:\n'))
d=float(input('Quantos reais você possui:\n'))
l=(2/10)
p=d*l
print('Você possui:',p)

#M-)
a=int(input('Digite um valor para A:\n'))
b=int(input('Digite um valor para B:\n'))
c=int(input('Digite um valor para C:\n'))
a2=a**2
b2=b**2
c2=c**2
r=b2+a2+c2
print('A soma dos três numeros elevados ao quadrado é:',r)

#N-)
a=int(input('Digite um valor para A:\n'))
b=int(input('Digite um valor para B:\n'))
c=int(input('Digite um valor para C:\n'))
r=a+b+c
r=r**2
print('A soma dos numeros elevados ao quadrado é:',r)

#O-)
a=int(input('Digite um valor para A:\n'))
b=int(input('Digite um valor para B:\n'))
c=int(input('Digite um valor para C:\n'))
d=int(input('Digite um valor para D:\n'))
p=a+c
s=b+d
print('O valor para a variante P é de:',p)
print('O valor para a variante S é de:',s)

#P-)
sm=float(input('Digite quanto você recebe mensalmente:\n'))
pr=float(input('Digite o reajuste:\n'))
ns=sm+sm*pr/100
print('O novo salario será de:',ns)

#Q-)
r=float(input('Digite o raio:\n'))
a=3.14159*r**2
print('A circuferencia é de:',a)

#R-)
a=int(input('Quantidade de votos validos para candidato A:\n'))
b=int(input('Quantidade de votos validos para candidato B:\n'))
c=int(input('Quantidade de votos validos para candidato C:\n'))
vn=int(input('Quantidade de votos nulos:\n'))
vb=int(input('Quantidade de votos em branco:\n'))
vta=a+b+c
te=vta+vn+vb
print('total de eleitores:',te)
perct = (vta*100)/te
perca = (a*100)/te
percb = (b*100)/te
percc = (c*100)/te
percbra = (vb*100)/te
print("votos validos para o candidato A=",perca)
print("votos validos para o candidato b=",percb)
print("votos validos para o candidato c=",percc)
print("quantidade dos votos brancos em relação de eleitores=",percbra)


#S-)
a=float(input('Digite o valor para A:\n'))
b=float(input('Digite o valor para B:\n'))
r=a+b
r2=a-b
r3=a*b
r4=a/b
print('SOMA= {} | SUBTRAÇÃO= {} | MULTIPLICAÇÃO= {} | DIVISÃO= {}'.format(r,r2,r3,r4))

#T-)
d=float(input('Digite a distancia:\n'))
t=float(input('Digite o tempo:\n'))
v=(d*1000)/(t*60)
print('A velocidade em m/s foi de:',v)

#U-)
r=float(input('Digite o raio:\n'))
v=(4/3)*3.14159*(r**3)
print('O volume da esfera é de:',v)


