"""
690. Employee Importance
Easy

You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

 

Note:

    One employee has at most one direct leader and may have several subordinates.
    The maximum number of employees won't exceed 2000.
"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# approach: circular indexing: find the leader, find the subordinates
# runtime: O(n^2)
# memory: O(1)
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates = []
        total_importance = 0
        
        # find the leader
        for employee in employees:
            
            # check if employee is our leader
            if employee.id == id:
                subordinates = employee.subordinates
                total_importance += employee.importance
                break
                
        # find the subordinates, circular index
        index = 0
        while len(subordinates) != 0:
                
            # check if employee is a subordinate
            if employees[index].id in subordinates:
                total_importance += employees[index].importance
                subordinates.remove(employees[index].id)
                
                # add subordinate's subordinates
                subordinates += employees[index].subordinates
                    
            # update index
            if index == len(employees) - 1:
                index = 0
            else:
                index += 1
                
        return total_importance