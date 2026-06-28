# - 아래 상품을 가격이 저렴한 순서대로 정렬하세요.

products = [
    {"name": "감자", "price": 500},
    {"name": "고구마", "price": 1200},
    {"name": "양파", "price": 800}
]

products.sort(key = lambda x: (x['price']))
print(products)