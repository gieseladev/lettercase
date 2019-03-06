from lettercase import convert_iter_items, mut_convert_items, mut_convert_keys


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
