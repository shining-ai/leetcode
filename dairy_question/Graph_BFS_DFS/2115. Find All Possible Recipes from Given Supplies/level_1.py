
# BFSによる解放
# 料理が作れなくなるまで繰り返す。
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies_map = {}
        for supply in supplies:
            supplies_map[supply] = True

        def can_cook(ingredient: List[str]):
            for food in ingredient:
                if not food in supplies_map:
                    return False
            return True

        not_cook = deque([i for i in range(len(recipes))])
        cooked = []
        num_not_cook = 0
        while num_not_cook != len(not_cook):
            num_not_cook = len(not_cook)
            for _ in range(num_not_cook):
                i = not_cook.popleft()
                if can_cook(ingredients[i]):
                    cooked.append(recipes[i])
                    supplies_map[recipes[i]] = True
                    continue
                not_cook.append(i)
        return cooked
