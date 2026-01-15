peso = float(input('Peso:'));
altura = float(input('Altura:'));

imc = peso / (altura ** 2);

print (f'Seu IMC é {imc:.2f}');

def Classificar_imc(imc):

 if imc <= 15.9:
    print('Magreza grave!');
 elif  16.0 <= imc <=  16.9:
    print('Magreza Moderada');
 elif   17.0 <= imc <=  18.4:
    print('Magreza Leve');
 elif   18.5 <= imc <= 24.9:
    print('Peso Ideal');
 elif  25.0 <= imc <= 29.9:
    print('Sobrepeso');
 elif  30.0 <= imc <= 34.9:
    print('Obesidade Grau I');
 elif  35.0 <= imc <= 39.9:
    print('Obesidade Grau II');
 else: 
    print('Obesidade Grau III');
 