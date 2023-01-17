import os
import yaml
import cashRegister

class product:
    def _init_(code):
        """ Save all information about a scanned product

        Args:
            code (str): product code

        attributes:
            CODE (str): product code
            NAME (str): product name
            PRICE (double): price of one item of product
            ITEMS (int): number of the items of the product
            TOTAL (double): Total price of the sum items of the product
        """
        product_dict = self.get_product(code)
        for k,v in product_dict.items():
            setattr(self, k, v)
        self.ITEMS = 1
        self.TOTAL = 0


    def get_product(self, code):
        """Get the product from the yaml (DDBB)

        Args:
            code (str): product code

        Returns:
            dict: the dictionary of the information of the product (code, name, price)
        """
        products_yaml = os.path.join(cashRegister.__path__[0], "products.yaml",)
        with open(products_yaml) as file:
            products_dict = yaml.load(file, Loader=yaml.FullLoader)
        product = products_dict[code]
        return product

    def add_item(self):
        """Add item
        """
        self.ITEMS += 1

    def remove_item(self):
        """Remove item
        """
        self.ITEMS -= 1





