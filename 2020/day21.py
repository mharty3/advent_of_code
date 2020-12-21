from __future__ import annotations
from typing import NamedTuple, List, Optional, Dict, Set


class Food(NamedTuple):
    ingredients: List[str]
    allergens: Optional[Set[str]]

    @staticmethod
    def parse_from_line(line: str) -> Food:
        ingredients, allergens = line.split("(contains")
        ingredients = ingredients.strip().split()
        allergens = allergens.strip().rstrip(")").split(", ")
        return Food(ingredients, allergens)


def find_possible_allergens(foods: List[Food]) -> Dict[str:Set]:
    possible_allergens = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen not in possible_allergens.keys():
                possible_allergens[allergen] = [(food.ingredients)]
            else:
                possible_allergens[allergen].append(food.ingredients)
    return {
        k: set.intersection(*[set(i) for i in v]) for k, v in possible_allergens.items()
    }


def solve1(input_data):
    foods = [Food.parse_from_line(line) for line in input_data.strip().split("\n")]
    d = find_possible_allergens(foods)
    allergens = set.union(*d.values())

    safe_ingredients = []
    for food in foods:
        for ingredient in food.ingredients:
            if ingredient not in allergens:
                safe_ingredients.append(ingredient)
    return len(safe_ingredients)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
                trh fvjkl sbzzf mxmxvkd (contains dairy)
                sqjhc fvjkl (contains soy)
                sqjhc mxmxvkd sbzzf (contains fish)"""

    assert solve1(test_data) == 5

    puz21 = Puzzle(2020, 21)
    data = puz21.input_data
    puz21.answer_a = solve1(data)
    # puz21.answer_b = solve2(data)
