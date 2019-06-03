from lettercase import pascal_to_dromedary_case, snake_to_dromedary_case, to_dromedary_case


def test_snake_to_dromedary_case():
    assert snake_to_dromedary_case("hello_world") == "helloWorld"
    assert snake_to_dromedary_case("_hello_world") == "_helloWorld"
    assert snake_to_dromedary_case("test") == "test"


def test_pascal_to_dromedary_case():
    assert pascal_to_dromedary_case("HelloWorld") == "helloWorld"
    assert pascal_to_dromedary_case("_HelloWorld") == "_helloWorld"
    assert pascal_to_dromedary_case("Test") == "test"


def test_to_dromedary_case():
    assert to_dromedary_case("hey_world") == "heyWorld"
    assert to_dromedary_case("HEY_WORLD") == "heyWorld"
    assert to_dromedary_case("Hey_World") == "heyWorld"
    assert to_dromedary_case("heyWorld") == "heyWorld"
    assert to_dromedary_case("HeyWorld") == "heyWorld"
