def len_moji(command):
    cmd, text = command.split()
    length = len(text)
    response = "文字列の長さは{}文字です".format(length)
    return response
