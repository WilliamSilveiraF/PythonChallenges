import productList

#A ideia inicial é fazer um caixa de supermercado com as funcionalidades:
# - Inserção de Produtos
# - Deleção de Produtos
# - Recuperar produtos já deletados
# - Calcular o valor de impostos
# - Calcular o valor total
# - Cada produto é dividido em ID, Preço, Quantidade e Imposto

'''
Nossa solução foi centralizada em uma classe de produtos, que quando chamada ela cria um carrinho para o
usuário, possibilitando que ele adicione novos produtos, veja todos os produtos que estão em seu carrinho
(preço, quantidade e impostos), e deletar produtos caso os queira mais. O programa calcula o valor total
da compra levando em consideração os impostos sobre a compra daqueles produtos.
'''

class Product(object):
    def __init__(self, id, price, amount, tax):
        self.id = int(id)
        self.price = float(price)
        self.amount = float(amount)
        self.tax = float(tax)

class Cart(object):
    cart = {}

    def create(self):
        for props in productList.getAll():
            id, name, price, tax = props
            product = vars(Product(id, price, 0, tax))
            self.cart[name] = product
        return self.cart
    
    def addProduct(self, name, amount):
        if not (name in self.cart):
            return 'Product not found'
        
        self.cart[name]['amount'] += amount
        print("Product added successfully")
        return self.cart
    
    def deleteProduct(self, name, amount):
        if self.cart[name]['amount'] < amount:
            print("Can't delete not found products")
            return 'err'
        self.cart[name]['amount'] -= amount
        print("Product successfully deleted")
        return self.cart

    def clear(self):
        for product in self.cart:
            self.cart[product]['amount'] = 0
        print("Successfully cleaned cart")
        return self.cart

    def getAll(self):
        print("\n====== MYCART ======\n")
        for name, info in self.cart.items():
            if info['amount'] > 0:
                print(f"- Product: {name}, Price: {info['price']}, Amount: {info['amount']}")
        print("\n====================")
        return self.cart

    def checkout(self):
        total = 0
        for product in self.cart:
            price = self.cart[product]['price']
            amount = self.cart[product]['amount']
            tax = self.cart[product]['tax']
            total += price * (1 + tax) * amount
        self.clear()
        print(f'Total: {total:.2f}')
        return total

cart = Cart()
cart.create()

while True:
    try:
        print("\n====== SUPERMARKET ======\n")
        print("Press the digit:")
        print("[1] Add product")
        print("[2] Delete product")
        print("[3] Clear cart")
        print("[4] Show products")
        print("[5] Checkout")
        print("\n=========================\n")
        choice = int(input('Choice: '))

        if choice == 1:
            name = input('Product name: ')
            amount = float(input('Amount: '))
            cart.addProduct(name, amount)
        elif choice == 2:
            name = input('Product name: ')
            amount = float(input('Amount: '))
            cart.deleteProduct(name, amount)
        elif choice == 3:
            cart.clear()
        elif choice == 4:
            cart.getAll()
        elif choice == 5:
            cart.checkout()
    except EOFError:
        break