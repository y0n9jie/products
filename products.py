products = []
while True:
	name = input('請輸入消費項目：')
	if name == 'q':
		break
	price = input('請輸入消費金額：')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的金額是', p[1])

