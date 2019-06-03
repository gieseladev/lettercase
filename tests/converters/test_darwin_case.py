from lettercase import snake_to_darwin_case, to_darwin_case


# only need to test this conversion because all others are implemented using this
def test_snake_to_darwin_case():
    assert snake_to_darwin_case("snake_case") == "Snake_Case"
    assert snake_to_darwin_case("this") == "This"


def test_to_darwin_case():
    assert to_darwin_case("dom_dom_dom") == "Dom_Dom_Dom"
    assert to_darwin_case("DOM_DOM_DOM") == "Dom_Dom_Dom"
    assert to_darwin_case("domDomDom") == "Dom_Dom_Dom"
    assert to_darwin_case("DomDomDom") == "Dom_Dom_Dom"
