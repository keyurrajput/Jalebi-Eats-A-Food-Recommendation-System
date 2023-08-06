#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import random

def load_dataset():
    try:
        # Load the dataset from CSV file
        df = pd.read_csv('food_recipes.csv')
        return df
    except FileNotFoundError:
        print("Error: 'food_recipes.csv' file not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: 'food_recipes.csv' file is empty.")
        return None

def get_random_recipes(df, mood):
    # Filter the dataset based on the selected mood
    mood_recipes = df[df['mood_category'] == mood]
    
    # If there are fewer than 5 recipes available for the selected mood, adjust the number of samples
    n_samples = min(5, len(mood_recipes))
    
    # Select random recipes from the filtered dataset
    random_recipes = mood_recipes.sample(n=n_samples)
    return random_recipes

def main():
    # Load the dataset
    df = load_dataset()
    if df is None:
        return
    
    # Take user's name
    print("Welcome to Jalebi Eats! Food for your Mood!")
    print("A Food Recommendation service by Keyur Rajput")
    user_name = input("Please enter your name: ")
    
    # Greet the user
    print(f"Hello, {user_name}! How are you feeling today?")
    
    # Display mood options
    mood_options = ['Happy', 'Sad', 'Excited', 'Comfort', 'Neutral', 'Relax']
    print("Mood options:")
    for index, mood in enumerate(mood_options, 1):
        print(f"{index}. {mood}")
    
    # Take user's mood choice
    user_choice = input("Enter the number or name corresponding to your mood: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < 1 or user_choice > len(mood_options):
            print("Invalid choice. Please enter a valid number.")
            return
        selected_mood = mood_options[user_choice - 1]
    else:
        selected_mood = user_choice.capitalize()
        if selected_mood not in mood_options:
            print("Invalid choice. Please enter a valid number or mood name.")
            return
    
    # Get random recipes for the selected mood
    random_recipes = get_random_recipes(df, selected_mood)
    
    if random_recipes.empty:
        print(f"No recipes found for the '{selected_mood}' mood.")
    else:
        # Display the recipes
        print(f"\nHere are some recipes for your '{selected_mood}' mood:")
        for index, row in random_recipes.iterrows():
            print(f"\nRecipe {index + 1}:\n")
            print(f"Name: {row['Recipe Name']}")
            print(f"Prep Time: {row['Prep Time']}")
            print(f"Cook Time: {row['Cook Time']}")
            print(f"Total Time: {row['Total Time']}")
            print(f"Servings: {row['Servings']}")
            print(f"Ingredients: {row['Ingredients']}")
            print(f"Directions: {row['Directions']}")
            print(f"Rating: {row['Rating']}")
            print(f"Cuisine Type: {row['Cuisine Type']}")
            print(f"Nutrition: {row['Nutrition']}")
    
    # Greet and thank the user
    print("\nThank you! Enjoy your meal!")

if __name__ == "__main__":
    main()


# In[ ]:




