import enum

class Color(enum):
    RED = 0
    GREEN = 1
    BLUE = 2

color = input('Please input the color ')

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")