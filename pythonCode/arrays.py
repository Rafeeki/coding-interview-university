def array_test():
    ar = [3, 2, 4, 5, 10, 13, 1]
    
    print("Created array of size: " + str(len(ar)))
    print(ar)
    
    ar.pop()
    ar.append(6)
    print("Popped last element and appended 6")
    print(ar)
    print("Index of 4: " + str(ar.index(4))) # index of given value
    
    ar.remove(4) # remove the first occurence of item with given value
    print("Removed 4: " + str(ar))
    
    del ar[2] # remove the 3rd item from the list
    print("Removed 3rd entry from list: " + str(ar))
    
    ar.insert(2, 7)
    print("Inserted 7 as 3rd entry in list: " + str(ar))
    
    ar.reverse()
    print("Reversed: " + str(ar))
    print("Sorted return: " + str(sorted(ar)))
    
    ar.sort()
    print("Sorted in place: " + str(ar))

def main():
    array_test()
    
if __name__ == "__main__":
    main()