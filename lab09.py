# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums: list[int], target: int):
    # Outline (write your plan here first):
    '''
    I have to take an array of numbers and a target number. 
    I have to find two numbers in the array that add up to the target number.
    I will use a nested loop to iterate through the array and check if any two numbers add up to the target number.
    I will use a for loop and use indexing to slowly cut the array down to avoid checking the same numbers again.
    '''
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def max_profit(prices):
    # Outline:
    '''
    I have to take an array of stock prices and find the maximum profit 
    that can be made by buying on one day and selling on a later day.
    I will iterate through the array and keep track of the minimum price seen so 
    far and the maximum profit that can be made by selling on the current day.
    I will return the maximum profit at the end of the iteration. If no profit is possible, I will return 0.

    I will keep track of the minimum price seen so far and the maximum profit that can be made by selling on the current day.
    Then, I will return the maximum profit at the end of the iteration. If no profit is possible, I will return 0.
    '''
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    minPrice: int = prices[0]
    maxProfit: int = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:  
            maxProfit = price - minPrice

    return maxProfit

def max_subarray(nums):
    # Outline:
    '''
    I need to find the numbers next to each other in the array that add up to the largest sum.
    I will use a nested loop to iterate through the array and check the sum of each contiguous block of numbers.
    I will keep track of the maximum sum seen so far and return it at the end of the iteration.
    '''
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    maxSum = nums[0]
    for i in range(len(nums)):
        currentSum = 0
        for j in range(i, len(nums)):
            currentSum += nums[j]
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    '''
    I need to check if the brackets in the string are balanced. 
    I will take bracket pairs out of the string. 
    If the string is empty at the end, then the brackets are balanced.
    '''
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    empty: bool = False
    while not empty:
        if "()" in s:
            s = s.replace("()", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        else:
            empty = True

    if len(s) == 0:
        return True
    else:
        return False

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]

    print(max_profit([7, 1, 5, 3, 6, 4]))   # returns 5   (buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))      # returns 0   (prices only fall)

    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # returns 6   (4 + -1 + 2 + 1)
    print(max_subarray([5, 4, -1, 7, 8]))                  # returns 23  (the whole list)

    print(is_balanced("()[]{}"))   # returns True
    print(is_balanced("{[]}"))   # returns True
    print(is_balanced("([)]"))    # returns False   (closed in the wrong order)


if __name__ == "__main__":
    main()
