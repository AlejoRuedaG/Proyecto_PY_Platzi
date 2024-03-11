def func_sum_salaries(data, job):
    salaries_2020 = 0
    salaries_2021 = 0
    salaries_2022 = 0
    filter_2020 = list(filter(lambda x: x['work_year'] == '2020', data))
    filter_job_2020 = list(filter(lambda x: x['job_title'] == job, filter_2020))
    filter_2021 = list(filter(lambda x: x['work_year'] == '2021', data))
    filter_job_2021 = list(filter(lambda x: x['job_title'] == job, filter_2021))
    filter_2022 = list(filter(lambda x: x['work_year'] == '2022', data))
    filter_job_2022 = list(filter(lambda x: x['job_title'] == job, filter_2022))
    for item in filter_job_2020:
        salaries_2020 += int(item['salary_in_usd'])
    for item in filter_job_2021:
        salaries_2021 += int(item['salary_in_usd'])
    for item in filter_job_2022:
        salaries_2022 += int(item['salary_in_usd'])

    return salaries_2020, salaries_2021, salaries_2022
