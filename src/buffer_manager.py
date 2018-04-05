from src.frame import Frame
from src.lru_replacer import LRUReplacer
from src.page import Page
from src.disk_manager import DiskManager


class BufferPoolManager:

    def __init__(self, no_of_pages):
        self.frame_table = []
        self.buffer_pool = []
        self.disk_manager = DiskManager(64)

        for i in range(no_of_pages):
            self.frame_table[i] = Frame(i)
            self.buffer_pool[i] = Page(i, 64)  # Setting default page size to 64

        self.replacer = LRUReplacer(self)
        self.page_map = {}
        self.no_of_pages = no_of_pages

    def __len__(self):
        return self.no_of_pages

    def getFrameTable(self):
        return self.frame_table

    def newPage(self):
        page = self.disk_manager.allocatePage()
        page.increment_pin_count()

        return page

    def fetchPage(self, page_id):
        for pages in self.buffer_pool:
            if pages.index == page_id:
                return pages

        # Page not in buffer pool
        page = self.replacer.victim(self.buffer_pool)

        if page.is_dirty():
            self.disk_manager.writePage(page)  # Page is dirty

        return self.disk_manager.readPage(page_id)

    def unpinPage(self, page_id, is_dirty):
        for pages in self.buffer_pool:
            if pages.index == page_id:
                pages.decrement_pin_count()
                if is_dirty:
                    pages.dirty = True
                if pages.pin_count == 0:
            # TODO: Put into LRU Cache
        return False

    def flushPage(self, page_id):
        for pages in self.buffer_pool:
            if pages.index == page_id:
                self.disk_manager.writePage(pages)
                return True
        return False

    def flushAllPages(self):
        for pages in self.buffer_pool:
            self.disk_manager.writePage(pages)

    def deletePage(self, page_id):
        for pages in self.buffer_pool:
            if pages.index == page_id:
                if pages.pin_count == 0:
                    self.disk_manager.deAllocatePage(pages)
                else:
                    raise ValueError("Page isn't pinned")
