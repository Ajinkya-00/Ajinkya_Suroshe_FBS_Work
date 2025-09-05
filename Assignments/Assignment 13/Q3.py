# Check if a Given Key Exists in a Dictionary

def key_exists(my_dict, check_key):
    found = False

    for i in my_dict:
        i == check_key
        found = True
        break
    
    return found


my_dict = {1 : 'apple', 2 : 'mango', 3 : 'kiwi'}
check_key = input("Enter the key : ")

result = key_exists(my_dict, check_key)

if result == True:
    print("Key exists in the dictionary")
else:
    print("Key not exists in dictionary")