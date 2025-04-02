def dna_to_binary(dna_input):
    # Define a reverse mapping between DNA bases and binary values
    reverse_dna_mapping = {
        'A': '00',
        'T': '01',
        'C': '10',
        'G': '11'
    }

    # Convert DNA to binary
    binary_sequence = ''.join(reverse_dna_mapping[dna_base] for dna_base in dna_input)

    return binary_sequence

# Example usage for multiple DNA sequences
dna_input = input("Enter space-separated DNA sequences: ")

# Split the input into individual DNA sequences
dna_sequences = dna_input.split()

# Convert each DNA sequence to binary
binary_results = [dna_to_binary(sequence) for sequence in dna_sequences]


def subtract_from_binary_line(line, number):
    binary_codes = line  # Split the line into individual binary codes
    result = []

    for binary_code in binary_codes:
        # Ensure that the input strings represent valid binary numbers
        if not all(bit in '01' for bit in binary_code):
            raise ValueError("Invalid binary input")

        # Convert binary string to integer, subtract the number, and then convert back to binary
        result.append(bin(int(binary_code, 2) - number)[2:])

    return result

# Example usage:
line_input = binary_results
number_to_subtract = int(input("Enter key: "))

try:
    result = subtract_from_binary_line(line_input, number_to_subtract)
    print("Resulting binary codes:", ' '.join(result))
except ValueError as e:
    print(f"Error: {e}")


def binary_to_string(binary_input):
    binary_values = binary_input
    ascii_characters = [chr(int(binary, 2)) for binary in binary_values]
    return ''.join(ascii_characters)

# Example usage
binary_input = result
string_result = binary_to_string(binary_input)
print(f"String representation: {string_result}")
