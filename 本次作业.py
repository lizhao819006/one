#作业
def max_sum(numbers):
    #初始化当前最大和和全局最大和
    max_here = 0
    max_so_far = 0
    
    for number in numbers:
        # 当前最大和
        max_here = max(number, max_here + number)
        # 全局最大和
        max_so_far = max(max_so_far, max_here)
    
    return max_so_far


numbers = [-20,11,-4,13, -5,-2]
print("最大子段和为:", max_sum(numbers))



