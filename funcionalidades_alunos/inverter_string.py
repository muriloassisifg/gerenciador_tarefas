def executar():
    print("--- Inversor de Texto ---")
    texto_original = input("Por favor, digite um texto para inverter: ")

    texto_invertido = texto_original[::-1]

    print(f"O texto '{texto_original}' invertido é '{texto_invertido}'.")

if __name__ == "__main__":
    executar()