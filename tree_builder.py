class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        """Insert a report recursively; return whether the manager was found."""
        first_call = current_node is None
        if first_call:
            side = side.strip().lower()
            if side not in ("left", "right"):
                print("Please choose 'left' or 'right' for the employee's side.")
                return False
            current_node = self.root

        if current_node is None:
            print("The team is empty. Add a team lead first.")
            return False

        if current_node.name == manager_name:
            if getattr(current_node, side) is not None:
                print(f"The {side.upper()} side of {manager_name} is already occupied.")
            else:
                setattr(current_node, side, EmployeeNode(employee_name))
                print(f" {employee_name} added to the {side.upper()} of {manager_name}")
            return True

        # Only recurse into existing children so None never restarts at the root.
        for child in (current_node.left, current_node.right):
            if child is not None:
                if self.insert(manager_name, employee_name, side, child):
                    return True

        if first_call:
            print(f"Manager '{manager_name}' does not exist in the team.")
        return False

    def print_tree(self, node=None, level=0):
        """Print each employee before their reports, indented by depth."""
        if node is None:
            if level == 0:
                node = self.root
            if node is None:
                return

        print(f"{'    ' * level}- {node.name}")
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()
