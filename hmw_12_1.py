import random

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington",
                 "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine",
                      "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
                   "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson",
                    "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
              "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman", "Tom Hardy", "Joseph Gordon-Levitt"}
# a
oscar_winners.add("Emma Watson")
print(oscar_winners)
# c + b
oscar_winners_copy = oscar_winners.copy()
oscar_winners_copy.clear()
print(oscar_winners_copy)
# d
oscar_winners.remove("Meryl Streep")
print(oscar_winners)
# e
intersection_set = dark_knight_actors.intersection(titanic_actors)
print(intersection_set)
# f
intersection_set2 = avengers_actors.intersection(iron_man_actors)
print(intersection_set2)
# g
not_oscar_winners = actor_list.difference(oscar_winners)
print(not_oscar_winners)
# h
not_in_actor_list = avengers_actors.difference(actor_list)
print(not_in_actor_list)
# i
movie_cast_copy = movie_cast.copy()
minus_actor = random.choice(list(movie_cast_copy))
movie_cast_copy.remove(minus_actor)
print(movie_cast_copy)
# j
no_damon = movie_cast.remove("Matt Damon")
print(movie_cast)
# k
not_oscar_winners_2 = titanic_actors.difference(oscar_winners)
print(not_oscar_winners_2)
# l
oscar_winners.add("Daniel Day-Lewis")
oscar_winners.add("Cate Blanchett")
print(oscar_winners)
# n
union_set = dark_knight_actors.union(titanic_actors)
print(union_set)
# m
inter_section = dark_knight_actors.intersection(titanic_actors)
print(inter_section)
# o
print(dark_knight_rises_actors <= dark_knight_actors)
# p
print(legendary_actors >= oscar_winners)
# q
print(avengers_actors - iron_man_actors)
# r
print(dark_knight_actors ^ avengers_actors)
# s
print(iron_man_actors | dark_knight_actors)
# t
legendary_actors_frozenset = frozenset(legendary_actors)
print(legendary_actors_frozenset)

