def check_EvenOdd(list):
    try:
        for i in range(i, len(list)):
            if i % 2 == 0:
                print(list[i], "this is even")
            else:
                print(list[i], "this is odd")
except Exception as e:
    print(f"this is en error {str(e)}")
    
