import pytest
from app.business_logic import *


test_dir = "app/tests/data_for_test"
words_for_test = ["питон", "питон", "flask", "python", "питон"]


def test_get_names_of_files():
    actual_result = get_count_of_files(test_dir)
    expected_result = 4
    assert actual_result == expected_result


def test_get_common_and_rare_words():
    actual_result = get_common_and_rare_words(words_for_test)
    expected_result = {"common_word": "питон", "rarest_word": "flask"}
    assert actual_result == expected_result


def test_get_average_word_len():
    actual_result = get_average_word_len(words_for_test)
    expected_result = 5
    assert actual_result == expected_result


def test_get_phonetic_analysis():
    actual_result = get_phonetic_analysis(words_for_test)
    expected_result = (9, 17, 9)
    assert actual_result == expected_result


def test_group_word_info():
    actual_result = group_word_info("питон")
    expected_result = {
        "len of word": 1,
        "count of vowels": 2,
        "count of consonants": 3,
        "syllables": 2,
    }
    assert actual_result == expected_result
