import tkinter as tk
from tkinter import messagebox

class Recipe:
    def __init__(self, name, preparation_time, serving_size, ingredients, preparation_description):
        self.name = name
        self.preparation_time = preparation_time
        self.serving_size = serving_size
        self.ingredients = ingredients
        self.preparation_description = preparation_description

class Ingredient:
    def __init__(self, name, unit, value_per_unit, place_of_purchase, calories_per_unit):
        self.name = name
        self.unit = unit
        self.value_per_unit = value_per_unit
        self.place_of_purchase = place_of_purchase
        self.calories_per_unit = calories_per_unit

    def __str__(self):
        return f"{self.name} ({self.unit}): ${self.value_per_unit:.2f}, {self.calories_per_unit} kcal"

class UserManagement:
    def __init__(self):
        # User data stored as a dictionary {username: {'password': password, 'role': role}}
        self.users = {'admin': {'password': 'admin', 'role': 'admin'}, 'chef': {'password': 'chef', 'role': 'chef'}}

    def add_user(self, username, password, role):
        # Add a new user to the user dictionary
        self.users[username] = {'password': password, 'role': role}
        messagebox.showinfo("User Added", f"User '{username}' added successfully.")

    def delete_user(self, username):
        # Delete a user from the user dictionary
        if username in self.users:
            del self.users[username]
            messagebox.showinfo("User Deleted", f"User '{username}' deleted successfully.")
        else:
            messagebox.showerror("Error", f"User '{username}' not found.")

    def change_user_role(self, username, new_role):
        # Change the role of an existing user
        if username in self.users:
            self.users[username]['role'] = new_role
            messagebox.showinfo("Role Changed", f"Role of user '{username}' changed to '{new_role}'.")
        else:
            messagebox.showerror("Error", f"User '{username}' not found.")

class MercedarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mercedario Recetas")

        # User and password placeholders for demonstration
        self.admin_credentials = {"admin": "admin"}
        self.chef_credentials = {"chef": "chef"}

        self.current_user = None
        self.recipes = []
        self.ingredients = []

        self.login_frame = tk.Frame(root)
        self.main_menu_frame = tk.Frame(root)
        self.manage_recipes_frame = tk.Frame(root)
        self.view_recipes_frame = tk.Frame(root)
        self.add_recipe_frame = tk.Frame(root)
        self.edit_recipe_frame = tk.Frame(root)
        self.delete_recipe_frame = tk.Frame(root)
        self.manage_ingredients_frame = tk.Frame(root)
        self.view_ingredients_frame = tk.Frame(root)
        self.add_ingredient_frame = tk.Frame(root)
        self.edit_ingredient_frame = tk.Frame(root)
        self.delete_ingredient_frame = tk.Frame(root)
        self.manage_users_frame = tk.Frame(root)

        self.user_management = UserManagement()  # Initialize UserManagement instance

        self.login()

    def login(self):
        self.login_frame.pack()

        label_username = tk.Label(self.login_frame, text="Username:")
        label_password = tk.Label(self.login_frame, text="Password:")

        entry_username = tk.Entry(self.login_frame)
        entry_password = tk.Entry(self.login_frame, show="*")

        label_username.grid(row=0, column=0, pady=5, padx=10, sticky=tk.W)
        label_password.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)
        entry_username.grid(row=0, column=1, pady=5, padx=10)
        entry_password.grid(row=1, column=1, pady=5, padx=10)

        button_login = tk.Button(self.login_frame, text="Login", command=lambda: self.check_credentials(entry_username.get(), entry_password.get()))
        button_login.grid(row=2, column=1, pady=10)

    def check_credentials(self, username, password):
        if username in self.admin_credentials and password == self.admin_credentials[username]:
            self.current_user = "admin"
            self.login_frame.pack_forget()
            self.show_main_menu()
        elif username in self.chef_credentials and password == self.chef_credentials[username]:
            self.current_user = "chef"
            self.login_frame.pack_forget()
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_main_menu(self):
        self.main_menu_frame.pack()

        label_welcome = tk.Label(self.main_menu_frame, text=f"Welcome, {self.current_user}!")
        label_welcome.pack(pady=10)

        button_manage_recipes = tk.Button(self.main_menu_frame, text="Manage Recipes", command=self.manage_recipes)
        button_manage_recipes.pack(pady=5)

        button_manage_ingredients = tk.Button(self.main_menu_frame, text="Manage Ingredients", command=self.manage_ingredients)
        button_manage_ingredients.pack(pady=5)

        button_manage_users = tk.Button(self.main_menu_frame, text="Manage Users", command=self.show_user_management)
        button_manage_users.pack(pady=10)

        button_logout = tk.Button(self.main_menu_frame, text="Logout", command=self.logout)
        button_logout.pack(pady=5)

    def hide_frames(self):
        # Hide all frames
        self.login_frame.pack_forget()
        self.main_menu_frame.pack_forget()
        self.manage_recipes_frame.pack_forget()
        self.view_recipes_frame.pack_forget()
        self.add_recipe_frame.pack_forget()
        self.edit_recipe_frame.pack_forget()
        self.delete_recipe_frame.pack_forget()
        self.manage_ingredients_frame.pack_forget()
        self.view_ingredients_frame.pack_forget()
        self.add_ingredient_frame.pack_forget()
        self.edit_ingredient_frame.pack_forget()
        self.delete_ingredient_frame.pack_forget()
        self.manage_users_frame.pack_forget()  # Added the line to hide the manage_users_frame

    def show_user_management(self):
        # Hide other frames and show User Management frame
        self.hide_frames()
        self.manage_users_frame.pack()

        # Add User button
        button_add_user = tk.Button(self.manage_users_frame, text="Add User", command=self.show_add_user)
        button_add_user.pack(pady=10)

        # Delete User button
        button_delete_user = tk.Button(self.manage_users_frame, text="Delete User", command=self.show_delete_user)
        button_delete_user.pack(pady=10)

        # Change User Role button
        button_change_role = tk.Button(self.manage_users_frame, text="Change User Role", command=self.show_change_role)
        button_change_role.pack(pady=10)

        button_back = tk.Button(self.manage_users_frame, text="Back to Main Menu", command=self.show_main_menu)
        button_back.pack(pady=10)

    def show_add_user(self):
        # Implementation for showing the add user interface
        # You can create a new frame or use a pop-up window for this
        add_user_frame = tk.Frame(self.root)
        add_user_frame.pack()

        tk.Label(add_user_frame, text="Username:").grid(row=0, column=0, pady=10)
        entry_username = tk.Entry(add_user_frame)
        entry_username.grid(row=0, column=1, pady=10)

        tk.Label(add_user_frame, text="Password:").grid(row=1, column=0, pady=10)
        entry_password = tk.Entry(add_user_frame, show="*")
        entry_password.grid(row=1, column=1, pady=10)

        tk.Label(add_user_frame, text="Role:").grid(row=2, column=0, pady=10)
        entry_role = tk.Entry(add_user_frame)
        entry_role.grid(row=2, column=1, pady=10)

        def save_user():
            username = entry_username.get()
            password = entry_password.get()
            role = entry_role.get()
            self.user_management.add_user(username, password, role)
            add_user_frame.destroy()

        tk.Button(add_user_frame, text="Save", command=save_user).grid(row=3, column=0, columnspan=2, pady=10)

    def show_delete_user(self):
        # Implementation for showing the delete user interface
        # You can create a new frame or use a pop-up window for this
        delete_user_frame = tk.Frame(self.root)
        delete_user_frame.pack()

        tk.Label(delete_user_frame, text="Username to delete:").grid(row=0, column=0, pady=10)
        entry_username = tk.Entry(delete_user_frame)
        entry_username.grid(row=0, column=1, pady=10)

        def delete_user():
            username = entry_username.get()
            self.user_management.delete_user(username)
            delete_user_frame.destroy()

        tk.Button(delete_user_frame, text="Delete", command=delete_user).grid(row=1, column=0, columnspan=2, pady=10)

    def show_change_role(self):
        # Implementation for showing the change user role interface
        # You can create a new frame or use a pop-up window for this
        change_role_frame = tk.Frame(self.root)
        change_role_frame.pack()

        tk.Label(change_role_frame, text="Username:").grid(row=0, column=0, pady=10)
        entry_username = tk.Entry(change_role_frame)
        entry_username.grid(row=0, column=1, pady=10)

        tk.Label(change_role_frame, text="New Role:").grid(row=1, column=0, pady=10)
        entry_role = tk.Entry(change_role_frame)
        entry_role.grid(row=1, column=1, pady=10)

        def change_role():
            username = entry_username.get()
            new_role = entry_role.get()
            self.user_management.change_user_role(username, new_role)
            change_role_frame.destroy()

        tk.Button(change_role_frame, text="Change Role", command=change_role).grid(row=2, column=0, columnspan=2, pady=10)

    def manage_recipes(self):
        self.manage_recipes_frame.pack()
        self.main_menu_frame.pack_forget()

        button_view_recipes = tk.Button(self.manage_recipes_frame, text="View Recipes", command=self.view_recipes)
        button_view_recipes.pack(pady=5)

        button_add_recipe = tk.Button(self.manage_recipes_frame, text="Add Recipe", command=self.add_recipe)
        button_add_recipe.pack(pady=5)

        button_edit_recipe = tk.Button(self.manage_recipes_frame, text="Edit Recipe", command=self.edit_recipe)
        button_edit_recipe.pack(pady=5)

        button_delete_recipe = tk.Button(self.manage_recipes_frame, text="Delete Recipe", command=self.delete_recipe)
        button_delete_recipe.pack(pady=5)

        button_plan_recipe = tk.Button(self.manage_recipes_frame, text="Plan Recipe", command=self.plan_recipe)
        button_plan_recipe.pack(pady=5)

        button_back = tk.Button(self.manage_recipes_frame, text="Back to Main Menu", command=self.show_main_menu)
        button_back.pack(pady=10)

    def view_recipes(self):
        self.view_recipes_frame.pack()
        self.manage_recipes_frame.pack_forget()

        text_widget = tk.Text(self.view_recipes_frame, height=20, width=50)
        text_widget.pack(pady=10)

        if self.recipes:
            for recipe in self.recipes:
                text_widget.insert(tk.END, f"Recipe: {recipe.name}\n")
                text_widget.insert(tk.END, f"Preparation Time: {recipe.preparation_time} hours\n")
                text_widget.insert(tk.END, f"Serving Size: {recipe.serving_size} people\n")
                text_widget.insert(tk.END, "Ingredients:\n")
                for ingredient in recipe.ingredients:
                    text_widget.insert(tk.END, f"  - {ingredient}\n")
                text_widget.insert(tk.END, f"Preparation Description: {recipe.preparation_description}\n")
                text_widget.insert(tk.END, "\n" + "=" * 50 + "\n")
        else:
            text_widget.insert(tk.END, "No recipes available.")

        button_back = tk.Button(self.view_recipes_frame, text="Back to Manage Recipes", command=self.manage_recipes)
        button_back.pack(pady=10)

    def add_recipe(self):
        self.add_recipe_frame.pack()
        self.manage_recipes_frame.pack_forget()

        label_name = tk.Label(self.add_recipe_frame, text="Recipe Name:")
        label_preparation_time = tk.Label(self.add_recipe_frame, text="Preparation Time (hours):")
        label_serving_size = tk.Label(self.add_recipe_frame, text="Serving Size:")
        label_ingredients = tk.Label(self.add_recipe_frame, text="Ingredients (comma-separated):")
        label_preparation_description = tk.Label(self.add_recipe_frame, text="Preparation Description:")

        entry_name = tk.Entry(self.add_recipe_frame)
        entry_preparation_time = tk.Entry(self.add_recipe_frame)
        entry_serving_size = tk.Entry(self.add_recipe_frame)
        entry_ingredients = tk.Entry(self.add_recipe_frame)
        entry_preparation_description = tk.Entry(self.add_recipe_frame)

        label_name.grid(row=0, column=0, pady=5, padx=10, sticky=tk.W)
        label_preparation_time.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)
        label_serving_size.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)
        label_ingredients.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)
        label_preparation_description.grid(row=4, column=0, pady=5, padx=10, sticky=tk.W)

        entry_name.grid(row=0, column=1, pady=5, padx=10)
        entry_preparation_time.grid(row=1, column=1, pady=5, padx=10)
        entry_serving_size.grid(row=2, column=1, pady=5, padx=10)
        entry_ingredients.grid(row=3, column=1, pady=5, padx=10)
        entry_preparation_description.grid(row=4, column=1, pady=5, padx=10)

        button_save = tk.Button(self.add_recipe_frame, text="Save Recipe", command=lambda: self.save_recipe(
            entry_name.get(), entry_preparation_time.get(), entry_serving_size.get(),
            entry_ingredients.get(), entry_preparation_description.get()
        ))
        button_save.grid(row=5, column=1, pady=10)

        button_back = tk.Button(self.add_recipe_frame, text="Back to Manage Recipes", command=self.manage_recipes)
        button_back.grid(row=6, column=1, pady=10)

    def save_recipe(self, name, preparation_time, serving_size, ingredients, preparation_description):
        new_recipe = Recipe(name, preparation_time, serving_size, ingredients.split(", "), preparation_description)
        self.recipes.append(new_recipe)
        messagebox.showinfo("Recipe Added", "Recipe added successfully.")
        self.manage_recipes()

    def edit_recipe(self):
        self.edit_recipe_frame.pack()
        self.manage_recipes_frame.pack_forget()

        label_choose_recipe = tk.Label(self.edit_recipe_frame, text="Choose a recipe to edit:")
        label_choose_recipe.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        recipe_choices = [recipe.name for recipe in self.recipes]
        selected_recipe = tk.StringVar()
        selected_recipe.set(recipe_choices[0] if recipe_choices else "")
        dropdown_recipe = tk.OptionMenu(self.edit_recipe_frame, selected_recipe, *recipe_choices)
        dropdown_recipe.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

        button_edit_selected = tk.Button(self.edit_recipe_frame, text="Edit Selected Recipe",
                                         command=lambda: self.edit_selected_recipe(selected_recipe.get()))
        button_edit_selected.grid(row=1, column=1, pady=10)

        button_back = tk.Button(self.edit_recipe_frame, text="Back to Manage Recipes", command=self.manage_recipes)
        button_back.grid(row=2, column=1, pady=10)

    def edit_selected_recipe(self, selected_recipe_name):
        selected_recipe = next((recipe for recipe in self.recipes if recipe.name == selected_recipe_name), None)

        if selected_recipe:
            self.add_recipe_frame.pack()
            self.manage_recipes_frame.pack_forget()

            entry_name = tk.Entry(self.add_recipe_frame, state=tk.DISABLED)
            entry_preparation_time = tk.Entry(self.add_recipe_frame)
            entry_serving_size = tk.Entry(self.add_recipe_frame)
            entry_ingredients = tk.Entry(self.add_recipe_frame)
            entry_preparation_description = tk.Entry(self.add_recipe_frame)

            entry_name.insert(0, selected_recipe.name)
            entry_preparation_time.insert(0, selected_recipe.preparation_time)
            entry_serving_size.insert(0, selected_recipe.serving_size)
            entry_ingredients.insert(0, ", ".join(selected_recipe.ingredients))
            entry_preparation_description.insert(0, selected_recipe.preparation_description)

            entry_name.grid(row=0, column=1, pady=5, padx=10)
            entry_preparation_time.grid(row=1, column=1, pady=5, padx=10)
            entry_serving_size.grid(row=2, column=1, pady=5, padx=10)
            entry_ingredients.grid(row=3, column=1, pady=5, padx=10)
            entry_preparation_description.grid(row=4, column=1, pady=5, padx=10)

            button_save = tk.Button(self.add_recipe_frame, text="Save Changes", command=lambda: self.save_recipe(
                entry_name.get(), entry_preparation_time.get(), entry_serving_size.get(),
                entry_ingredients.get(), entry_preparation_description.get()
            ))
            button_save.grid(row=5, column=1, pady=10)

            button_back = tk.Button(self.add_recipe_frame, text="Back to Manage Recipes", command=self.manage_recipes)
            button_back.grid(row=6, column=1, pady=10)
        else:
            messagebox.showerror("Error", "Selected recipe not found.")

    def plan_recipe(self):
        self.recipe_preparation_frame = tk.Frame(self.root)
        self.recipe_preparation_frame.pack()
        self.manage_recipes_frame.pack_forget()

        label_choose_recipe = tk.Label(self.recipe_preparation_frame, text="Choose a recipe to plan:")
        label_choose_recipe.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        recipe_choices = [recipe.name for recipe in self.recipes]
        selected_recipe = tk.StringVar()
        selected_recipe.set(recipe_choices[0] if recipe_choices else "")
        dropdown_recipe = tk.OptionMenu(self.recipe_preparation_frame, selected_recipe, *recipe_choices)
        dropdown_recipe.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

        label_num_people = tk.Label(self.recipe_preparation_frame, text="Number of People:")
        label_num_people.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)

        entry_num_people = tk.Entry(self.recipe_preparation_frame)
        entry_num_people.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

        button_plan_selected = tk.Button(self.recipe_preparation_frame, text="Plan Selected Recipe",
        command=lambda: self.plan_selected_recipe(selected_recipe.get(), entry_num_people.get()))
        button_plan_selected.grid(row=2, column=1, pady=10)

        button_back = tk.Button(self.recipe_preparation_frame, text="Back to Manage Recipes", command=self.manage_recipes)
        button_back.grid(row=3, column=1, pady=10)

    def plan_selected_recipe(self, selected_recipe_name, num_people):
        selected_recipe = next((recipe for recipe in self.recipes if recipe.name == selected_recipe_name), None)

        if selected_recipe:
            try:
                num_people = int(num_people)
                if num_people <= 0:
                    raise ValueError("Number of people must be a positive integer.")
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid input: {str(e)}")
                return

            self.recipe_preparation_frame.pack_forget()

            # Display Planned Recipe Frame
            self.planned_recipe_frame = tk.Frame(self.root)
            self.planned_recipe_frame.pack()

            # Display selected recipe details with the specified number of people
            label_recipe_name = tk.Label(self.planned_recipe_frame, text=f"Recipe: {selected_recipe.name}")
            label_prep_time = tk.Label(self.planned_recipe_frame, text=f"Preparation Time: {selected_recipe.preparation_time} hours")
            label_serving_size = tk.Label(self.planned_recipe_frame, text=f"Serving Size: {num_people} people")
            label_ingredients = tk.Label(self.planned_recipe_frame, text="Ingredients:")
            text_ingredients = tk.Text(self.planned_recipe_frame, height=10, width=50)
            text_ingredients.insert(tk.END, "\n".join([f"- {ingredient}" for ingredient in selected_recipe.ingredients]))
            label_prep_description = tk.Label(self.planned_recipe_frame, text=f"Preparation Description: {selected_recipe.preparation_description}")

            label_recipe_name.pack(pady=10)
            label_prep_time.pack(pady=5)
            label_serving_size.pack(pady=5)
            label_ingredients.pack(pady=5)
            text_ingredients.pack(pady=5)
            label_prep_description.pack(pady=10)

            # Calculate total cost and calories
            total_cost = sum([ingredient.value_per_unit for ingredient in selected_recipe.ingredients])
            total_calories = sum([ingredient.calories_per_unit for ingredient in selected_recipe.ingredients]) * num_people

            label_total_cost = tk.Label(self.planned_recipe_frame, text=f"Total Cost: ${total_cost:.2f}")
            label_total_calories = tk.Label(self.planned_recipe_frame, text=f"Total Calories: {total_calories} kcal")

            label_total_cost.pack(pady=5)
            label_total_calories.pack(pady=10)

            button_confirm_prep = tk.Button(self.planned_recipe_frame, text="Confirm Preparation", command=self.confirm_preparation)
            button_confirm_prep.pack(pady=10)

            button_back = tk.Button(self.planned_recipe_frame, text="Back to Main Menu", command=self.create_main_menu_frame)
            button_back.pack(pady=10)
        else:
            messagebox.showerror("Error", "Selected recipe not found.")

    def delete_recipe(self):
        self.delete_recipe_frame.pack()
        self.manage_recipes_frame.pack_forget()

        label_choose_recipe = tk.Label(self.delete_recipe_frame, text="Choose a recipe to delete:")
        label_choose_recipe.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        recipe_choices = [recipe.name for recipe in self.recipes]
        selected_recipe = tk.StringVar()
        selected_recipe.set(recipe_choices[0] if recipe_choices else "")
        dropdown_recipe = tk.OptionMenu(self.delete_recipe_frame, selected_recipe, *recipe_choices)
        dropdown_recipe.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

        button_delete_selected = tk.Button(self.delete_recipe_frame, text="Delete Selected Recipe",
                                           command=lambda: self.delete_selected_recipe(selected_recipe.get()))
        button_delete_selected.grid(row=1, column=1, pady=10)

        button_back = tk.Button(self.delete_recipe_frame, text="Back to Manage Recipes", command=self.manage_recipes)
        button_back.grid(row=2, column=1, pady=10)

    def delete_selected_recipe(self, selected_recipe_name):
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the recipe '{selected_recipe_name}'?"):
            self.recipes = [recipe for recipe in self.recipes if recipe.name != selected_recipe_name]
            messagebox.showinfo("Recipe Deleted", "Recipe deleted successfully.")
            self.manage_recipes()

    def manage_ingredients(self):
        self.manage_ingredients_frame.pack()
        self.main_menu_frame.pack_forget()

        button_view_ingredients = tk.Button(self.manage_ingredients_frame, text="View Ingredients", command=self.view_ingredients)
        button_view_ingredients.pack(pady=5)

        button_add_ingredient = tk.Button(self.manage_ingredients_frame, text="Add Ingredient", command=self.add_ingredient)
        button_add_ingredient.pack(pady=5)

        button_edit_ingredient = tk.Button(self.manage_ingredients_frame, text="Edit Ingredient", command=self.edit_ingredient)
        button_edit_ingredient.pack(pady=5)

        button_delete_ingredient = tk.Button(self.manage_ingredients_frame, text="Delete Ingredient", command=self.delete_ingredient)
        button_delete_ingredient.pack(pady=5)

        button_back = tk.Button(self.manage_ingredients_frame, text="Back to Main Menu", command=self.show_main_menu)
        button_back.pack(pady=10)

    def view_ingredients(self):
        self.view_ingredients_frame.pack()
        self.manage_ingredients_frame.pack_forget()

        text_widget = tk.Text(self.view_ingredients_frame, height=20, width=50)
        text_widget.pack(pady=10)

        if self.ingredients:
            for ingredient in self.ingredients:
                text_widget.insert(tk.END, f"Ingredient: {ingredient.name}\n")
                text_widget.insert(tk.END, f"Unit: {ingredient.unit}\n")
                text_widget.insert(tk.END, f"Value per Unit: {ingredient.value_per_unit}\n")
                text_widget.insert(tk.END, f"Place of Purchase: {ingredient.place_of_purchase}\n")
                text_widget.insert(tk.END, f"Calories per Unit: {ingredient.calories_per_unit}\n")
                text_widget.insert(tk.END, "\n" + "=" * 50 + "\n")
        else:
            text_widget.insert(tk.END, "No ingredients available.")

        button_back = tk.Button(self.view_ingredients_frame, text="Back to Manage Ingredients", command=self.manage_ingredients)
        button_back.pack(pady=10)

    def add_ingredient(self):
        self.add_ingredient_frame.pack()
        self.manage_ingredients_frame.pack_forget()

        label_name = tk.Label(self.add_ingredient_frame, text="Ingredient Name:")
        label_unit = tk.Label(self.add_ingredient_frame, text="Unit:")
        label_value_per_unit = tk.Label(self.add_ingredient_frame, text="Value per Unit:")
        label_place_of_purchase = tk.Label(self.add_ingredient_frame, text="Place of Purchase:")
        label_calories_per_unit = tk.Label(self.add_ingredient_frame, text="Calories per Unit:")

        entry_name = tk.Entry(self.add_ingredient_frame)
        entry_unit = tk.Entry(self.add_ingredient_frame)
        entry_value_per_unit = tk.Entry(self.add_ingredient_frame)
        entry_place_of_purchase = tk.Entry(self.add_ingredient_frame)
        entry_calories_per_unit = tk.Entry(self.add_ingredient_frame)

        label_name.grid(row=0, column=0, pady=5, padx=10, sticky=tk.W)
        label_unit.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)
        label_value_per_unit.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)
        label_place_of_purchase.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)
        label_calories_per_unit.grid(row=4, column=0, pady=5, padx=10, sticky=tk.W)

        entry_name.grid(row=0, column=1, pady=5, padx=10)
        entry_unit.grid(row=1, column=1, pady=5, padx=10)
        entry_value_per_unit.grid(row=2, column=1, pady=5, padx=10)
        entry_place_of_purchase.grid(row=3, column=1, pady=5, padx=10)
        entry_calories_per_unit.grid(row=4, column=1, pady=5, padx=10)

        button_save = tk.Button(self.add_ingredient_frame, text="Save Ingredient", command=lambda: self.save_ingredient(
            entry_name.get(), entry_unit.get(), entry_value_per_unit.get(),
            entry_place_of_purchase.get(), entry_calories_per_unit.get()
        ))
        button_save.grid(row=5, column=1, pady=10)

        button_back = tk.Button(self.add_ingredient_frame, text="Back to Manage Ingredients", command=self.manage_ingredients)
        button_back.grid(row=6, column=1, pady=10)

    def save_ingredient(self, name, unit, value_per_unit, place_of_purchase, calories_per_unit):
        new_ingredient = Ingredient(name, unit, value_per_unit, place_of_purchase, calories_per_unit)
        self.ingredients.append(new_ingredient)
        messagebox.showinfo("Ingredient Added", "Ingredient added successfully.")
        self.manage_ingredients()

    def edit_ingredient(self):
        self.edit_ingredient_frame.pack()
        self.manage_ingredients_frame.pack_forget()

        label_choose_ingredient = tk.Label(self.edit_ingredient_frame, text="Choose an ingredient to edit:")
        label_choose_ingredient.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        ingredient_choices = [ingredient.name for ingredient in self.ingredients]
        selected_ingredient = tk.StringVar()
        selected_ingredient.set(ingredient_choices[0] if ingredient_choices else "")
        dropdown_ingredient = tk.OptionMenu(self.edit_ingredient_frame, selected_ingredient, *ingredient_choices)
        dropdown_ingredient.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

        button_edit_selected = tk.Button(self.edit_ingredient_frame, text="Edit Selected Ingredient",
                                         command=lambda: self.edit_selected_ingredient(selected_ingredient.get()))
        button_edit_selected.grid(row=1, column=1, pady=10)

        button_back = tk.Button(self.edit_ingredient_frame, text="Back to Manage Ingredients", command=self.manage_ingredients)
        button_back.grid(row=2, column=1, pady=10)

    def edit_selected_ingredient(self, selected_ingredient_name):
        selected_ingredient = next((ingredient for ingredient in self.ingredients if ingredient.name == selected_ingredient_name), None)

        if selected_ingredient:
            self.add_ingredient_frame.pack()
            self.manage_ingredients_frame.pack_forget()

            entry_name = tk.Entry(self.add_ingredient_frame, state=tk.DISABLED)
            entry_unit = tk.Entry(self.add_ingredient_frame)
            entry_value_per_unit = tk.Entry(self.add_ingredient_frame)
            entry_place_of_purchase = tk.Entry(self.add_ingredient_frame)
            entry_calories_per_unit = tk.Entry(self.add_ingredient_frame)

            entry_name.insert(0, selected_ingredient.name)
            entry_unit.insert(0, selected_ingredient.unit)
            entry_value_per_unit.insert(0, selected_ingredient.value_per_unit)
            entry_place_of_purchase.insert(0, selected_ingredient.place_of_purchase)
            entry_calories_per_unit.insert(0, selected_ingredient.calories_per_unit)

            entry_name.grid(row=0, column=1, pady=5, padx=10)
            entry_unit.grid(row=1, column=1, pady=5, padx=10)
            entry_value_per_unit.grid(row=2, column=1, pady=5, padx=10)
            entry_place_of_purchase.grid(row=3, column=1, pady=5, padx=10)
            entry_calories_per_unit.grid(row=4, column=1, pady=5, padx=10)

            button_save = tk.Button(self.add_ingredient_frame, text="Save Changes", command=lambda: self.save_ingredient(
                entry_name.get(), entry_unit.get(), entry_value_per_unit.get(),
                entry_place_of_purchase.get(), entry_calories_per_unit.get()
            ))
            button_save.grid(row=5, column=1, pady=10)

            button_back = tk.Button(self.add_ingredient_frame, text="Back to Manage Ingredients", command=self.manage_ingredients)
            button_back.grid(row=6, column=1, pady=10)
        else:
            messagebox.showerror("Error", "Selected ingredient not found.")

    def delete_ingredient(self):
        self.delete_ingredient_frame.pack()
        self.manage_ingredients_frame.pack_forget()

        label_choose_ingredient = tk.Label(self.delete_ingredient_frame, text="Choose an ingredient to delete:")
        label_choose_ingredient.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        ingredient_choices = [ingredient.name for ingredient in self.ingredients]
        selected_ingredient = tk.StringVar()
        selected_ingredient.set(ingredient_choices[0] if ingredient_choices else "")
        dropdown_ingredient = tk.OptionMenu(self.delete_ingredient_frame, selected_ingredient, *ingredient_choices)
        dropdown_ingredient.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

        button_delete_selected = tk.Button(self.delete_ingredient_frame, text="Delete Selected Ingredient",
                                           command=lambda: self.delete_selected_ingredient(selected_ingredient.get()))
        button_delete_selected.grid(row=1, column=1, pady=10)

        button_back = tk.Button(self.delete_ingredient_frame, text="Back to Manage Ingredients", command=self.manage_ingredients)
        button_back.grid(row=2, column=1, pady=10)

    def delete_selected_ingredient(self, selected_ingredient_name):
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the ingredient '{selected_ingredient_name}'?"):
            self.ingredients = [ingredient for ingredient in self.ingredients if ingredient.name != selected_ingredient_name]
            messagebox.showinfo("Ingredient Deleted", "Ingredient deleted successfully.")
            self.manage_ingredients()

    def logout(self):
        self.current_user = None
        self.login_frame.pack()
        self.main_menu_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = MercedarioApp(root)
    root.mainloop()
