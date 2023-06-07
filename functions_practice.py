def hello():
    print('hello user!!')

def pack(a, b, c):  #not sure if i was suppose to add a specific arguments so i just copied the solution code for the pack()
    return [a, b, c]

def eat_lunch(favorite_food):
    if len(favorite_food) == 0:
        print('My lunch box is empty!')
    else:
        for i in range(len(favorite_food)):
            if i == 0:
                print(f'First, I eat {favorite_food[0]}')
            else:
                print(f'Next, I eat {favorite_food[i]}')

hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["spaghetti"])
eat_lunch(["spaghetti", "bread", "tuna", "pizza"])
