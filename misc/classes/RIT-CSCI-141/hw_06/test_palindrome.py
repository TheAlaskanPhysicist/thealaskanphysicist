import palindrome


def test_is_palindrome(test_args: str, word: str, expected_result: bool) -> None:
    """
    A boolean function that tests if is_palindrome is returning the correct value.
    :param test_args: a string with the function and arguments being tested
    :param word: the word being tested by is_palindrome()
    :param expected_result: the expected result of is_palindrome(word)
    :return: None
    """
    _function_output = palindrome.is_palindrome(word)
    if _function_output == expected_result:
        print(test_args, 'passed')
    else:
        print(test_args, 'failed; expected', expected_result, 'but got', _function_output)


def run_tests() -> None:
    """
    Tests 10 different words for is_palindrome()
    :return: None
    """
    test_is_palindrome("is_palindrome(aabbaa)", "aabbaa", True)
    test_is_palindrome("is_palindrome(ababab)", "ababab", False)
    test_is_palindrome("is_palindrome(aabaa)", "aabaa", True)
    test_is_palindrome("is_palindrome(abbba)", "abbba", True)
    test_is_palindrome("is_palindrome(aaabbbbaaaa)", "aaabbbbaaaa", False)
    test_is_palindrome("is_palindrome(aaabbbbaaa)", "aaabbbbaaa", True)
    test_is_palindrome("is_palindrome(bbbaabbb)", "bbbaabbb", True)
    test_is_palindrome("is_palindrome(bbabab)", "bbabab", False)
    test_is_palindrome("is_palindrome(bbabaa)", "bbabaa", False)
    test_is_palindrome("is_palindrome(abbaaabba)", "abbaaabba", True)
    test_is_palindrome("is_palindrome(abbbbbba)", "abbbbbba", True)

    test_is_palindrome("is_palindrome(bbabbb)", "bbabbb", False)
    test_is_palindrome("is_palindrome(bbbabb)", "bbbabb", False)


if __name__ == "__main__":
    run_tests()
