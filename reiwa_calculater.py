def reiwa_calculater(command):
    reiwa,str_year = command.split()
    try:

        year = int(str_year)
        if year > 2019:
            reiwa_year = year - 2019
            response = "西暦{}年は令和{}年です。".format(year,reiwa_year)
        elif year ==2019:
            response = "西暦{}年は令和元年です。".format(year)
        else:
            response = "西暦{}年は令和ではありません。".format(year)

    except ValueError:
        response = "数値を指定してください"

    return response