class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}

        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)

            parts = domain.split('.')

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])

                if subdomain in freq:
                    freq[subdomain] += count
                else:
                    freq[subdomain] = count

        result = []
        for dom, cnt in freq.items():
            result.append(str(cnt) + " " + dom)

        return result
