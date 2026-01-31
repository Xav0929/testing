cloud_storage = []

while True:
    print("\n ===CLOUD STORAGE MENU===")
    print("\n1. Upload File")
    print("2. Remove File")
    print("3. View Cloud Storage")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "4":
        file_name = input("Enter file name to upload: ")
        cloud_storage.append(file_name)
        print(f"'{file_name}' has been uploaded.")
    else:
        if choice == "2":
            file_name = input("Enter file name to remove: ")
            if file_name in cloud_storage:
                cloud_storage.remove(file_name)
                print(f"'{file_name}' has been removed.")
            else:
                print("Error: File does not exist in cloud storage.")
        else:
            if choice == "3":
                if cloud_storage:
                    print("\nFiles in Cloud Storage:")
                    for file in cloud_storage:
                        print(f"- {file}")
                else:
                    print("Cloud storage is empty.")
            else:
                if choice == "4":
                    print("Exiting program")
                    break
                else:
                    print("Invalid option. Please choose from 1-4.")
