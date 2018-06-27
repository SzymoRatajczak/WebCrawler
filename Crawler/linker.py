from html.parser import HTMLParser
from urllib import parse



#this class is responsible for parsing webpage  form starting point which is base_url
#follow by outcome will be stored in result set
#but this is just funcionality
class LinkFinder(HTMLParser):

    def __init__(self,base_url):
        super().__init__()
        self.base_url=base_url
        self.links=set()


    def handle_starttag(self, tag, attrs):
        if tag=='a':
            for(attributes,value)in attrs:
                if attributes=='href':
                    url=parse.urljoin(self.base_url,value)
                    self.links.add(url)


    def Show(self):
        return  self.links


    def error(self, message):
        pass




