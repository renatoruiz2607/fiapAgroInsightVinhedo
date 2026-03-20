def display_menu():
    print("\n=== Agro Insight Menu ===")
    print("1 - Add record")
    print("2 - List records")
    print("3 - Update record")
    print("4 - Delete record")
    print("0 - Exit")


def get_menu_option():
    display_menu()
    option = input("Choose an option: ").strip()
    return option