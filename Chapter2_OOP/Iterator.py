class SequenceIterator:
    """Iterator for any of python Sequence types"""

    def __init__(self,sequence):
        """Create an iterator from the given sequence"""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return next element or Stop Iteration"""
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """Returns seld as iterator"""
        return self

if __name__ == '__main__':
    list = [x for x in range(10)]
    hello = SequenceIterator(list)
    for i in hello:
        print(i)
