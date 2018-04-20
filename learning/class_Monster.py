# The blueprint to create monsters
class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

# Create some real monsters
fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 4)
tangleface = Monster("Read", 3)

# Check whethere those monsters got different existence in memory or not
print('I have ' + str(fogthing.heads) + ' heads and I\'m ' + fogthing.color)
print('I also have ' + str(mournsnake.heads) + ' heads and I\'m ' + mournsnake.color)
print('I got ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color)

#
# # The blueprint to create monsters
# class Monster:
#     def __init__(self, color, heads, legs):
#         self.color = color
#         self.heads = heads
#         self.legs = legs
#
# # Create some real monsters
# fogthing = Monster("Black", 5, 5)
# mournsnake = Monster("Yellow", 4, 4)
# tangleface = Monster("Read", 3, 3)
# tinckle = Monster("Blue", 2, 5)
#
# # Check whethere those monsters got different existence in memory or not
# print('I have ' + str(fogthing.heads) + ' heads and I\'m ' + fogthing.color)
# print('I also have ' + str(mournsnake.heads) + ' heads and I\'m ' + mournsnake.color)
# print('I got ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color)
# print('I obtained ' + str(tinckle.heads) + ' heads, ' + str(tinckle.legs) + ' legs and I\'m ' + tinckle.color)