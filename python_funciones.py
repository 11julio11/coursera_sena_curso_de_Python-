def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print('total tax: ',calculate_tax(175.00, 16))

print('total tax: ',calculate_tax(164.33, 22))


#-------------------------------------------------------------#
bill = [175.00, 23.11, 56.00]

valor_tax = 26

def calculate_tax(bill , valor_tax):
    taxes = [(item *  valor_tax)/ 100.00 for item in bill] 
    return taxes

valor_tax = float(input('ingrese el valor del impuestos: '))

taxes = calculate_tax(bill, valor_tax)
 
print(taxes)

#-------------------------------------------------------------#
def calculate_tax(valor, valor_tax):
    tax = (valor * valor_tax) / 100.00
    return tax

valor = float(input('ingrese un valor: '))

valor_tax = float(input('ingrese el valor del impuesto: '))

tax = calculate_tax(valor, valor_tax)
print(f'el impuesto para el valor {valor} con una tasa de {valor_tax}% es: {tax} ')