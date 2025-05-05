import random
import string

def generate_password(length=12):
    if length < 4: 
        raise ValueError("Password length must be at least 4 characters.")
    
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    all_characters = lower + upper + digits
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated Password:", generate_password(12))