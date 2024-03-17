month = int(input('Qual mes, de acordo com o número, você quer saber?'))

months_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12

}

for mes in months_dict.keys():
    if(month == months_dict[mes]):
        print(mes)