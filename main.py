from importmysql import insertdata


def month_year_iter2(start_month, start_year, end_month, end_year):
    for year in range(start_year,end_year+1):
        month_start = 1
        month_end = 13
        if year == end_year:
            month_end = end_month+1
        if year == start_year:
            month_start = start_month
        for month in range(month_start, month_end):
            f = str(year)+str('{:02d}'.format(month))
            insertdata("2317", f)


month_year_iter2(1, 1992, 5, 2018)
