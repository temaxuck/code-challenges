class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        result = []
        s_len = len(s)

        def dfs(index, partition):
            if index == s_len:
                if len(partition) == 4:
                    result.append(".".join(partition))
                return

            if len(partition) == 4 and index < s_len:
                return

            if s[index] == "0":
                partition.append(s[index])
                dfs(index + 1, partition)
                partition.pop()
            else:
                for i in range(index + 1, s_len + 1):
                    if 0 <= int(s[index:i]) <= 255:
                        partition.append(s[index:i])
                        dfs(i, partition)
                        partition.pop()
                    else:
                        break

        dfs(0, [])

        return result


if __name__ == "__main__":
    s = "101023"
    print(Solution().restoreIpAddresses("25525511135"))
