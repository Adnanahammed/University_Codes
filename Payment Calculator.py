book_price = int(input('책 값을 입력하세요 : ')) 
discount = float(input('할인율을 입력하세요(%) : ')) 
shipping = int(input('배송료를 입력하세요 : ')) 
total_price = book_price - (book_price * discount/100) + shipping 
print("결제 금액 : %.0f원" % total_price)
