# tests/test_app.py
from src.app import add_product, list_products


def test_add_and_list():
    add_product("item", 1)
    assert len(list_products()) >= 1