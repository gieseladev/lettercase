from lettercase import LetterCase, detect_letter_case


def test_detect_letter_case():
    assert detect_letter_case("test_one") == {LetterCase.SNAKE}
    assert detect_letter_case("testOne") == {LetterCase.DROMEDARY}

    assert detect_letter_case("____testOne") == {LetterCase.DROMEDARY}

    assert detect_letter_case("Sneaky_Darwin_Case") == {LetterCase.DARWIN}

    assert detect_letter_case("UPPER_CASE") == {LetterCase.UPPER_SNAKE}

    assert detect_letter_case("ambiguous") == {LetterCase.SNAKE, LetterCase.DROMEDARY}
