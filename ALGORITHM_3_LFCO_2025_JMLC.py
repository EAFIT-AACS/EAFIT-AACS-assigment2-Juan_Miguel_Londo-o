from ALGORITHM_2_LFCO_2025_JMLC import pda_accepts, test_pda

def build_derivation_tree(string):
    if not pda_accepts(string):
        return "No es una cadena válida."
    tree = ["S"]
    for char in string:
        if char == 'a':
            tree.append("aSb")
        elif char == 'b':
            tree.pop()
            tree.append("ε")
    return " -> ".join(tree)

if __name__ == "__main__":
    accepted_strings = test_pda()
    
    print("\nÁrboles de derivación:")
    for s in accepted_strings:
        print(f"Para '{s}': {build_derivation_tree(s)}")
