class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        all_responses = []
        for x in range(len(responses)):
            removed = set(responses[x])
            all_responses.extend(removed)

        final = {}
        for each in all_responses:
            final[each] = final.get(each, 0) + 1
        max_one = max(final.values())
        highest_freq = [key for key, value in final.items() if value == max_one]

        if len(highest_freq) == 1:
            return highest_freq[0]
        else:
            highest_freq.sort()
            return highest_freq[0]