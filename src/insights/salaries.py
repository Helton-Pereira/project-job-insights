from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    max_salary = 0
    list_of_jobs = read(path)

    for job in list_of_jobs:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            if int(job['max_salary']) > int(max_salary):
                max_salary = job['max_salary']

    return int(max_salary)
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    min_salary = 100000000
    list_of_jobs = read(path)

    for job in list_of_jobs:
        if job['min_salary'].isnumeric():
            if int(job['min_salary']) < int(min_salary):
                min_salary = job['min_salary']

    return int(min_salary)
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary_int = int(salary)

    except (KeyError, TypeError):
        raise ValueError
    
    if min_salary > max_salary:
        raise ValueError
    
    return min_salary <=  salary_int <= max_salary

    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    list = []


    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            pass
    return list

    raise NotImplementedError
