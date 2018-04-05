from src.replacer import Replacer


class LRUReplacer(Replacer):
    AVAILABLE = -1
    REFERENCED = 0
    PINNED = 1

    def __init__(self, buffer_manager):
        super().__init__()
        self.no_of_buffers = len(buffer_manager)
        self.frame_table = buffer_manager.getFrameTable()

        for frames in self.frame_table:
            frames.state = AVAILABLE

        self.head = -1

    def insert(self, page):
        page.state = self.REFERENCED

    def victim(self):
        if self.frame_table:
            for i in range(2 * len(self.frame_table)):
                self.head = (self.head + 1) % len(self.frame_table)

                if self.frame_table[self.head].state == self.REFERENCED:
                    self.frame_table[self.head].state = self.AVAILABLE

                elif self.frame_table[self.head].state == self.AVAILABLE:
                    return self.frame_table[self.head]

        return None

    def erase(self, page):
        index = -1
        for frames in self.frame_table:
            index += 1
            if frames.index == page.index:
                self.frame_table.pop(index)
                return True
        return False

    def __len__(self):
        return self.no_of_buffers
