"""Part B. A queue: first in, first out (Section 8.1).

The queue is a Python list. The FRONT of the list is the HEAD of the queue,
and the END of the list is the TAIL.
Replace each `pass` with your own code. Each function needs one or two lines.
"""


from pytest import Item


def enqueue(queue, item):
    """Add item at the tail of the queue."""
    queue.append(item)
    pass


def dequeue(queue):
    """Take the item at the head of the queue and return it.

    If the queue is empty, return None.
    """

    if len(queue) == 0:
        return None

    output_value = queue.pop(0)

    return output_value





example_list = [1, 2, 3]


item = dequeue(example_list)    
print(item)
print(example_list)
