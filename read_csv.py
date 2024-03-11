import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';') #objeto iterable
        header = next(reader) # Se guarda el header, es decir, los titulos de cada columna
        #print(header) # Opcional
        data = []
        for row in reader:
            iterable = zip(header, row) #se crea un objeto iterable que cada row se convierte en tuplas compuesta por par (titulo y valor)
                                        # row 1: (titulo, valor), (titulo, valor), (titulo, valor), ...
            population_dict = {key: value for key, value in iterable} # Por medio de dictionary comprehension creo un diccionario del iterable
            #print(population_dict)
            data.append(population_dict) #Por cada iteración (row) del reader, se adiciona a la lista data el diccionario creado
    return data

'''
filtro de job title
sume por cada job title y año el salary en usd

{   'id': '0',
    'work_year': '2020',
    'experience_level': 'MI',
    'employment_type': 'FT',
    'job_title': 'Data Scientist',
    'salary': '70000',
    'salary_currency': 'EUR',
    'salary_in_usd': '79833',
    'employee_residence': 'DE',
    'remote_ratio': '0',
    'company_location': 'DE',
    'company_size': 'L'
}
'''
