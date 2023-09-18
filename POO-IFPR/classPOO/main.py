from classPOO.pessoa.pessoa import Pessoa
from classPOO.aluno.aluno import Aluno
from classPOO.funcionario.funcionario import Funcionario
from classPOO.produto.produto import Produto
from classPOO.veiculo.veiculo import Veiculo
from classPOO.conta_a_pagar.conta_a_pagar import ContaAPagar
from classPOO.computador.computador import Computador
from classPOO.smartphone.smartphone import Smartphone
from classPOO.eletrodomestico.eletrodomestico import Eletrodomestico
from classPOO.pagamento.pagamento import Pagamento #Importou todas classPOO

p1 = Pessoa('Matheus Pedro', 12345678901, 16, 'matheuscapriolipedro@gmail.com', 'Rua Antônio Chemin, 28, São Gabriel')#Nessas linhas abaixo, os Objetos são criados, definindo os valores dos atributos
f1 = Funcionario('Matheus', 12345678901, 16, 'matheuscapriolipedro@gmail.com', 'Rua Antônio Chemin, 28, São Gabriel', 1200.00, 'Desenvolvedor', 122, 'TI')
a1 = Aluno('Matheus Pedro', 12345678901, 16, 'matheuscaprolipedro@gmail.com', 'Rua Antônio Chemin, 28, São Gabriel', 'Informática', 2022, 2)
pr1 = Produto('ESP32', 12.50, 69.00, 110, 10)
v1 = Veiculo('Audi', 'TT', '2.5', 400, 3.7, 2020, 60000, 'Cupê', 'Automático', 'Gasolina')
cp1 = ContaAPagar('Matheus Pedro', 'Banco do Brasil', 1_000, 10092023)
c1 = Computador(3.5, 8, 165, 'Windows', 3000.50)
s1 = Smartphone('Preto', 2023, '14 Pro Max', 'iPhone', 9_500.00)
e1 = Eletrodomestico('Aspirador de Pó', 'Limpar a sala', 'Smart 1300W ABS03 220V', 'Electrolux', 390.00)
pa1 = Pagamento('Pix', 'Ronan', 'Matheus', 5072007, 1_000.00) #Definiu todos objetos 

print(p1)
print(f1)
print(a1)
print(pr1)
print(v1)
print(cp1)
print(c1)
print(s1)
print(e1)
print(pa1) #Imprimiu todos objetos