import time,math
class Range:
    """Implementation of inbuilt range function"""

    def __init__(self,start=0,stop=None,step=1):
        """Initialize range function parameters"""
        self._stop = stop
        self._start = start
        self._step = step

        if self._step == 0:
            raise ValueError("Step can't be 0")

        if self._stop is None:
            self._stop = start
            self._start = 0


    '''def __next__(self):
        """Return the next element in the list"""
        if self._start < self._stop:
            val = self._start
            self._start = self._start + self._step
            return val
        else:
            raise StopIteration()'''

    def __len__(self):
        #print("Length is ",math.ceil((self._stop-self._start)/self._step))
        #if (self._step > 0):
        return abs(math.ceil((self._stop-self._start)/self._step))
        #else:
            #return math.ceil((self._start - self._stop) / self._step)

    def __getitem__(self, item):
        if -1 < item < len(self):
            if self._step > 0:
                return self._start + item * self._step
            else:
                return self._stop + item * self._step
        else:
            raise IndexError("Item out of bound")


    '''def __iter__(self):
        """Return self as iterable"""
        return self'''

if __name__ == "__main__":
    a = [x for x in Range(25,11,-2)]
    print(str(a))