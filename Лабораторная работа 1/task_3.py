# TODO Найдите количество книг, которое можно разместить на дискете

information_discet = 1.44 * 1024 * 1024
pages_book = 100
lines_page = 50
symbols_line = 25
symbol_code = 4
book_size_bytes = pages_book * lines_page * symbols_line * symbol_code
quantity_book = int(information_discet // book_size_bytes)

print("Количество книг, помещающихся на дискету:", quantity_book)
