def test_input_text(expected_result: object, actual_result: object) -> int:
    assert expected_result == actual_result, \
        f'expected {expected_result}, got {actual_result}'

if __name__ == "__main__":
    test_input_text(8,11)
    test_input_text(11,11)
    test_input_text(11,15)