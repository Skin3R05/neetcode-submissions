class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        ans=0
        for j in dic:
            
            for i in range(len(s)):
                m=i
                t=0
                kt=k
                while(kt>-1 and m<len(s)):
                    if s[m]==j:
                        t+=1
                        m+=1
                    elif kt>0:
                        kt-=1
                        t+=1
                        m+=1
                    else:
                        kt-=1
                
                if t>ans:
                    ans=t
            
        return ans

        
