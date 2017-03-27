from functools import reduce
from typing import Dict, Tuple, List


"""discount tiers"""
DISCOUNT_MAPPING = {
    7: 0.65,
    6: 0.7,
    5: 0.75,
    4: 0.85,
    3: 0.9,
    2: 0.95,
    1: 1,
}


def buy(books):
    """do discount"""
    # unique_books_count = get_total_uniq_books(books)
    total_books = reduce((lambda x, y: x + y), books.values())
    unit_price = 8
    discounted_price = 0
    discount_tiers = DISCOUNT_MAPPING.keys()
    discounts = {}
    unique_books_count = len(books.keys())
    for tier in discount_tiers:
        print(unique_books_count, tier)
        if unique_books_count >= tier:
            count = 0
            discount_books = []
            for book, quantity in books.items():
                if books[book] == 0:
                    continue
                discount_books.append(book)
                count += 1
                books[book] -= 1
                total_books -= 1
                if books[book] == 0:
                    unique_books_count -= 1
                if count == tier:
                    discounted_price += unit_price*DISCOUNT_MAPPING[tier]*tier
                    discounts[tier] = discount_books
                    break
    return {
        "price":total_books * unit_price + discounted_price,
        "discount_books":discounts
    }
