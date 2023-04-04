# Definição de uma função que calcula o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Chamada da função fatorial e impressão do resultado
print("Fatorial de 5:", fatorial(5))

# Definição de uma classe Pessoa
class Pessoa:
    # Construtor da classe Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # Método que retorna uma string com informações da pessoa
    def info(self):
        return f"{self.nome} tem {self.idade} anos."
    
    # Método que atualiza a idade da pessoa
    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade

# Instanciação de um objeto da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Chamada do método info() do objeto pessoa1 e impressão do resultado
print(pessoa1.info())

# Chamada do método atualizar_idade() do objeto pessoa1 e atualização da idade
pessoa1.atualizar_idade(31)

# Chamada do método info() do objeto pessoa1 novamente e impressão do resultado atualizado
print(pessoa1.info())
