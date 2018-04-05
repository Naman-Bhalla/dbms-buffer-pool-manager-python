class Page:

    def __init__(self, id, size):
        self.index = index
        self.page_number = uuid4()
        self.pin_count = 0
        self.dirty = False
        self.state = -1

    def increment_pin_count(self):
        self.pin_count += 1

    def decrement_pin_count(self):
        self.pin_count -= 1

    def is_dirty(self):
        return self.dirty

    def get_pin_count(self):
        return self.pin_count
