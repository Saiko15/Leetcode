class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubsequence(s1, s2):
            n,m = len(s1),len(s2)
            i,j = 0,0
            while (i < n and j < m):
                if (s1[i] == s2[j]):
                    i += 1
                j += 1
            return i == n
			
        count = 0
        a = {}
		
        for i in words:
            if i not in a.keys():
                if issubsequence(i,s) == True:
                    a[i] = True
                    count+=1
                else:
                    a[i]=False                  
            else:
                if a[i]==True:
                    count+=1
					
        return count