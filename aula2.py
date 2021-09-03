def main ():
	nota_1 = int(input())
	nota_2 = int(input())
	
	soma = nota_1 + nota_2
	media = soma/2
	
	if media >= 5:
		print('passou')
	else:
		print('bombou')

main()
