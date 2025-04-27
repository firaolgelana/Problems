# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {recipes[i]:len(ingredients[i]) for i in range(len(recipes))}
        ingredients_to_recipes = defaultdict(list)
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                ingredients_to_recipes[ingredient].append(recipes[i])
 
        queue = deque(supplies)
        ans = []
        while queue:
            current = queue.popleft()
            for recipe in ingredients_to_recipes[current]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    ans.append(recipe)

        return ans
