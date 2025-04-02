def string_to_binary(input_string):
    binary_representation = ' '.join(format(ord(char), '08b') for char in input_string)
    return binary_representation

# Example usage
user_input = input("Enter a string: ")
binary_result = string_to_binary(user_input)
print(f"Binary representation: {binary_result}")

def add_to_binary_line(line, number):
    result = []
    current_code = ""

    for char in line:
        if char in '01':
            current_code += char
        elif char.isspace():
            if current_code:
                # Ensure that the input strings represent valid binary numbers
                if not all(bit in '01' for bit in current_code):
                    raise ValueError("Invalid binary input")

                # Convert binary string to integer, add the number, and then convert back to binary
                result.append(bin(int(current_code, 2) + number)[2:])
                current_code = ""
        else:
            raise ValueError("Invalid character in the input")

    if current_code:
        if not all(bit in '01' for bit in current_code):
            raise ValueError("Invalid binary input")
        result.append(bin(int(current_code, 2) + number)[2:])

    return result

# Example usage:
line_input = binary_result
number_to_add = int(input("Enter the secret key No.: "))

try:
    result = add_to_binary_line(line_input, number_to_add)
    print("Resulting binary codes:", ' '.join(result))
    a = result
except ValueError as e:
    print(f"Error: {e}")


def binary_to_dna(binary_input):
    # Define a mapping between binary values and DNA bases
    dna_mapping = {
        '00': 'A',
        '01': 'T',
        '10': 'C',
        '11': 'G'
    }

    # Ensure the binary input length is a multiple of 2
    if len(binary_input) % 2 != 0:
        binary_input = '0' + binary_input  # pad with a leading zero if needed

    # Convert binary to DNA
    dna_sequence = ''.join(dna_mapping[binary_input[i:i+2]] for i in range(0, len(binary_input), 2))

    return dna_sequence

# Example usage for multiple binary codes
binary_input = a

# Split the input into individual binary codes
binary_codes = binary_input

# Convert each binary code to DNA format
dna_results = [binary_to_dna(code) for code in binary_codes]

# Display the results
for i, result in enumerate(dna_results):
    print(result +" ", end="")
