from lettercase import darwin_to_snake_case, dromedary_to_snake_case, pascal_to_snake_case, to_snake_case, \
    screaming_snake_to_snake_case


def test_dromedary_to_snake_case():
    assert dromedary_to_snake_case("snakeCase") == "snake_case"
    assert dromedary_to_snake_case("_snakeCase") == "_snake_case"
    assert dromedary_to_snake_case("roleID") == "role_id"
    assert dromedary_to_snake_case("__className") == "__class_name"
    assert dromedary_to_snake_case("c") == "c"
    assert dromedary_to_snake_case("") == ""


def test_pascal_to_snake_case():
    assert pascal_to_snake_case("CamelCase") == "camel_case"
    assert pascal_to_snake_case("_CamelCase") == "_camel_case"
    assert pascal_to_snake_case("__CamelCase") == "__camel_case"


def test_screaming_snake_to_snake_case():
    assert screaming_snake_to_snake_case("SNAKE_CASE") == "snake_case"
    assert screaming_snake_to_snake_case("THIS") == "this"


def test_darwin_to_snake_case():
    assert darwin_to_snake_case("Darwin_Case") == "darwin_case"


def test_to_snake_case():
    assert to_snake_case("snake_case") == "snake_case"
    assert to_snake_case("domDomDom") == "dom_dom_dom"
    assert to_snake_case("DomDomDom") == "dom_dom_dom"
    assert to_snake_case("Dom_Dom_Dom") == "dom_dom_dom"
