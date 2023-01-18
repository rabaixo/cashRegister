from . import product as pr

class Checkout:
    def __init__(self, pricing_rules):
        """Scan or remove an product items

        Args:
            pricing_rules (dict): pricing rules
        """
        self.pricing_rules = pricing_rules
        self.items_list = []
        self.objs_products_list = []


    def scan(self, code):
        """Scan item from an product

        Args:
            code (str): the code of product

        Returns:
            dict: items & total
        """
        self.items_list.append(code)
        codes_products_list = [object_product.CODE for object_product in self.objs_products_list]
        if code in codes_products_list:
            self.objs_products_list[codes_products_list.index(code)].add_item()
        else:
            self.objs_products_list.append(pr.Product(code))
        total = self.get_total()
        return {"items": self.items_list, "total": total}

    def remove_item(self, code):
        """ Remove item from an product

        Args:
            code (str): the code of product

        Returns:
            dict: items & total
        """
        pass


    def get_total(self):
        """ Get the total of all items

        Returns:
            double: the items total
        """
        for obj_product in self.objs_products_list:
            if obj_product.CODE in self.pricing_rules:
                obj_product.TOTAL = self.pricing_rules[obj_product.CODE](obj_product)
            else:
                obj_product.TOTAL = obj_product.ITEMS * obj_product.PRICE
        return sum([obj_product.TOTAL for obj_product in self.objs_products_list])




