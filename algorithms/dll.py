class node:
    def __init__(self, x):
        self.value = x
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None

    def insert( self, x ):
        x.next = self.__head
        if self.__head is not None:
            self.__head.prev = x
        self.__head = x
        x.prev = None
        self.__count += 1
        return x

    """
    Insert a node between 2 nodes given a current node or in the head if current is None
    """
    def insert_between( self, current, new ):
        if current is None:
            new.next = self.__head
            if self.__head is not None:
                self.__head.prev = new
            self.__head = new
        else:
            new.next = current.next
            new.prev = current
            if current.next is not None:
                current.next.prev = new
            current.next = new
        self.__count += 1
        return new

    def insert_tail( self, x ):
        if self.__tail is None:
            self.__head = x
            self.__tail = x
            x.prev = None
            x.next = None
        else:
            x.prev = self.__tail
            x.next = None
            self.__tail.next = x
            self.__tail = x
        self.__count += 1


    def size(self):
        return self.__count



