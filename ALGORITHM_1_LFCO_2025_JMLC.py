import random

def generate_valid_strings(n=2):
    valid_strings = []
    for _ in range(n):
        s = ""
        count = random.randint(1, 5)
        for _ in range(count):
            s = "a" + s + "b"
        valid_strings.append(s)
    return valid_strings

def generate_invalid_strings(n=2):
    invalid_strings = []
    for _ in range(n):
        length = random.randint(2, 6)
        s = "".join(random.choice("ab") for _ in range(length))
        if s.count("a") != s.count("b"):
            invalid_strings.append(s)
    return invalid_strings

if __name__ == "__main__":
    accepted = generate_valid_strings()
    rejected = generate_invalid_strings()
    print("Cadenas aceptadas:", accepted)
    print("Cadenas rechazadas:", rejected)
