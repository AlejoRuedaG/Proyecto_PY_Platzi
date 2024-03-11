import read_csv
import utils
import charts

print('*** SISTEMA DE MONITOREO DE SALARIOS EN DATA SCIENCE ***\n')
opciones = set()

result = read_csv.read_csv('ds_salaries.csv')
for item in result:
    opciones.add(item['job_title'])
print('Digite el cargo a consultar de las siguientes opciones:\n')
for element in opciones:
    print(element)

job = input('select a job: ').title()
suma2020, suma2021, suma2022 = utils.func_sum_salaries(result, job)

labels = ['2020', '2021', '2022']
values = [suma2020, suma2021, suma2022]

charts.generate_bar_chart(labels, values)
