STX = 'STX'
ETX = 'ETX'
DLE = 'DLE'
ESC = 'ESC'


def stuff_bytes(data):
    stuffed = [DLE, STX]
    for char in data:
        if char in (STX, ETX, DLE, ESC):
            stuffed.append("ESC")
            stuffed.append(char)
        else:
            stuffed.append(char)
    stuffed.append(DLE)
    stuffed.append(ETX)
    return stuffed


def unstuff_bytes(data):
    unstuffed = []
    i = 0
    while i != (len(data)):
        if data[i] == "ESC":
            next_char = data[i + 1]
            unstuffed.append(next_char)
            i = i + 2
        elif data[i] == DLE:
            i = i + 1
        elif data[i] == STX:
            i = i + 1
        elif data[i] == ETX:
            i = i + 1
        else:
            unstuffed.append(data[i])
            i = i + 1
    return unstuffed


def send(data):
    return stuff_bytes(data)


def receive(data):
    return unstuff_bytes(data)


def main():
    input_str = input("Enter your message (space between): ")
    message = input_str.split()

    sent_message = send(message)
    print("Sent message:", ' '.join(sent_message))

    received_message = receive(sent_message)
    received_str = ' '.join(received_message)

    print("Received message:", received_str)


if __name__ == "__main__":
    main()
