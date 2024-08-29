"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
Yan ZHu
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb



def longest_run(mylist, key):
    maxrun = 0 
    run = 0 
    for i in range(len(mylist)):
        if mylist[i] == key:
            run += 1  
            if run > maxrun:
                maxrun = run 
        else:
            run = 0 
    return maxrun

          
          
  

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if len(mylist) == 0:
        return Result(0, 0, 0, False)
    
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    
    mid = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)
    
    left_len = left_result.left_size
    if left_result.is_entire_range and mylist[mid] == key:
        left_len += right_result.left_size
    
    right_len = right_result.right_size
    if right_result.is_entire_range and mylist[mid-1] == key:
        right_len += left_result.right_size
    
    cross_len = 0
    if mylist[mid-1] == key and mylist[mid] == key:
        cross_len = left_result.right_size + right_result.left_size
    
    max_len = max(left_result.longest_size, right_result.longest_size, cross_len)
    
    entire_range = left_result.is_entire_range and right_result.is_entire_range
    
    return Result(left_len, right_len, max_len, entire_range)



## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
test_longest_run()




def test_longest_run_recursive():
    result = longest_run_recursive([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12)
    assert result.longest_size == 3, "ff"
    
    result = longest_run_recursive([12, 12, 12, 12, 12], 12)
    assert result.longest_size == 5, "ff"
    
    result = longest_run_recursive([1, 2, 3, 4, 5], 12)
    assert result.longest_size == 0, "ff"
    
    result = longest_run_recursive([12, 1, 12, 1, 12], 12)
    assert result.longest_size == 1, "ff"
    
    result = longest_run_recursive([12, 12, 1, 12, 12, 12], 12)
    assert result.longest_size == 3, "ff"
    
    result = longest_run_recursive([], 12)
    assert result.longest_size == 0, "ff"
    
    result = longest_run_recursive([12], 12)
    assert result.longest_size == 1, "ff"
    
    result = longest_run_recursive([1], 12)
    assert result.longest_size == 0, "ff"
    
    print("pass！")


test_longest_run_recursive()

