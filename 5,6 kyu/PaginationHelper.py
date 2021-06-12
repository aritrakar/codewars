# https://www.codewars.com/kata/515bb423de843ea99400000a
# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper 
# class, which is a utility class helpful for querying paging information related to an array. The class is 
# designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
# The types of values contained within the collection/array are not relevant.

class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        l = len(self.collection)
        return (l // self.items_per_page) + (1 if l % self.items_per_page > 0 else 0)
        
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if (page_index >= self.page_count() or page_index < 0):
            return -1
        pages = []
        remaining = 0
        for x in range(1,len(self.collection)):
            if x % self.items_per_page == 0 and (not x == 0):
                pages.append(self.items_per_page)
                remaining = 0
            else:
                remaining += 1        
        if remaining > 0:
            pages.append(remaining + 1)
        return pages[page_index]


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        l = len(self.collection)
        if (item_index >= l or item_index < 0 or l == 0):
            return -1
        return item_index // self.items_per_page
