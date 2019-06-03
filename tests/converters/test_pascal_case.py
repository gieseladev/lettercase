from lettercase import dromedary_to_pascal_case, to_pascal_case


def test_dromedary_to_pascal_case():
    assert dromedary_to_pascal_case("helloWorld") == "HelloWorld"
    assert dromedary_to_pascal_case("_helloWorld") == "_HelloWorld"
    assert dromedary_to_pascal_case(" test") == " Test"


def test_to_pascal_case():
    assert to_pascal_case("hey_world") == "HeyWorld"
    assert to_pascal_case("HEY_WORLD") == "HeyWorld"
    assert to_pascal_case("Hey_World") == "HeyWorld"
    assert to_pascal_case("heyWorld") == "HeyWorld"
    assert to_pascal_case("HeyWorld") == "HeyWorld"
