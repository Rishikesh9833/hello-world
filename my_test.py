from pkg.MyInt import MyInt
import pytest
5
class TestMyInt:
    def test_add(self):
        a=MyInt(2)
        b=MyInt(3)
        print(a)
        
        assert a+b ==MyInt(5)
    
    def test_seq(self):
        a=MyInt(2)
        assert a.seq() == 4