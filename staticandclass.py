class MealPlan:
    def __init__(self, food_price: float, calories: int):
        self._food_price = food_price
        self._calories = int(calories)
    
    def get_food_price(self):
        return self._food_price
    
    def set_food_price(self, value):
        self._food_price = value
    
    def get_calories(self):
        return self._calories
    
    def set_calories(self, value):
        self._calories = int(value)
    
    def total_cost(self, servings: int):
        return self._food_price * servings
    
    @staticmethod
    def calculate_total_cost(food_price: float, servings: int):
        return food_price * servings
    
    @classmethod
    def from_calories(cls, food_price: float, calories_per_serving: int, num_servings: int):
        return cls(food_price, calories_per_serving * num_servings)

if __name__ == "__main__":
    calories_per_serving = int(input("Enter calories per serving: "))
    cost_per_serving = float(input("Enter cost per serving: "))
    
    meal_plan = MealPlan(food_price=cost_per_serving, calories=calories_per_serving)
    
    num_servings = int(input("Enter number of servings: "))  
    
    total_cost = meal_plan.total_cost(servings=num_servings)
    print(f"Total cost for the meal plan: ${total_cost}")
    
    
    static_total_cost = MealPlan.calculate_total_cost(cost_per_serving, num_servings)
    print(f"Static total cost for the meal plan: ${static_total_cost}")
    
    
    meal_plan_from_calories = MealPlan.from_calories(cost_per_serving, calories_per_serving, num_servings)
    print(f"Meal plan from calories total cost: ${meal_plan_from_calories.total_cost(servings=num_servings)}")
