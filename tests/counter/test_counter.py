from src.pre_built.counter import count_ocurrences


def test_counter_should_return_the_correct_number_of_word_searched():
    assert count_ocurrences('data/jobs.csv', 'Python') == 1639
