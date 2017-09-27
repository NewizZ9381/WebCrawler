# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page

def get_page(url):
    try:
        from urllib.request import urlopen
        return urlopen(url).read()
    except:
        return ""

def get_next_link(page):
    start_link = page.find('<a href=')
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, end_quote = get_next_link(page)
        if url:
            print (url)
            page = page[end_quote:]
        else:
            break

def get_all_links(page):
    links = []
    while True:
        url, end_quote = get_next_link(page)
        if url:
            links.append(url)
            page = page[end_quote:]
        else:
            break
    return links

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        print('1 tocrawl is ', tocrawl)
        print('1 crawled is ', crawled)
        print('*************************************')
        webpage = tocrawl.pop() #depth first search
        print(webpage)
        if webpage not in crawled:
            a = union(tocrawl, get_all_links(bytes.decode(get_page(webpage))))
            print('*************************************')
            print('a is ', a)
            crawled.append(webpage)
            print('tocrawl is ', tocrawl)
            print('*************************************')
            print('crawled is ', crawled)
            print('*************************************')
    return crawled
    
seed = "http://udacity.com"
print('*************************************')
print (crawl_web(seed))



