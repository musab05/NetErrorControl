import random


def calculate_parity_bits(data: str):
    n = len(data)
    r = 0

    while 2**r < (n + r + 1):
        r += 1

    hamming_code = []
    j = 0

    # Insert parity bits placeholders
    for i in range(0, n + r):
        if (i + 1) & i == 0:  # If i+1 is a power of 2 (parity bit positions)
            hamming_code.append('0')  # Placeholder for parity bits
        else:
            hamming_code.append(data[j])
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_position = 2**i - 1
        parity = 0
        for j in range(parity_position, len(hamming_code), 2 * (parity_position + 1)):
            parity ^= sum(int(bit) for bit in hamming_code[j:j + parity_position + 1]) % 2
        hamming_code[parity_position] = str(parity)

    return ''.join(hamming_code)


def send(data: str):
    hamming_code = calculate_parity_bits(data)
    while True:
        choice = input(
            "Enter choice (1 for without error, 2 for with error, 3 to exit): ")
        match choice:
            case "1":
                transmitwithoutError(hamming_code)
            case "2":
                transmitwithError(hamming_code)
            case "3":
                print("Exiting...")
                return
            case _:
                print("Invalid choice")


def transmitwithoutError(data: str):
    print(f"Message to be transmitted: {data}")
    receive(data)


def transmitwithError(data: str):
    error_index = random.randint(0, len(data) - 1)
    data_list = list(data)
    data_list[error_index] = '1' if data_list[error_index] == '0' else '0'
    error_data = ''.join(data_list)
    print(f"Message to be transmitted with error: {error_data}")
    receive(error_data)


def receive(data: str):
    n = len(data)
    r = 0

    while 2**r < n + 1:
        r += 1

    error_position = 0

    # Calculate parity to detect error position
    for i in range(r):
        parity_position = 2**i - 1
        parity = 0
        for j in range(parity_position, len(data), 2 * (parity_position + 1)):
            parity ^= sum(int(bit) for bit in data[j:j + parity_position + 1]) % 2
        if parity != 0:
            error_position += parity_position + 1

    if error_position != 0:
        corrected_code = list(data)
        corrected_code[error_position - 1] = '1' if data[error_position - 1] == '0' else '0'
        print(f"Error detected and corrected at position {error_position}")
        print("Corrected code:", ''.join(corrected_code))
    else:
        print("No error detected.")
        print("Received code:", data)


msg = input("Enter message in binary: ")

for char in msg:
    if char != '0' and char != '1':
        print("Invalid input")
        break
else:
    send(msg)
