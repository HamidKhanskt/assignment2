def meal(food_price: float, calories: int):
    return {
        "food_price": food_price,
        "calories": int(calories)
    }

def total_cost_of_meal(food_price, calories, servings):
    total_cost = food_price * servings
    return total_cost

if __name__ == "__main__":
    
    
    calories_per_serving = int(input("Enter calories per serving: "))
    cost_per_serving = float(input("Enter cost per serving: "))
    
   
    meal_plan = meal(food_price=cost_per_serving, calories=calories_per_serving)
    
   
    num_servings = int(input("Enter number of servings: "))  
    
    
    total_cost = total_cost_of_meal(food_price=meal_plan["food_price"],
                                    calories=meal_plan["calories"],
                                    servings=num_servings)
    
   
    print(f"Total cost for the meal plan: ${total_cost}")