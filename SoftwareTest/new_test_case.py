import pytest

import scrabble

@pytest.mark.one
def test_userInput_game():
    phrase(["cabbage])
    expected = 14
    scrabble.game()
    output = get_display_output()
    assert output == 14


def phrase(param):
    pass

@pytest.mark.two
def test_userInput_sucess():
    response = phrase("watermelon")

    assert response == True, "test passed"

@pytest.mark.three
def test_userInput_failure():
    response = phrase("@pple")

    assert response == True, "test failed"

@pytest.mark.four
def test_userInput_game():
    phrase(["CABBAGE])
    expected = 14
    scrabble.game()
    output = get_display_output()
    assert output == 14


@pytest.mark.five

def test_userInput_game():
    phrase(["CABBAGE])
            expected = 14
    scrabble.game()
    output = get_display_output()
    assert output == 14
