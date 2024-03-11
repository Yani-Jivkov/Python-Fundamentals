class Storage:
    storage = []
    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if len(Storage.storage) < int(self.capacity):
            Storage.storage.append(product)
        else:
            pass

    def get_products(self):
        return Storage.storage

# Example
# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())
