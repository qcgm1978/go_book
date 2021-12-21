from testbook import testbook


@testbook('/Users/philipp/Documents/go_book/book/mini_book/docs/Part1_Ch3.1.ipynb', execute=True)
def test_func(tb):
   func = tb.get("Player")

   assert func(1, 2) == 3