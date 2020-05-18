'''
concptualize a sorted half and an unsorted half
initially the sorted half consistws of just the first element
iterate along the rest of the array
place it in its appropraite spot in the sorted half
the sorted half grows until it ecompasses the whole array
'''


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def insertion_sort_books(arr_books):
        # sort by the title
        for i in range(1, ln(arr_books)):
            curr_book = arr_books[i]
            j = i
            # ut curr_book in the appropriate spot
            # loop through our sorted half and find the approrpiate loop
            # #comparing the element with the element right before it
            while j > 0 and curr_book.title < arr_books[j-1].title:
                # slide the currentbook over with the element at j-1
                arr_books[j] = arr_books[j-1]
                j -= 1
            # override the book at the correct position
            arr_books[j] = curr_book
            return arr_books

