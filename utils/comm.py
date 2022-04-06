def read(uart):
    start = False
    end = False

    while end:
        byte_read = uart.read(1)
        if byte_read is None:
            continue
        if byte_read == b"<":
            message = []
            start = True
            continue
        if start:
            if byte_read == b">":
                end = True      
                return message
            else:
                message.append(chr(byte_read[0]))

