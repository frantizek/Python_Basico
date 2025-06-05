import sys

def demonstrate_variable_behavior(my_string_param, my_list_param):
    """
    This function illustrates how Python handles variables within different scopes,
    focusing on the concepts of mutability and immutability.

    In Python, arguments are passed by 'object reference'. This means:
    - For immutable objects (like strings, numbers, tuples), the function receives
      a *copy of the value*. Any modification inside the function creates a new
      object, and the local variable points to this new object, leaving the
      original object outside the function unaffected.
    - For mutable objects (like lists, dictionaries, sets), the function receives
      a *reference to the same object*. Modifications made to the object
    - using its methods (e.g., list.append()) inside the function will
      directly affect the original object outside the function.
    """

    print("\n" + "="*60)
    print(f"--- INSIDE FUNCTION: '{demonstrate_variable_behavior.__name__}' ---")
    print("Variables 'my_string_param' and 'my_list_param' are LOCAL to this function.")
    print("They initially point to the same objects that were passed from the caller.")
    print("="*60)

    # --- Initial State Inside Function ---
    print(f"\n[Function Scope] Initial my_string_param: '{my_string_param}'")
    print(f"[Function Scope] ID of my_string_param: {id(my_string_param)}")
    print(f"[Function Scope] Initial my_list_param: {my_list_param}")
    print(f"[Function Scope] ID of my_list_param: {id(my_list_param)}")
    print("-" * 60)

    # --- Demonstrating Immutability (Strings) ---
    print("\n--- Action: Modifying 'my_string_param' (an immutable string) ---")
    print("Strings are IMMUTABLE. Reassigning or modifying a string creates a NEW string object.")
    print("The local variable 'my_string_param' will now point to this new object.")

    old_string_id = id(my_string_param)
    my_string_param = my_string_param.upper() # Creates a new string object
    new_string_id = id(my_string_param)

    print(f"[Function Scope] my_string_param after .upper(): '{my_string_param}'")
    print(f"[Function Scope] Old ID of my_string_param: {old_string_id}")
    print(f"[Function Scope] New ID of my_string_param: {new_string_id}")
    if old_string_id != new_string_id:
        print(">>> OBSERVATION: The ID of 'my_string_param' CHANGED. This confirms a new object was created.")
    else:
        print(">>> ERROR: The ID of 'my_string_param' did NOT change. This indicates an unexpected behavior.")
    print("-" * 60)

    # --- Demonstrating Mutability (Lists) ---
    print("\n--- Action: Modifying 'my_list_param' (a mutable list) ---")
    print("Lists are MUTABLE. Operations like .append() modify the list IN-PLACE.")
    print("Since 'my_list_param' and the original variable outside the function point")
    print("to the SAME list object, changes here WILL affect the outside variable.")

    old_list_id = id(my_list_param)
    my_list_param.append(my_string_param) # Modifies the list object directly
    new_list_id = id(my_list_param)

    print(f"[Function Scope] my_list_param after .append(): {my_list_param}")
    print(f"[Function Scope] Old ID of my_list_param: {old_list_id}")
    print(f"[Function Scope] New ID of my_list_param: {new_list_id}")
    if old_list_id == new_list_id:
        print(">>> OBSERVATION: The ID of 'my_list_param' remained the SAME. This confirms in-place modification.")
    else:
        print(">>> ERROR: The ID of 'my_list_param' CHANGED. This indicates an unexpected behavior.")
    print("-" * 60)

    print("\n" + "="*60)
    print(f"--- EXITING FUNCTION: '{demonstrate_variable_behavior.__name__}' ---")
    print("="*60)

    # Returning a value explicitly to show how it can be used to update global state
    return my_string_param


# --- GLOBAL SCOPE ---
print("="*60)
print("--- GLOBAL SCOPE ---")
print("These variables exist outside any function and are accessible globally.")
print("="*60)

global_person_name = "Jennifer"
global_names_collection = ["GINNY", "JEAN"]

print(f"\n[Global Scope] Initial global_person_name: '{global_person_name}'")
print(f"[Global Scope] ID of global_person_name: {id(global_person_name)}")
print(f"[Global Scope] Initial global_names_collection: {global_names_collection}")
print(f"[Global Scope] ID of global_names_collection: {id(global_names_collection)}")
print("-" * 60)

# Call the function, passing the global variables as arguments
# The function will receive copies of references to these objects.
print("\n--- Calling 'demonstrate_variable_behavior' function ---")
# We can capture the return value to explicitly update a global variable if needed
returned_string = demonstrate_variable_behavior(global_person_name, global_names_collection)
print("\n--- Function call completed ---")
print("-" * 60)

# --- State After Function Call (Back in Global Scope) ---
print("\n" + "="*60)
print("--- BACK IN GLOBAL SCOPE ---")
print("Let's see the state of our global variables after the function call.")
print("="*60)

print(f"\n[Global Scope] global_person_name after function call: '{global_person_name}'")
print(f"[Global Scope] ID of global_person_name: {id(global_person_name)}")
print(f"   (Note: global_person_name is UNCHANGED because strings are immutable and")
print(f"          the function's local variable 'my_string_param' was reassigned to a new object.)")

print(f"\n[Global Scope] global_names_collection after function call: {global_names_collection}")
print(f"[Global Scope] ID of global_names_collection: {id(global_names_collection)}")
print(f"   (Note: global_names_collection IS CHANGED because lists are mutable and")
print(f"          the function modified the SAME list object in-place.)")

print(f"\n[Global Scope] Value returned by function: '{returned_string}'")
print(f"[Global Scope] ID of returned string: {id(returned_string)}")
print(f"   (This is the new string object created inside the function.)")

# If we wanted to update global_person_name with the modified string from the function:
# global_person_name = returned_string
# print(f"\n[Global Scope] If global_person_name was explicitly updated: '{global_person_name}'")
# print(f"[Global Scope] ID of global_person_name after explicit update: {id(global_person_name)}")

print("\n" + "="*60)
print("--- SUMMARY ---")
print("Python passes arguments by 'object reference'.")
print("- Immutable objects (like strings) mean local reassignments don't affect the original.")
print("- Mutable objects (like lists) mean in-place modifications DO affect the original.")
print("The 'id()' function helps visualize whether an object's identity has changed.")
print("Explicitly returning values is the clean way to pass data out of a function.")
print("="*60)