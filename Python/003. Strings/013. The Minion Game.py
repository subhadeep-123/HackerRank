def minion_game(string):
    # your code goes here
    v = 'AEIOU'
    k_score, s_score = 0, 0
    str_len = len(string)
    for i in range(str_len):
        if s[i] in v:
            k_score += (str_len-i)
        else:
            s_score += (str_len-i)

    if (k_score > s_score):
        print("Kevin", k_score)
    elif(k_score < s_score):
        print("Stuart", s_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
