import productList

'''
A ideia principal é criar um sistema de supermercado, 
onde o usuário pode realizar as seguintes ações:
    - Inserir produtos
    - Deletar produtos
    - Limpar o carrinho
    - Verificar quais produtos já foram adicionados
    - Abrir checkout mostrando o valor total a ser pago pelo usuário

A modelagem do código leva em consideração duas classes principais:
    - Product
        => Retorna um objeto que faz referência a um produto
        => Props: id, price, amount, tax
    - Cart
        => Uma interface de ações sobre o carrinho do usuário
        => Ações disponíveis: criar carrinho, adicionar produtos, deletar produtos, 
            limpar carrinho, mostrar produtos adicionados e abrir checkout

Assim, dado um lista de produtos .csv foi possível parsear os dados usando as classes citadas
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