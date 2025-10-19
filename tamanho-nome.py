
nome = input("Qual seu primeiro nome? ")
tamanho = len(nome)
print(f"Seu nome tem {tamanho} letras.")

if(tamanho <= 4):
    print("Seu nome é curto.")
elif(tamanho >= 5 and tamanho <= 6):
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
