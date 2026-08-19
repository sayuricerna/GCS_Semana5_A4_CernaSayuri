# src/app.py
products = []


def list_products():
    return products


def add_product(name, qty):
    if not name:
        raise ValueError("name required")
    if qty < 0:
        raise ValueError("qty must be >= 0")
    products.append({"name": name, "qty": qty})
    return True