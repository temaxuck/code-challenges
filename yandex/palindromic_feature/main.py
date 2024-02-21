if __name__ == "__main__":
    s = input()
    n = len(s)

    min_palindrome = None

    def helper(lp, rp):
        global min_palindrome

        while 0 <= lp and rp < n and s[lp] == s[rp]:
            cur_palindrome = s[lp : rp + 1]
            if len(cur_palindrome) > 1 and cur_palindrome < (
                min_palindrome or cur_palindrome + "a"
            ):
                min_palindrome = cur_palindrome
            lp -= 1
            rp += 1

    for i in range(n):
        helper(i, i)
        helper(i, i + 1)

    print(min_palindrome or -1)
