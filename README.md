# food_blog_backend

This is a good opportunity to practice my skills and build a tool that would collect data in a database. It will allow creating a database of recipes that will be able to used in the blog with the recipes. 


Objectives

    1. Create a database. Pass the name of the database to the script as an argument.
    2. Create a table named meals with two columns: meal_id of an integer type with the primary key attribute,
    and meal_name of a text type and with the unique and not null attribute.
    3. Create a table named ingredients with two columns: ingredient_id of an integer type with the primary key
    attribute and ingredient_name of a text type with the unique and not null attribute. 
    Multi-word ingredients are out of scope, I don't implement their support in this script.
    4. Create a table named measures with two columns: measure_id of an integer type with the primary key attribute,
    and measure_name of a text type with the unique attribute.
    5. Create a table named recipes with three columns: recipe_id of an integer type with the primary key attribute,
    recipe_name of a text type with the not-null attribute, and recipe_description of a text type.
    6. Populate the tables. Those tables are the dictionaries for the Food Blog system.

    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
     
     7. Prepare a simple system that allows to populate this table. Ask for the recipe name and the cooking directions, and
     insert the data into the table.
     8. When a zero-length string is entered for the recipe name the script should terminate.

   
   
Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

> python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: > Cold milk
Recipe description: > Freeze milk
Recipe name: > Hot milk
Recipe description: > Boil milk
Recipe name: >

