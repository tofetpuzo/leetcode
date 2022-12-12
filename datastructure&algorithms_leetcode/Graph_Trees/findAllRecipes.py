# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. 
# The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
# Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.

 

# Example 1:

# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".

# Example 2:

# Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

# Example 3:

# Input: recipes = ["bread","sandwich","burger"], 
# ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], 
# supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
import collections


def findAllRecipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]):
    graph = collections.defaultdict(list)
    indegree_no = collections.defaultdict(int)
    for recipe, ingre in zip(recipes, ingredients):
        indegree_no[recipe] = len(ingre)

        for ingr in ingre:
            graph[ingr].append(recipe)

    res = []

    queue = collections.deque(supplies)
    recipes = set(recipes)

    while queue:
        supply = queue.popleft()
        if supply in recipes:
            res.append(supply)

        for recipe in graph[supply]:
            indegree_no[recipe] -=1

            if indegree_no[recipe] == 0:
                queue.append(recipe)

    return res
    

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
print(findAllRecipes(recipes, ingredients, supplies))