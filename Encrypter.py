from pystyle import Colorate, Colors
import os

try:
# Limpiar consola
    os.system('cls' if os.name == 'nt' else 'clear')

# Funcion SAN
    def SAN(text):
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z = range(1, 28)
        letter_map = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 
                  'K': K, 'L': L, 'M': M, 'N': N, 'Ñ': Ñ, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 
                  'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}
        letter_map[' '] = ' '

        converted_text = []
        for char in text.upper():
            if char in letter_map:
                converted_text.append(str(letter_map[char]))
            else:
                converted_text.append(char)

        return ','.join(converted_text)

# Funcion SMAN
    def SMAN(text):
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z = range(1, 28)
        letter_map = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 
                  'K': K, 'L': L, 'M': M, 'N': N, 'Ñ': Ñ, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 
                  'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}
    
        text_length = len(text)
        result = []

        for char in text.upper():
            if char in letter_map:
                result.append(int(letter_map[char] * text_length))
            elif char == ' ':
                result.append(' ')

        return result

    
# Funcion SMPC
    def SMPC(text):
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z = range(1, 28)
        letter_map = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 
                  'K': K, 'L': L, 'M': M, 'N': N, 'Ñ': Ñ, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 
                  'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}

        converted_text = []
        for i, char in enumerate(text.upper(), start=1):
            if char in letter_map:
                converted_text.append(str(letter_map[char] * i))
            elif char == ' ':
                converted_text.append(' ')

        return converted_text
    
# Funcion SMAN + SMPC
    def SMAN_SMPC(text):
        sman_result = SMAN(text)
        smpc_result = [num * (i+1) for i, num in enumerate(sman_result)]
        
        return ','.join(map(str, smpc_result))
        

    print(Colorate.Horizontal(Colors.red_to_blue, "[1] SAN (Sistema Alfa Numerico)\n[2] SMAN (Sistema de Multiplicacion Alfa Numerico)\n[3] SMPC (Sistema de Multiplicacion por casilla)\n[4] SMAN + SMPC"))
    op = int(input(Colorate.Horizontal(Colors.green_to_blue, '=88> ')))
    if op == 1:
        text = input(Colorate.Horizontal(Colors.green_to_blue, "txt =88> "))
        converted_text = SAN(text)
        print(Colorate.Horizontal(Colors.green_to_white, f"Converted text: {converted_text}" ))

    elif op == 2:
        text = input(Colorate.Horizontal(Colors.green_to_blue, "txt =88> "))
        converted_text = SMAN(text)
        converted_text_str = ','.join(map(str, converted_text))
        print(Colorate.Horizontal(Colors.green_to_white, f"Converted text: {converted_text_str}" ))        

    elif op == 3:
        text = input(Colorate.Horizontal(Colors.green_to_blue, "txt =88> "))
        converted_text = SMPC(text)
        converted_text_str = ','.join(map(str, converted_text))
        print(Colorate.Horizontal(Colors.green_to_white, f"Converted text: {converted_text_str}" ))
    
    elif op == 4:
        text = input(Colorate.Horizontal(Colors.green_to_blue, "txt =88> "))
        SMAN_SMPC_CONVERTER = SMAN_SMPC(text)
        print(Colorate.Horizontal(Colors.green_to_white, f"Converted text: {SMAN_SMPC_CONVERTER}" ))

except Exception as e:
    print(f"Error as {e}")