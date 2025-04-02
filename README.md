# DNA Encryption and Decryption

## Overview

This project demonstrates encryption and decryption using DNA sequences. It follows a structured approach to encode and decode data securely, showcasing how cryptographic techniques can be applied using DNA-inspired methods.

## Features

- Implements DNA-based encryption and decryption.
- Converts text to binary, modifies it using a secret key, and maps it to DNA sequences.
- Ensures secure data transformation using biological sequence patterns.

## Files in the Project

- `Encryption.py` – Encrypts the given input text into a DNA sequence.
- `Decryption.py` – Decrypts the DNA sequence back to the original text.

## Encryption Process

1. Convert the input text into its binary representation.
2. Apply a secret key by adding a number to each binary value.
3. Map the modified binary data to DNA sequences using predefined rules:
   - `00` → `A`
   - `01` → `T`
   - `10` → `C`
   - `11` → `G`
4. Output the encrypted DNA sequence.

## Decryption Process

1. Convert the DNA sequence back into binary using the reverse mapping:
   - `A` → `00`
   - `T` → `01`
   - `C` → `10`
   - `G` → `11`
2. Subtract the secret key from the binary values.
3. Convert the modified binary values back into their original text form.

## How to Run

### Prerequisites

- Python 3.x installed

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/jayavardhan4546/DNA-Encryption
   cd dna-encryption
   ```

2. Run the encryption script:
   ```bash
   python Encryption.py
   ```
   - Input the plaintext message.
   - Enter a secret key (integer).
   - The script will output the encrypted DNA sequence.

3. Run the decryption script:
   ```bash
   python Decryption.py
   ```
   - Input the encrypted DNA sequence.
   - Enter the secret key.
   - The script will output the original plaintext.

## Example Usage

### Encryption
```plaintext
Input: "HELLO"
Binary: 01001000 01000101 01001100 01001100 01001111
Secret Key: 2
Modified Binary: 01001010 01000111 01001110 01001110 01010001
DNA Sequence: TGCG GCTA CTAG CTAG ACTA
```

### Decryption
```plaintext
Input DNA Sequence: TGCG GCTA CTAG CTAG ACTA
Secret Key: 2
Binary: 01001000 01000101 01001100 01001100 01001111
Decrypted Output: "HELLO"
```

## Future Enhancements

- Adding more complex encryption techniques.
- Improving security measures.
- GUI implementation.

## License

This project is open-source. Feel free to use and modify it.
