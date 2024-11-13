import random

def get_random_nums():
    random_nums = [[random.randint(1, 10) for num in range(4)] for equasion in range(25)]
    return random_nums

def create_equasions(nums):
    with open('data/equasions.txt', 'w') as file:
        for i, equasion in enumerate(nums):
            if i == len(nums) - 1:
                file.write(f"({equasion[0]} + {equasion[1]}) * {equasion[2]} - {equasion[3]}")
            else:
                file.write(f"({equasion[0]} + {equasion[1]}) * {equasion[2]} - {equasion[3]}\n")

def create_solutions(nums):
    with open('data/solutions.txt', 'w') as file:
        for i, equasion in enumerate(nums):
            solution = str((equasion[0] + equasion[1]) * equasion[2] - equasion[3])
            if i == len(nums) - 1:
                file.write(f"{solution}")
            else:
                file.write(f"{solution}\n")

def setup_data():
    random_nums = get_random_nums()
    create_equasions(random_nums)
    create_solutions(random_nums)


if __name__ == "__main__":
    random.seed(1) 
    setup_data()