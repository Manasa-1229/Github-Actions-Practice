from src.math_operations import add,sub,multiply,div

def test_cases():
    assert add(2,5)==7
    assert add(-1,1)==0
    assert sub(5,3)==2
    assert sub(-1,1)==-2
    assert sub(6,10)==-4
    assert multiply(5,5)==25
    assert multiply(-1,1)==-1
    assert multiply(0,5)==0
    assert div(10,2)==5
    assert div(10,0)== "Error: Division by zero is not allowed"
    assert div(-10,2)==-5
    assert div(0,2)==0
    assert div(10,10)==1
