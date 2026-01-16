from project import merge
from project import counttotal
from project import priceparse

def test_merge():
    left = [{"Price": "RM1"}, {"Price": "RM5"}, {"Price": "RM7"}, {"Price": "RM10"}]
    right = [{"Price": "RM2"}, {"Price": "RM3"}, {"Price": "RM8"}, {"Price": "RM11"}]
    assert merge(left, right) == [{"Price": "RM1"}, {"Price": "RM2"}, {"Price": "RM3"}, {"Price": "RM5"}, 
                                  {"Price": "RM7"}, {"Price": "RM8"}, {"Price": "RM10"}, {"Price": "RM11"}]

def test_counttotal():
    read = [{"Price": "RM1"}, {"Price": "RM5"}, {"Price": "RM7"}]
    assert counttotal(read) == 13

def test_priceparse():
    assert priceparse("RM10") == 10