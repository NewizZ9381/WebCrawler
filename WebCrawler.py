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
        
#page = get_page("http://xkcd.com/353")
#url, end_quote = get_next_link(page)
#print (url)
#print (end_quote)
        
page = '"zskchakdsuhaudh <a href="1.com">dasdasdasdasdasdasd <a href="2.com"> xxxxxxxxxxxxxxxxxxxxx <a href="3.com">'
print_all_links(page)



