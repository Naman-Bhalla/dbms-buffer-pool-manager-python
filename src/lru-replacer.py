from src.replacer import Replacer

class LRU_Replacer(Replacer):
    AVAILABLE = -1
    REFERENCED = 0
    PINNED = 1

    def __init__(self, buffer_manager):
        super().__init__()
        self.no_of_buffers = buffer_manager.getNoOfBuffers()
        self.frame_table = buffer_manager.getFrameTable()

        for frames in self.frame_table:
            frames.state = AVAILABLE

        self.head = -1

    def insert(self, frame):
        pass

    def victim(self, frame):
        for i in range(2 * self.no_of_buffers):
            self.head = (self.head + 1) % self.no_of_buffers

            if self.frame_table[self.head].state == self.REFERENCED:
                self.frame_table[self.head].state = self.AVAILABLE

            elif self.frame_table[self.head].state == self.AVAILABLE:
                return self.frame_table[self.head]

        return None

    def erase(self, frame):
        pass

    def __len__(self):
        return self.no_of_buffers