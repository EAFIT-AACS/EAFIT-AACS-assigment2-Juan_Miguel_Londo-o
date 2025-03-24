from ALGORITHM_1_LFCO_2025_JMLC import generate_valid_strings, generate_invalid_strings

def pda_accepts(input_string):
    stack = []
    for char in input_string:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if stack and stack[-1] == 'a':
                stack.pop()
            else:
                return False  # Rechazado
    return len(stack) == 0  # Aceptado si la pila está vacía

def test_pda():
    test_strings = generate_valid_strings() + generate_invalid_strings()
    accepted = [s for s in test_strings if pda_accepts(s)]
    rejected = [s for s in test_strings if not pda_accepts(s)]

    print("\nResultados del PDA:")
    for s in accepted:
        print(f"Aceptado: {s}")
    for s in rejected:
        print(f"Rechazado: {s}")
    
    return accepted

if __name__ == "__main__":
    test_pda()
