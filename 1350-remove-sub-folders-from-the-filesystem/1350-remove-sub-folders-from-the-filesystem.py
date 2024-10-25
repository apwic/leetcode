class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]

        for f in folder[1:]:
            before = ans[-1] + '/'

            if not f.startswith(before):
                ans.append(f)

        return ans