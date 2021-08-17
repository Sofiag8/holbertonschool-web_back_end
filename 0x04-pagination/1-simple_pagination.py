#!/usr/bin/env python3

"""
Simple pagination
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """

    start = (page-1) * page_size
    end = page * page_size
    # end = start + page_size
    i_range = (start, end)
    return i_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes two integer arguments page with default value 1
        and page_size with default value 10.
        """

        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        gp_range = index_range(page, page_size)
        gp_start = gp_range[0]
        gp_end = gp_range[1]
        return self.dataset()[gp_start:gp_end]
