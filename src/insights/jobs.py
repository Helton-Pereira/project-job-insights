from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    list_dict = []
    with open(path, encoding='utf-8') as file:
        jobs_reader = csv.DictReader(file, delimiter=',')
        for job in jobs_reader:
            list_dict.append(job)
        return list_dict

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    list = []
    list_of_jobs = read(path)

    for job in list_of_jobs:
        if job['job_type'] not in list:
            list.append(job['job_type'])
    return list

    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list = []
    for job in jobs:
        if job['job_type'] == job_type:
            list.append(job)
    return list

    raise NotImplementedError
