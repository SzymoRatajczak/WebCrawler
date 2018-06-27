from urllib.request import urlopen
from linker import LinkFinder
from WebCrawler import *


#Spider is thing that is going through the webpage and gathers all stuff we want
#to some extent spider may be treated like threat beceause we will run a few spiders simultaneously
#The very first spider-the first one beyond crawling the webpage
#is also responsible for creating directory and files (both for pendling and done url_addresses)


class Spider:
    project_name=''
    url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue=set()
    crawled=set()


    def __init__(self,project_name,url,domain_name):
        Spider.project_name=project_name
        Spider.url=url
        Spider.domain_name=domain_name
        Spider.queue_file=project_name+'_queue.txt'
        Spider.crawled_file=project_name+'_crawled.txt'
        self.preparation()
        self.crawling("first spider",url)

    # when i create file i automatically write sth down there
    # but i am not gonna read from file -i am gonna read form set
    # that is why i call Convert function
    @staticmethod
    def preparation():
        create_directory(Spider.project_name)
        create_file_queue(Spider.project_name,Spider.url)
        create_file_crawled(Spider.project_name,'')
        Spider.queue=Convert_From_File_To_Set(Spider.queue_file)
        Spider.crawled=Convert_From_File_To_Set(Spider.crawled_file)

#what thread is crawling what webpage
    @staticmethod
    def crawling(thread_name,url):
        if url not in Spider.crawled:



            print(thread_name+'is crawling'+url)
            print('queue'+str(len(Spider.queue)))
            Spider.queue.remove(url)
            Spider.crawled.add(url)




'''to return webpage link
  @staticmethod
  def gatherLinks(link):
    html_string=''
    try:
        response=urlopen(link)
        if response.getheader('Content-Type')=='text/html':
            html_bit=response.read()
            html_string=html_bit.decode('utf-8')
        finder=LinkFinder(Spider.start_url,link)
        finder.feed(html_string)
    except:
        print("Error can not crawl page")
        return  set()
    return  finder.Show()


'''







