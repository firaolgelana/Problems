# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        in_degree = {recipe:0 for recipe in recipes}
        gredients = defaultdict(list)
        for recipe, gredient in zip(recipes, ingredients):
            for g in gredient:
                gredients[g].append(recipe)
            in_degree[recipe] = len(gredient)
        
        queue = deque(supplies)
        ans = []
        while queue:
            current = queue.popleft()
            for recipe in gredients[current]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    queue.append(recipe)
                    ans.append(recipe)

        return ans