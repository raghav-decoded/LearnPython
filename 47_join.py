'''
"STRING".join(LIST)
    joins a list by using STRING between two consecutive elements
'''

lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# for item in lis:
#     print(item, "and", end=" ")

a = ", ".join(lis)
print(a, "other wwe superstars")
