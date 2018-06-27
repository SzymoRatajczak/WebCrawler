from urllib.parse import  urlparse

#to return sub address of page firest of all we must get ful address

def get_subDomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ' '

def get_full_domain_name(url):
    try:
        result=get_subDomain_name(url).split()
        return  result[-3] + " " + result[-2]
    except:
        return  ''