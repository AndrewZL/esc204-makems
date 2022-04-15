def read(uart):
    message_started = False
    while True:
        byte_read = uart.read(1)
        if byte_read is None:
            continue
        
        if byte_read == b"<":
            message = []
            message_started = True
            continue

        if message_started:
            if byte_read == b">":
                message_parts = "".join(message).split(",")
                message_type = message_parts[0]
                message_started = False            
                if message_parts[0] == "R":
                    message=message_parts[1]
                    print(f"read {message}")
                break
            else:
                message.append(chr(byte_read[0]))
            
def signal(uart):
    byte_read = uart.read(1)
    if byte_read == b'z':
        print(byte_read)
        return True
    return False
        