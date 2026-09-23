"""T1.1 smoke test: the package imports and a placeholder Battle object exists."""


def test_engine_imports():
    import medarot

    assert medarot.__version__ == "0.1.0"
