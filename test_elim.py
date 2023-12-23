import random
import pdb

num_people = 10
losses = {k: 0 for k in range(1, num_people+1)}

# for i in range(100000):
#     people = list(range(num_people))
#     while len(people) > 1:
#         chosen_person = random.randint(0, len(people)-1)
#         losses[people[chosen_person]] += 1
#         people.pop(chosen_person)


for j in range(100):
    last_num = -1

    for i in range(100000):
        num = random.randint(1, num_people)
        if num == last_num:
            losses[num] += 1
        last_num = num


pdb.set_trace()
