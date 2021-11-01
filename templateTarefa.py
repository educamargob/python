# Demonstração das funções de string templates
from string import Template

def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format("Pyton Avançado", "Jéssica Temporal")
    print(frase)

    # Crie um template com placeholders
    templ = "Você está assistindo ${0} com ${1}"
    # Use o método substitute passando argumentos nomeados

    # Use o método substitute com um dicionário