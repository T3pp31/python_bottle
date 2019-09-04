def gengo_calculater(command):
    gengo,str_year = command.split()

    try:
        year = int(str_year)

        if year == 2019:
            response = "西暦{}年は平成３１年か令和元年です。".format(year)
        elif year <2019 and year >1989:
            gengo_year = year - 1989
            response = "西暦{}年は平成{}年です。".format(year,gengo_year)
        elif year == 1989:
            response = "西暦{}年は昭和６３年か、平成元年です。".format(year)
        elif year <1989 and year >=1926:
            gengo_year = year - 1926
            response = "西暦{}年は昭和{}年です。".format(year,gengo_year)
        elif year <=1925 and year>=1912:
            gengo_year = year - 1912
            response ="西暦{}年は大正{}年です。".format(year,gengo_year)
        elif year <=1911 and year >=1868:
            gengo_year = year -1868
            response ="西暦{}年は明治です。".format(year)
        else:
            response ="これ以上はわからん！"
    except ValueError:
        response = "数値を指定してください。"

    return response