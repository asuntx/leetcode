from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        ballon = ["b", "a", "l", "o", "n"]
        if len(text) <= len(ballon) + 1:
            return 0
        for key in text_counter.copy():
            if key not in ballon:
                text_counter.pop(key)
        if len(text_counter.keys()) != len(ballon):
            return 0
        if text_counter["l"] < 2 and text_counter["o"]:
            return 0
        text_counter["l"] /= 2
        text_counter["o"] /= 2
        return int(min(list(text_counter.values())))


sol = Solution()
print(
    sol.maxNumberOfBalloons(
        "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    )
)
