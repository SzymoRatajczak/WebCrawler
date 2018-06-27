import os

#here are some functions used by Spider(s)

def create_directory(directory):
    if not os.path.exists(directory):
        print("crrating directory:" +directory)
        os.makedirs(directory)



def create_file_queue(project_name,start_point):
    queue=project_name+'_queue.txt'
    write_file(queue,start_point)


def create_file_crawled(project_name,start_point):
    crawled=project_name+'_crawled.txt'
    write_file(crawled,' ')



def write_file(file,start_point):
    fw=open(file,'a')
    fw.write(start_point+'\n')
    fw.close()


#it will be using by spider beceause  i do not allow spider read from file
#spider can read merely from set
def Convert_From_File_To_Set(file):
    result=set()
    f=open(file,"rt")
    line=f.read()
    result.add(line)
    return result




def Convert_From_Set_To_File(result):
    f=open("Result_Crawling.txt",'a')
    f.write(str(result)+'\n' )
    f.close()




