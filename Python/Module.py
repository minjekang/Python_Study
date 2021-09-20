#import Theater_module
#Theater_module.price(3) # 3명이서 영화 보러갔을 때 가격
#Theater_module.price_morning(4) # 4명이서 조조 할인
#Theater_module.price_soldier(5) # 5명 군인 할인

# import Theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from Theater_module import*
# price(3)
# price_morning(4)
# price_soldier(5)

# from Python.Theater_module import price_soldier
# from Theater_module import price, price_morning
# price(5)
# price_morning(6)
# #price_soldier(4)  X

from Theater_module import price_soldier as price
price(5)