if __name__ == "__main__":
    s = input()
    n = len(s)

    palindromes = []

    def helper(lp, rp):
        while 0 <= lp and rp < n and s[lp] == s[rp]:
            palindrome = s[lp : rp + 1]
            if len(palindrome) > 1:
                palindromes.append(palindrome)
            lp -= 1
            rp += 1

    for i in range(n):
        helper(i, i)
        helper(i, i + 1)
        if palindromes:
            break

    print(min(palindromes) if palindromes else -1)
