import sys


def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(x - median) for x in nums)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task_4.py numbers.txt")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        nums = [int(line.strip()) for line in f if line.strip()]

    moves = min_moves(nums)

    if moves > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(moves)
