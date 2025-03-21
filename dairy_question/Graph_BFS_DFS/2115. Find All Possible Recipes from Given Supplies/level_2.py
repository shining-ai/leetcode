# トポロジカルソートを使って解く
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_ingredient = set(supplies)
        ingredient_to_recipes = defaultdict(list)
        num_remain_ingredient = defaultdict(int)
        # 足りない材料と作れないレシピを紐づける
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in available_ingredient:
                    ingredient_to_recipes[ingredient].append(recipe)
                    num_remain_ingredient[recipe] += 1
        # 作れるレシピをキューに入れる
        queue = deque(
            [recipe for recipe in recipes if num_remain_ingredient[recipe] == 0])
        cooked = []
        while queue:
            recipe = queue.popleft()
            cooked.append(recipe)
            for next_recipe in ingredient_to_recipes[recipe]:
                num_remain_ingredient[next_recipe] -= 1
                if num_remain_ingredient[next_recipe] == 0:
                    queue.append(next_recipe)
        return cooked
