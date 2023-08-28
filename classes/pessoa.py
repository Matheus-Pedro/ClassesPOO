class Pessoa: #Cria Classe pessoa
    def __init__(self, nome, cpf, idade, email, endereco): #Cria método construtor
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.endereco = endereco #Cria atributos do objeto

    def __str__(self): #Cria método "String". É usado para determinar um valor tipo string a classe, o que isso quer dizer? Quando chamado como em um 'print', retorna a string abaixo, em 'return'
        return f'\nNome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\nEmail: {self.email}\nEndereço: {self.endereco}\n'
