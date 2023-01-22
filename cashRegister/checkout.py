# package modules
from . import product as pr

class Checkout:
    def __init__(self, pricing_rules):
        """Scan or remove the items of store products

        Args:
            pricing_rules (dict): pricing rules

        Attributes:
            pricing_rules (dict):  pricing rules
            items_list (list): the list of scanned items
            objs_products_dict (dict): dict of the scanned products objects
        """
        self.pricing_rules = pricing_rules
        self.items_list = []
        self.objs_products_dict = {}

    def scan(self, code):
        """Scan an item of a product

        Args:
            code (str): the code of product

        Returns:
            dict: scanned items & the total cost (items, total) or error (error)
        """
        if code in self.objs_products_dict:
            self.objs_products_dict[code].add_item()
        else:
            try:
                self.objs_products_dict[code] = pr.Product(code)
            except Exception as err:
                return {"error": err.__str__()}

        self.items_list.append(code)
        total = self.get_total()
        return {"items": self.items_list, "total": total}

    def remove(self, code):
        """ Remove an item of a product from the scanned products list

        Args:
            code (str): the code of product

        Returns:
            dict: scanned items without the deleted item & the updated total cost (items, total) or warning (warning)
        """
        if code in self.objs_products_dict:
            self.objs_products_dict[code].remove_item()
            total = self.get_total()
            self.items_list.remove(code)
            if self.objs_products_dict[code].ITEMS == 0:
                del self.objs_products_dict[code]
            return {"items": self.items_list, "total": total}
        else:
            return {"warning": f'"{code}" not registered.'}



    def get_total(self):
        """ Get the total cost of all scanned items

        Returns:
            double: the items total cost
        """
        for obj_product in self.objs_products_dict.values():
            if obj_product.CODE in self.pricing_rules:
                obj_product.TOTAL = self.pricing_rules[obj_product.CODE](obj_product)
            else:
                obj_product.TOTAL = obj_product.ITEMS * obj_product.PRICE
        return sum([obj_product.TOTAL for obj_product in self.objs_products_dict.values()])




