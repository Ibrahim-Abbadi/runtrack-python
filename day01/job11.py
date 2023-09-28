# Job 1.1 :

def draw_rectangle(w, h):
    if w < 2 or h < 2:
        print("Error, w and h must be at least 2.")
        return
    
    print('|' + '-' * (w - 2) + '|')
    
    for i in range(h - 2):
        print('|' + ' ' * (w - 2) + '|')
        
    print('|' + '-' * (w - 2) + '|')

# Test :
draw_rectangle(4, 4)  

