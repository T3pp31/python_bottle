def showa_calculater(command):
    showa, str_year = command.split()
    try:

        year = int(str_year)
        if year > 1926 and year<1989:
            showa_year = year - 1926
            response = "西暦{}年は、昭和{}年です。".format(year, showa_year)
        elif year == 1989:
            response = "西暦{}年は、昭和最後の年で、昭和64年、平成元年です。".format(year)
        elif year ==1926:
            response = "西暦{}年は、昭和元年です。".format(year)
        else:
            response = "西暦{}年は、昭和ではありません。".format(year)

    except ValueError:
        response = "数値を指定してください。"
    return response
