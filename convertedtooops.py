class MealPlan:
    def __init__(self, food_price: float, calories: int):
        self.food_price = food_price
        self.calories = int(calories)
    
    def total_cost(self, servings: int):
        return self.food_price * servings

if __name__ == "__main__":
    calories_per_serving = int(input("Enter calories per serving: "))
    cost_per_serving = float(input("Enter cost per serving: "))
    
    meal_plan = MealPlan(food_price=cost_per_serving, calories=calories_per_serving)
    
    num_servings = int(input("Enter number of servings: "))  
    
    total_cost = meal_plan.total_cost(servings=num_servings)
    
    print(f"Total cost for the meal plan: ${total_cost}")