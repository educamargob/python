# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "Isto é uma string"
    print(s)

    # Tente juntar os dois
    #print (s + b)

    # Bytes e strings precisam ser apropridamente enconded e 
    print(s + b.decode('utf-8'))
    
    # faça o encode da String como utf-32
    print(s.encode('utf-32') + b)