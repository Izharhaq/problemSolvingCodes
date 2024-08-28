s = "aaaaba"

def calculate_similarity(s):
    total_similarity = 0
    n = len(s)

    for i in range(n):
        suffix = s[i:]
        common_length = 0

        for j in range(len(suffix)):
            if s[j] == suffix[j]:
                common_length += 1
            else:
                break

        total_similarity += common_length

    return total_similarity

print(calculate_similarity(s))  # Expected output is 11
