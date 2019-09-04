def heisei_calculater(command):
    heisei, str_year = command.split()
    try:

        year = int(str_year)
        if year > 1989 and year < 2019:
            heisei_year = year - 1989
            response = "西暦{}年は、平成{}年です。".format(year, heisei_year)
        elif year == 2019:
            response = "西暦{}年は、平成最後の年で平成31年、令和元年です".format(year)
        elif year ==1989:
            response = "西暦{}年は、平成元年です。".format(year)
        else:
            response = "西暦{}年は、平成ではありません。".format(year)
    except ValueError:
        response = "数値を指定してください。"
    return response
