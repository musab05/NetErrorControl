import random


def send(message):
  block_size = int(input("Enter block size: "))
  sender_checksum = checksum(message, block_size)
  sender_msg = message + sender_checksum
  while True:
    choice = input(
        "Enter choice (1 for without error, 2 for with error, 3 to exit): ")
    match choice:
      case "1":
        transmitwithoutError(sender_msg, block_size)
      case "2":
        transmitwithError(sender_msg, block_size)
      case "3":
        print("Exiting...")
        return
      case _:
        print("Invalid choice")


def checksum(data: str, block_size: int) -> str:
  n = len(data)
  if n % block_size != 0:
    pad_size = block_size - (n % block_size)
    data = '0' * pad_size + data

  def binary_addition(a: str, b: str) -> str:
    sum = int(a, 2) + int(b, 2)
    max_length = max(len(a), len(b))
    binary_sum = bin(sum)[2:].zfill(max_length)
    if len(binary_sum) > max_length:
      carry = binary_sum[:-max_length]
      result = binary_sum[-max_length:]
      return bin(int(result, 2) + int(carry, 2))[2:].zfill(max_length)
    return binary_sum.zfill(max_length)

  result = data[:block_size]

  for i in range(block_size, len(data), block_size):
    next_block = data[i:i + block_size]
    result = binary_addition(result, next_block)

  return ones_complement(result.zfill(block_size))


def ones_complement(data: str) -> str:
  return ''.join('1' if bit == '0' else '0' for bit in data)


def transmitwithoutError(data: str, block_size: int):
  print(f"Message received is: {data}")
  receive(data, block_size)


def transmitwithError(data: str, block_size: int):
  error_index = random.randint(0, len(data) - 1)
  data_list = list(data)
  data_list[error_index] = '1' if data_list[error_index] == '0' else '0'
  error_data = ''.join(data_list)
  print(f"Message received is: {error_data}")
  receive(error_data, block_size)


def receive(data: str, block_size):
  receiver_checksum = checksum(data, block_size)
  if receiver_checksum.count('0') == block_size:
    print(True)
  else:
    print(False)


msg = input("Enter message in binary: ")

if all(char in '01' for char in msg):
  send(msg)
else:
  print("Invalid input")
