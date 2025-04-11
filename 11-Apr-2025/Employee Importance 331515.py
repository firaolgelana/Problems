# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        maps = {emp.id:emp for emp in employees}
        def dfs(emp):
            total_imp = emp.importance
            for sub in emp.subordinates:
                total_imp += dfs(maps[sub])
            return total_imp
        
        return dfs(maps[id])
