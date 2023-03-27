from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_dict = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in jobs_dict:
        assert 'salary' in job
        assert 'title' in job
        assert 'type' in job
        assert 'salário' not in job
