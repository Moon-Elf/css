def custom_hash_xor(input_str):
    hash_value_xor = 0
    final_hash_value_xor =''
    for char in input_str:
        hash_value_xor ^= ord(char)
        final_hash_value_xor += str(hash_value_xor)
    return int(final_hash_value_xor)

def custom_hash_prime(input_str):
    hash_value_prime = 0
    prime = 31
    
    for char in input_str:
        hash_value_prime = (hash_value_prime * prime + ord(char))
    
    return hash_value_prime

def combined_custom_hash(input_str):
    hash_value_xor = custom_hash_xor(input_str)
    hash_value_prime = custom_hash_prime(input_str)
    
    input_length = len(input_str)
    
    combined_hash = (hash_value_xor + hash_value_prime + input_length) % (1 << 32)
    
    return combined_hash

input_data = input("Enter plain text ")
hashed_value_combined = combined_custom_hash(input_data)

print(f"Combined Hashed value: {hashed_value_combined}")
