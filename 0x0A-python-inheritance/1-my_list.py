#!/usr/bin/python3
"""Class called MyList inherits from list"""


class MyList(list):
    """Impliments the printing of sorted list"""

    def print_sorted(self):
        """Print list in ascending order"""
        order = sorted(self)
        print(order)
