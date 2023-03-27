from src.pre_built.sorting import sort_by

jobs_dict = [
    {'max_salary': 50000, 'min_salary': 20000, 'date_posted': '2022-10-06'},
    {'max_salary': 40000, 'min_salary': 10000, 'date_posted': '2022-01-02'},
    {'max_salary': 30000, 'min_salary': 5000, 'date_posted': '2022-10-21'},
]

jobs_dict_min_salary = [
    {'max_salary': 30000, 'min_salary': 5000, 'date_posted': '2022-10-21'},
    {'max_salary': 40000, 'min_salary': 10000, 'date_posted': '2022-01-02'},
    {'max_salary': 50000, 'min_salary': 20000, 'date_posted': '2022-10-06'},
]

jobs_dict_date_posted = [
    {'max_salary': 30000, 'min_salary': 5000, 'date_posted': '2022-10-21'},
    {'max_salary': 50000, 'min_salary': 20000, 'date_posted': '2022-10-06'},
    {'max_salary': 40000, 'min_salary': 10000, 'date_posted': '2022-01-02'},
]


def test_sort_by_criteria():
    sort_by(jobs_dict, 'max_salary')
    assert jobs_dict == jobs_dict
    sort_by(jobs_dict, 'min_salary')
    assert jobs_dict == jobs_dict_min_salary
    sort_by(jobs_dict, 'date_posted')
    assert jobs_dict == jobs_dict_date_posted
