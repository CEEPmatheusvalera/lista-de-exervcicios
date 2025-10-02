print("Calculadora de Média")
num1 = float (input("Digite sua nota do primeiro trimestre:  "))
num2 = float (input("Digite sua nota do segundo trimestre:  "))
num3 = float (input("Digite sua nota do terceiro trimestre:  "))
premedia = num1 + num2 + num3
media = premedia / 3

if media >= 7:
    print(f"Paranéns sua média é {media} você passou de ano")
else: 
    print(f"Sua media é {media}você foi reprovado")
