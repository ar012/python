fruit_ranking = [1, 2, 3]
fruit_name = ['Mango', 'Pineapple', 'Watermelon']
fruit_rank_dict = {}

for i in range(len(fruit_ranking)):
    fruit_rank_dict[fruit_ranking[i]] = fruit_name[i]

print(fruit_rank_dict)

# uing dictionay comprehension
print("\nUsing dictionary comprehension")
fruit_ranking = [1, 2, 3, 4, 5]
fruit = ['Mango', 'Pineapple', 'Watermelon', 'Banana', 'Orange']
fruit_ranking_dict = {fruit_ranking[i] : fruit[i] for i in range(len(fruit_ranking))}
print(fruit_ranking_dict)