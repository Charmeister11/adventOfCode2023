def part1():
    sum = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            res = [int(i) for i in list(line) if i.isdigit()]
            sum += res[0] * 10 + res[-1]
    return sum


def part2():
    dict_nums = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    sum = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            # find the index of each last word in the dictionary
            lw_indexes = [line.rfind(dict_nums[i]) for i in range(1, 10)]
            lw_index = max(lw_indexes)  # latest index
            if lw_index != -1:  # ensure that the word is in the line
                lw_num = lw_indexes.index(lw_index) + 1  # value of the latest word
                # replace the word with the number leaving the first letter and the last letter
                line = str(lw_num).join([line[:lw_index + 1], line[lw_index + len(dict_nums[lw_num]) - 1:]])

            # find the index of each first word in the dictionary
            fw_indexes = [line.find(dict_nums[i]) if line.find(dict_nums[i]) != -1 else float('inf') for i in
                          range(1, 10)]
            fw_index = min(fw_indexes)  # earliest index
            if fw_index != float('inf'):  # ensure that the word is in the line
                fw_num = fw_indexes.index(fw_index) + 1  # value of the earliest word
                # replace the word with the number leaving the first letter and the last letter
                line = str(fw_num).join([line[:fw_index + 1], line[fw_index + len(dict_nums[fw_num]) - 1:]])

            # find all the digits in the line
            res = [int(i) for i in list(line) if i.isdigit()]
            # add the first and last digit to the sum
            sum += res[0] * 10 + res[-1]
    return sum


if __name__ == "__main__":
    print(f"part 1 answer: part1()")
    print(f"part 2 answer: part2()")
