import  threading
from queue import  Queue
from Spider import Spider
from domain import *
from WebCrawler import *


Project_Name="The WebCrawler"
Home_Page="http://codechannels.com/channel/thenewboston/"
Domain_Name=get_full_domain_name(Home_Page)
Queue_File=Project_Name+'_queue.txt'
Crawled_File=Project_Name+'_crawled.txt'
Number_Of_Threads=8
queue=Queue()
Spider(Project_Name,Home_Page,Domain_Name)


#create wroker threads
#Die when maix exits
def create_workers():
    for _ in range(Number_Of_Threads):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()

#do the next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawling(threading.current_thread().name,url)
        queue.task_done()



#each queued link is a new job
def create_jobs():
    for link in Convert_From_File_To_Set(Queue_File):
        queue.put(link)
    queue.join()
    crawl()


#check if items are in queue is so -crawl them
def crawl():
    queue_links=Convert_From_File_To_Set(Queue_File)
    if len(queue_links)>0:
        print(str(len(queue_links))+'links in the queue')


create_workers()
crawl()