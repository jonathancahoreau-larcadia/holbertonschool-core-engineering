#!/usr/bin/env python3
"""
This module defines a VerboseList class that logs list mutations.
"""


class VerboseList(list):
    """
    List subclass that prints descriptive messages for mutation operations.
    """

    def append(self, item):
        """
        Append an item and print a notification.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend the list and print a notification.

        Args:
            items: An iterable of items to add to the list.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove an item and print a notification.

        Args:
            item: The item to remove from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=(-1)):
        """
        Pop an item by index and print a notification.

        Args:
            index (int, optional): The index of the item to pop.
            Defaults to -1.

        Returns:
            The popped item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)


if __name__ == "__main__":
    """
    Demonstrate the VerboseList behavior.
    """
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
