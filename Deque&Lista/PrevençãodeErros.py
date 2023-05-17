def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
  		previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
