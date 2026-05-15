#!/usr/bin/env python3
"""
VerboseList module - Extends Python's built-in list with verbose notifications
"""


class VerboseList(list):
    """
    VerboseList class that extends the built-in list class

    Provides notifications whenever items are added or removed from the list
    """

    def append(self, item):
        """
        Append an item to the list and print a notification

        Args:
            item: The item to append to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification

        Args:
            iterable: An iterable containing items to add to the list
        """
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification

        Args:
            item: The item to remove from the list

        Raises:
            ValueError: If the item is not in the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list at the given index and print a notification

        Args:
            index (int): The index of the item to pop (default: -1, last item)

        Returns:
            The popped item

        Raises:
            IndexError: If the list is empty or index is out of range
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
