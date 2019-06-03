from lettercase import snake_to_screaming_snake_case, to_screaming_snake_case


# only need to test this conversion because all others are implemented using this
def test_snake_to_screaming_snake_case():
    assert snake_to_screaming_snake_case("snake_case") == "SNAKE_CASE"
    assert snake_to_screaming_snake_case("this") == "THIS"


def test_to_screaming_snake_case():
    assert to_screaming_snake_case("snake_case") == "SNAKE_CASE"
    assert to_screaming_snake_case("domDomDom") == "DOM_DOM_DOM"
    assert to_screaming_snake_case("DomDomDom") == "DOM_DOM_DOM"
    assert to_screaming_snake_case("Dom_Dom_Dom") == "DOM_DOM_DOM"
