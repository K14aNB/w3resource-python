"""
Task
----
Write a python function to find the length of the longest increasing sub-sequence in a list.
"""


def longest_increasing_sub_sequence(my_list: list[int]) -> int:
    """
    Function to find the length of longest increasing sub-sequence in a list.
    """

    length: list[int] = []
    seq_len = 0

    for i in range(1, len(my_list) - 1):
        if my_list[i] - my_list[i - 1] == my_list[i + 1] - my_list[i]:
            if seq_len == 0:
                seq_len += 2
                length.append(seq_len)
            else:
                length[-1] += 1
                seq_len += 1

        elif my_list[i] - my_list[i - 1] == my_list[i - 1] - my_list[i - 2]:
            pass

        elif seq_len > 0:
            seq_len = 0

    if len(length) > 0:
        length.sort(reverse=True)
        return length[0]
    else:
        return 0


if __name__ == "__main__":
    my_list = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )

    print(f"Length of longest increasing sub-sequence in {
          my_list} = {longest_increasing_sub_sequence(my_list)}")
