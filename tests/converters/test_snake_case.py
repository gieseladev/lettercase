from lettercase.converters.snake_case import dromedary_to_snake_case


def test_dromedary_to_snake_case() -> None:
    assert dromedary_to_snake_case("snakeCase") == "snake_case"
    assert dromedary_to_snake_case("roleID") == "role_id"
    assert dromedary_to_snake_case("ClassName") == "class_name"
    assert dromedary_to_snake_case("c") == "c"
    assert dromedary_to_snake_case("C") == "c"
    assert dromedary_to_snake_case("") == ""
