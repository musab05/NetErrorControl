import random


def crc(message: str, polynomial: str) -> str:
  message = message + '0' * (len(polynomial) - 1)
  divisor = int(polynomial, 2)
  message = int(message, 2)
  divisor = int(polynomial, 2)

  while (message.bit_length() >= divisor.bit_length()):
    shift = message.bit_length() - divisor.bit_length()
    message ^= divisor << shift

  remainder = format(message, '0' + str(len(polynomial) - 1) + 'b')
  return remainder


def send(message: str):
  polynomial = input("Enter polynomial (e.g., '1101'): ")
  remainder = crc(message, polynomial)
  sender_msg = message + remainder
  while True:
    choice = input(
        "Enter choice (1 for without error, 2 for with error), 3 to exit): ")
    match choice:
      case "1":
        transmitwithoutError(sender_msg, polynomial)
      case "2":
        transmitwithError(sender_msg, polynomial)
      case "3":
        print("Exiting...")
        return
      case _:
        print("Invalid choice")


def transmitwithoutError(data: str, polynomial: str):
  print(f"Message received is: {data}")
  receive(data, polynomial)


def transmitwithError(data: str, polynomial: str):
  error_index = random.randint(0, len(data) - 1)
  data_list = list(data)
  data_list[error_index] = '1' if data_list[error_index] == '0' else '0'
  error_data = ''.join(data_list)
  print(f"Message received is: {error_data}")
  receive(error_data, polynomial)


def receive(data: str, polynomial: str):
  divisor = int(polynomial, 2)
  message = int(data, 2)

  while message.bit_length() >= divisor.bit_length():
    shift = message.bit_length() - divisor.bit_length()
    message ^= divisor << shift

  remainder = format(message, '0' + str(len(polynomial) - 1) + 'b')

  if int(remainder, 2) == 0:
    print(remainder)
    print("Message is valid.")
  else:
    print(remainder)
    print("Message is invalid.")


msg = input("Enter message in binary: ")

for char in msg:
  if char != '0' and char != '1':
    print("Invalid input")
    break
else:
  send(msg)
