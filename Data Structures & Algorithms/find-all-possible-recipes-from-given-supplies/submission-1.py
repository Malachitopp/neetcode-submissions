from collections import defaultdict


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = {} 

        for i in range(len(recipes)):
            adj[recipes[i]] = ingredients[i] 

        created = set() 
        cycle = set() 
        supply = set(supplies) 
    

        def dfs(recipe):
            if recipe in created:
                supply.add(recipe)
                return True 

            if recipe in cycle:
                return False 
            cycle.add(recipe) 

            for ingredient in adj[recipe]:
                if ingredient not in supply and ingredient not in adj:
                    return False 
                if ingredient in supply:
                    continue 
                if not dfs(ingredient):
                    return False 
            
            created.add(recipe) 
            cycle.remove(recipe) 
            return True
        output = [] 
        for r in recipes:
            if not dfs(r):
                continue 
            output.append(r) 
        
        return output 

                
