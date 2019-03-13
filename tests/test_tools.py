import lettercase
from lettercase import convert_iter_items, memo_converter, mut_convert_items, mut_convert_keys


def test_conversion_memo():
    memo = lettercase.ConversionMemo("dromedary_case", "snake_case")
    assert memo.convert("dromedaryCase", True) == "dromedary_case"
    assert memo["dromedaryCase"] == "dromedary_case"
    assert memo["dromedary_case"] == "dromedaryCase"

    assert memo.get("test_ing", direction=False) == "testIng"
    assert memo["testIng"] == "test_ing"
    assert memo["test_ing"] == "testIng"

    assert memo.get("doesNotExist") is None

    assert "doesNotExist" not in memo

    assert memo.get("doesNotExist", default="something") == "something"

    del memo["testIng"]
    assert "testIng" not in memo
    assert "test_ing" not in memo


def test_memo_converter():
    simple_memo = {}
    converter = memo_converter(lettercase.get_converter("snake", "dromedary"), simple_memo)

    assert converter("snake_case") == "snakeCase"
    assert "snake_case" in simple_memo


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
