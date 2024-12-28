x1 = " ///// \n"
x2 = "/\n/\n/\n/\n/"
x3 = "      /\n      /\n      /\n      /\n      /\n"
x23 = "/     /\n/     /\n/     /\n/     /\n/     /\n"

def ind(adr):
	if adr == "0":
		print(x1+x23+x23+x1+"  a  \nf   b\n\ne   c\n  d   ")
		
	elif adr == "1":
		print(x3+x3+"\n   b\n\n   c")
	elif adr == "2":
		print(x1+x3+x1+x2+x1+"  a  \n    b\n  g  \ne   \n  d  ")
	elif adr == "3":
		print(x1+x3+x1+x3+x1+"  a  \n   b\n  g  \n   c\n  d  ")
	elif adr == "4":
		print(x23+x1+x3+"\nf   b\n  g  \n    c")

	elif adr == "5":
		print(x1+x2+x1+x3+x1+"  a  \nf    \n  g  \ne    \n  d  ")
	elif adr == "6":
		print(x1+x2+x1+x23+x1+"  a  \nf    \n  g  \ne   c\n  d  ")
	elif adr == "7":
		print(x1+x3+x3+"  a  \n    b\n     \n    c")
	elif adr == "8":
		print(x1+x23+x1+x23+x1+"  a  \nf   b\n  g  \ne   c\n  d  ")
	elif adr == "9":
		print(x1+x23+x1+x3+"  a  \nf   b\n  g  \n    c\n  d  ")

	elif adr == "a":
		print(x1+x23+x1+x23+"............")
	elif adr == "b":
		print(x2+x1+x23+x1+"............")
	elif adr == "c":
		print(x1+x2+'\n'+x2+x1+"............")
	elif adr == "d":
		print(x3+x1+x23+x1+"............")
	elif adr == "e":
		print(x1+x2+x1+x2+x1+"............")
	elif adr == "f":
		print(x1+x2+x1+x2+"\n  a  \nf   \n  g  \ne   \n")
	elif adr == "_":
		print("\n\n\n\n"+x1+"\n  g  \n")

def calc(adr, A, B):		
	if adr == "+":
		print(A+B)
	elif adr == "-":
		print(A-B)
	elif adr == "--":
		print(B-A)
	elif adr == "*":
		print(A*B)
	elif adr == "/":
		print(A/B)
	elif adr == "//":
		print(B/A)
	elif adr == "%":
		print(A%B)
	elif adr == "%%":
		print(B%A)
