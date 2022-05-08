import pytest

@pytest.fixture
def printFirstRepeatedInteger(A, B):
    for i in A:
        for j in B:
            if (i == j):
                print("The first repeating element is", i)
                return i
    print("There are no repeating elements")

def test_FirstRepeatedIntegerExist():
    assert  printFirstRepeatedInteger([1,9,3,7,8,10], [4,5,6,7]) == 7
         
def test_FirstRepeatedIntegerNotExist(): 
    assert  printFirstRepeatedInteger([1,2,3], [4,5,6,7]) == None