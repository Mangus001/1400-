for x in range(100, 1000):
    c = x % 10  
    remaining = x // 10 
    
    a = remaining // 10
    b = remaining % 10
    
    result = 100 * c + 10 * b + a
    
    if result == 654:
        print(f"Ответ: {x}")
        break
