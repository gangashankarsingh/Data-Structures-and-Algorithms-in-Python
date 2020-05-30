class SequenceIterator:

    def __init__(self,sequence):
        self.sequence = sequence
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index >= len(self.sequence):
            raise StopIteration("No more elements")
        else:
            return self.sequence[self.index]

if __name__ == '__main__':
    a = [i for i in range(5)]
    b = SequenceIterator(a)
    while True:
        try:
            print(next(b))
        except  StopIteration:
            print("Reached the end")
            break