#Question 1:

def number_of_pairs(gloves):
    colors={}
    result= 0
    for i in gloves:
        if i not in colors:
            colors[i] = 1
        elif i in colors:
            colors[i] += 1
    for i in colors.values():
            pair = i//2
            result += pair
    return result 
    pass


    #Part 2:
    
def number_to_string(num):
    return(str(num))



    #Part 3:
def solution(number):
    if number < 0:
        return 0
    total = 0
    for i in range(number): 
        if i % 3 == 0 or i % 5 == 0: 
            total += i 
    return total 







#Question 2:

def create_show(fireworks, show_time):
    fireworks.sort()
    show = []
    remaining_time = show_time


    while remaining_time > 0 and fireworks: 
           firework = random.choice(fireworks)

           if firework <= remaining_time:
               show.append(firework) 
               remaining_time -= firework

    else:
         fireworks.remove(firework) #O(1)

    return show