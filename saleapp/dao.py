def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "iPhone 13",
        "price": 20000000,
        "image": "https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg"
    }, {
        "id": 2,
        "name": "Galaxy SX",
        "price": 20000000,
        "image": "https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg"
    }, {
        "id": 3,
        "name": "Oppo",
        "price": 20000000,
        "image": "https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg"
    }, {
        "id": 4,
        "name": "Redmi",
        "price": 20000000,
        "image": "https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg"
    }, {
        "id": 5,
        "name": "Apple",
        "price": 20000000,
        "image": "https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
