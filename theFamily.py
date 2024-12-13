# Define the family tree
# I have used the family tree for Harry Potter
# Some of these characters have empty arrays for parents/siblings/children due to not being known

# Harry Potter Family Tree
harry_potter_family_tree = {
    "Harry Potter": {
        "parents": ["James Potter", "Lily Potter"],
        "children": ["James Sirius Potter", "Albus Severus Potter", "Lily Luna Potter"],
        "siblings": []
    },
    "James Potter": {
        "parents": ["Fleamont Potter", "Euphemia Potter"],
        "children": ["Harry Potter"],
        "siblings": []
    },
    "Lily Potter": {
        "parents": ["Mr. Evans", "Mrs. Evans"],
        "children": ["Harry Potter"],
        "siblings": ["Petunia Dursley"]
    },
    "Ginny Weasley": {
        "parents": ["Arthur Weasley", "Molly Weasley"],
        "children": ["James Sirius Potter", "Albus Severus Potter", "Lily Luna Potter"],
        "siblings": ["Ron Weasley", "Bill Weasley", "Charlie Weasley", "Percy Weasley", "Fred Weasley", "George Weasley"]
    },
    "Ron Weasley": {
        "parents": ["Arthur Weasley", "Molly Weasley"],
        "children": ["Rose Granger-Weasley", "Hugo Granger-Weasley"],
        "siblings": ["Ginny Weasley", "Bill Weasley", "Charlie Weasley", "Percy Weasley", "Fred Weasley", "George Weasley"]
    },
    "Hermione Granger": {
        "parents": ["Mr. Granger", "Mrs. Granger"],
        "children": ["Rose Granger-Weasley", "Hugo Granger-Weasley"],
        "siblings": []
    },
    "James Sirius Potter": {
        "parents": ["Harry Potter", "Ginny Weasley"],
        "children": [],
        "siblings": ["Albus Severus Potter", "Lily Luna Potter"]
    },
    "Albus Severus Potter": {
        "parents": ["Harry Potter", "Ginny Weasley"],
        "children": [],
        "siblings": ["James Sirius Potter", "Lily Luna Potter"]
    },
    "Lily Luna Potter": {
        "parents": ["Harry Potter", "Ginny Weasley"],
        "children": [],
        "siblings": ["James Sirius Potter", "Albus Severus Potter"]
    },
    "Rose Granger-Weasley": {
        "parents": ["Ron Weasley", "Hermione Granger"],
        "children": [],
        "siblings": ["Hugo Granger-Weasley"]
    },
    "Hugo Granger-Weasley": {
        "parents": ["Ron Weasley", "Hermione Granger"],
        "children": [],
        "siblings": ["Rose Granger-Weasley"]
    },
    "Arthur Weasley": {
        "parents": [],
        "children": ["Bill Weasley", "Charlie Weasley", "Percy Weasley", "Fred Weasley", "George Weasley", "Ron Weasley", "Ginny Weasley"],
        "siblings": []
    },
    "Molly Weasley": {
        "parents": [],
        "children": ["Bill Weasley", "Charlie Weasley", "Percy Weasley", "Fred Weasley", "George Weasley", "Ron Weasley", "Ginny Weasley"],
        "siblings": []
    },
    "Mr. Granger": {
        "parents": [],
        "children": ["Hermione Granger"],
        "siblings": []
    },
    "Mrs. Granger": {
        "parents": [],
        "children": ["Hermione Granger"],
        "siblings": []
    },
    "Fleamont Potter": {
        "parents": [],
        "children": ["James Potter"],
        "siblings": []
    },
    "Euphemia Potter": {
        "parents": [],
        "children": ["James Potter"],
        "siblings": []
    },
    "Mr. Evans": {
        "parents": [],
        "children": ["Lily Potter", "Petunia Dursley"],
        "siblings": []
    },
    "Mrs. Evans": {
        "parents": [],
        "children": ["Lily Potter", "Petunia Dursley"],
        "siblings": []
    },
    "Petunia Dursley": {
        "parents": ["Mr. Evans", "Mrs. Evans"],
        "children": ["Dudley Dursley"],
        "siblings": ["Lily Potter"]
    },
    "Dudley Dursley": {
        "parents": ["Petunia Dursley", "Vernon Dursley"],
        "children": [],
        "siblings": []
    }
}

def get_parents(name):
    return ", ".join(harry_potter_family_tree[name]["parents"])

# Get children name
def get_children(name):
    return ", ".join(harry_potter_family_tree[name]["children"])

# Get siblings name
def get_siblings(name):
    return ", ".join(harry_potter_family_tree[name]["siblings"])

# Find common ancestors
def find_common_ancestors(name1, name2):
    # Holds the final result
    common_ancestors = []

    # i being the key in this case
    for i in harry_potter_family_tree[name1]:
        # if any of the values of the keys for both names are equal
        if harry_potter_family_tree[name1][i] == harry_potter_family_tree[name2][i]:
            # then append as this is a common ancestor
            common_ancestors.append(harry_potter_family_tree[name1][i])
            # If the key is equal to parents, this means these two names have the same grandparents
            if i == "parents":
                # Essentially harry_potter_family_tree[name1][i][0], accesses the first value of the array in the 
                # parents key
                common_ancestors.append(harry_potter_family_tree[harry_potter_family_tree[name1][i][0]]["parents"])
                common_ancestors.append(harry_potter_family_tree[harry_potter_family_tree[name1][i][1]]["parents"])

    # remove any empty arrays
    common_ancestors.remove([])
    print(f"Common Ancestors: {common_ancestors}")
    
# Check if inputs are related
def is_related(name1, name2):
    # check if they have the same grandparent
    if harry_potter_family_tree[harry_potter_family_tree[name1]["parents"][0]]["parents"] in harry_potter_family_tree[harry_potter_family_tree[name2]["parents"][0]]["parents"]:
        return True
    # check if they have the same parents (i.e. they are siblings):
    elif harry_potter_family_tree[name1]["parents"] == harry_potter_family_tree[name2]["parents"]:
        return True
    # check if they have the same children
    elif harry_potter_family_tree[name1]["children"] == harry_potter_family_tree[name2]["children"]:
        return True
    # check if they share the same sibling
    elif harry_potter_family_tree[name1]["children"] in harry_potter_family_tree[name2]["children"]:
        return True
    else:
        return False

# Print family tree

def print_family_tree(name):
    print(name)
    # Print out the parents and children name using the functions aforementioned
    print(f"    Parents: {get_parents(name)}")
    print(f"    Children: {get_children(name)}")

    # Loop through all the values for the children of entered name
    for i in harry_potter_family_tree[name]["children"]:
        # Printing 'i' here is to print the name of the child
        print("     " + i)
        # Use the same logic as above and use the predefined functions to print out 
        # parents and children names
        print(f"      Parents: {get_parents(i)}")
        print(f"      Siblings: {get_siblings(i)}")


print_family_tree("Harry Potter") 