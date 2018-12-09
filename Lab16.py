# Lab 16 - Web Scraping

import urllib.request

def makePage():
    # replace the directory in the line below with the path to your file
    file1 = open("superweb.html", "wt")
    file1.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">

  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
    file1.close()

# This method scrapes the 10 latest latest blog post titles and the direct links to these posts
# With this data, a new HTML file is created with these titles hyperlinked to their sources.
# Source: http://www.kazemicode.org/blog/blog
def getLatestPosts(source, target):
    target.write("<h1>Latest posts on kazemicode.org</h1>")
    ahref_start = "<h1 class=\"entry-title\"><a href=\""
    goal_start = "/\" rel=\"bookmark\">" # HTML code directly preceding blog titles / same as href_end
    goal_end = "</a></h1>"  # HTML code directly following blog titles
    ahref_psn = source.find(ahref_start, 0)
    psn = source.find(goal_start, 0) # position starts at first instance of goal_start
    while source.find(goal_start, psn) > -1: # as long as we still find occurrences of goal_start in source
        psn = source.find(goal_start, psn)  # psn reassigned to position of the next occurrence of goal_start
        ahref_psn = source.find(ahref_start, ahref_psn)
        link_start = ahref_psn + len(ahref_start)
        link_end = source.find(goal_start, link_start)
        start = psn + len(goal_start)   # start of the blog title is right after the end of goal_start
        end = source.find(goal_end, start) # end of the blog title is right before the start of goal_end
        target.write("<p><a href=\"" + source[link_start:link_end] + "\">" + source[start:end]+"</a></p>\n") # append title to the list
        psn = start # reassign psn to just after the last goal_start we found ends
        ahref_psn = link_start

file = open("scrapings.html", "wt")
html_file = urllib.request.urlopen("http://www.kazemicode.org/blog/blog").read().decode("utf-8")
#print(html_file)
getLatestPosts(html_file, file)
file.close()
