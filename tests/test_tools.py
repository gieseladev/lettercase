import lettercase
from lettercase import convert_iter_items, is_memo_converter, memo_converter, mut_convert_items, mut_convert_keys


def test_conversion_memo():
    memo_conv = lettercase.ConversionMemo()
    forward = memo_conv.get_memo("snake", "dromedary")
    backward = memo_conv.get_memo("dromedary", "snake")
    converter = lettercase.memo_converter(lettercase.get_converter("snake", "dromedary"), forward)

    assert converter("dromedary_case") == "dromedaryCase"

    assert forward["dromedary_case"] == "dromedaryCase"
    assert "dromedaryCase" not in forward

    assert backward["dromedaryCase"] == "dromedary_case"
    assert "dromedary_case" not in backward

    assert converter("dromedaryCase") == "dromedaryCase"
    assert backward["dromedaryCase"] == "dromedary_case"


def test_memo_converter():
    converter = lettercase.get_converter("snake", "dromedary")

    assert not is_memo_converter(converter)

    simple_memo = {}

    converter = memo_converter(converter, simple_memo)

    assert converter("snake_case") == "snakeCase"
    assert "snake_case" in simple_memo

    assert is_memo_converter(converter)


def test_convert_iter_items():
    iterable = iter(("helloThere", "this_too", "MaybeThis"))
    assert list(convert_iter_items(iterable, None, "snake")) == ["hello_there", "this_too", "maybe_this"]


def test_mut_convert_items():
    l = ["helloWorld", "_ThisIsWorking"]
    mut_convert_items(l, None, "snake_case")
    assert l == ["hello_world", "_this_is_working"]


def test_mut_convert_key():
    m = {"helloWorld": 5, "_ThisIsWorking": 3}
    mut_convert_keys(m, None, "snake_case")
    assert m == {"hello_world": 5, "_this_is_working": 3}
