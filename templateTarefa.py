# Demonstração das funções de string templates
from string import Template

def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format("Pyton Avançado", "Jéssica Temporal")
    print(frase)

    # Crie um template com placeholders
    templ = Template("Você está assistindo ${curso} com ${instrutora}")

    # Use o método substitute passando argumentos nomeados
    frase2 = templ.substitute(
        curso = "Python Avançado",
        instrutora = "Jéssica Temporal"
    )
    print(frase2)
    
    # Use o método substitute com um dicionário
    dados = {
        "curso": "Python Avançado",
        "instrutora": "Jéssica Temporal"
    }
    frase3 = templ.substitute(dados)
    print(frase3)

