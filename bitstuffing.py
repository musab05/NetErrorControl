STX = '0111111110'
ETX = '0111111110'
BIT_TO_INSERT = '0'


def bit_stuffing(data):
  stuffed_data = [STX]
  consecutive_ones = 0

  for bit in data:
    if bit == '1':
      consecutive_ones += 1
    else:
      consecutive_ones = 0
    stuffed_data.append(bit)

    if consecutive_ones == 5:
      stuffed_data.append(BIT_TO_INSERT)
      consecutive_ones = 0
  stuffed_data.append(ETX)
  return ''.join(stuffed_data)


def bit_unstuffing(data):
  unstuffed_data = []
  consecutive_ones = 0
  i = 0

  while i < len(data):
    bit = data[i]

    if bit == '1':
      consecutive_ones += 1
    else:
      consecutive_ones = 0

    unstuffed_data.append(bit)

    if consecutive_ones == 5 and i + 1 < len(data) and data[
        i + 1] == BIT_TO_INSERT:
      i += 1
      consecutive_ones = 0
    if consecutive_ones == 8 and i + 1 < len(data) and data[
        i + 1] == BIT_TO_INSERT:
      i += 1
      unstuffed_data = unstuffed_data[:-9]
    i += 1

  return ''.join(unstuffed_data)


def main():
  input_str = input("Enter a binary string (without spaces): ")

  stuffed_message = bit_stuffing(input_str)
  print("Bit-stuffed message:", stuffed_message)

  unstuffed_message = bit_unstuffing(stuffed_message)
  print("Bit-unstuffed message:", unstuffed_message)


if __name__ == "__main__":
  main()
