# spam_amount = 0
# print(spam_amount)

# # Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
# spam_amount = spam_amount + 4

# if spam_amount > 0:
#     print("But I don't want ANY spam!")

# viking_song = "Spam " * spam_amount
# print(viking_song)

# print(5 / 2)
# print(6 / 2)
# print(type(spam_amount)) 


# hat_height_cm = 25
# my_height_cm = 190
# # How tall am I, in meters, when wearing my hat?
# total_height_meters = (hat_height_cm + my_height_cm) / 100
# print("Height in meters =", total_height_meters, "?")

# print(min(1, 2, 3))
# print(max(1, 2, 3))
# print(float(10))
# print(int(3.33))
# # They can even be called on strings!
# print(int('807') + 1)
# 
# alice_candies = 121
# bob_candies = 77
# carol_candies = 109
# to_smash = -1
# total = (alice_candies + bob_candies + carol_candies) % 3
# print(total)
# print(91%3)

# 

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

    def sum(a, b, c):
        return a + b + c
print(least_difference(1, 10, 100), "should be 9")