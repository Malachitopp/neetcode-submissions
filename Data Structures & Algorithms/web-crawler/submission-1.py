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
        array = startUrl.split("/") 
        toLookFor = array[2]

        seen = set() 
        seen.add(startUrl)
     
        def dfs(url):
            for u in htmlParser.getUrls(url):
                compare = u.split('/')[2]
                if toLookFor == compare and u not in seen:
                    seen.add(u)
                    dfs(u) 
        dfs(startUrl)
        return [url for url in seen]