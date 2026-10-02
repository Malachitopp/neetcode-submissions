# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    

        array=startUrl.split('/')
        toLookFor = array[2]

        seen = set({startUrl}) 

        def dfs(url):
            for nxt in htmlParser.getUrls(url):
                if nxt in seen:
                    continue 
                partition = nxt.split('/')
                if partition[2] == toLookFor:
                    seen.add(nxt)
                    dfs(nxt) 
        dfs(startUrl)
        return [url for url in seen]

