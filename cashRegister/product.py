# python packages
import os
import yaml
import jmespath

# package modules
import cashRegister

class Product:
    def __init__(self, code):
        """ Save all information about a scanned product

        Args:
            code (str): product code

        attributes:
            CODE (str): product code
            NAME (str): product name
            PRICE (double): price of one item of product
            ITEMS (int): number of the scanned items of the product
            TOTAL (double): total price of the sum items of the product
        """
        product_dict = self.get_product(code)
        for k,v in product_dict.items():
            setattr(self, k, v)
        self.ITEMS = 1
        self.TOTAL = 0

    def add_item(self):
        """Add item
        """
        self.ITEMS += 1

    def remove_item(self):
        """Remove item
        """
        self.ITEMS -= 1

    def __repr__(self):
        """Product representation

        Returns:
            str: product representation
        """
        return self.CODE


    @staticmethod
    def get_product(code):
        """Get the product from the yaml (DDBB)

        Args:
            code (str): product code

        Returns:
            dict: the dictionary of the information of the product (CODE, NAME, PRICE)
        """
        products_yaml = os.path.join(cashRegister.__path__[0], "products_data","products.yaml",)
        with open(products_yaml) as file:
            products_list = yaml.load(file, Loader=yaml.FullLoader)

        try:
            product = jmespath.search(f"[?CODE == '{code}']", products_list)[0]
        except IndexError:
            raise ValueError(f'Product code "{code}" not available.')

        return product


