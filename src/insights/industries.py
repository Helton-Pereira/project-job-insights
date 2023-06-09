from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_of_jobs = read(path)
    list = []

    for job in list_of_jobs:
        if job['industry'] != '':
            if job['industry'] not in list:
                list.append(job['industry'])

    return list
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list = []

    for job in jobs:
        if job['industry'] == industry:
            list.append(job)
    return list
    raise NotImplementedError
