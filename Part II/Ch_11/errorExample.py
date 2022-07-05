"""
errorExample.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 252). No Starch Press. Kindle Edition. 
"""

def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message.')

spam()


# this doesnt' work. the traceback text was supposed to be 
# printed to a txt file 

# import traceback


# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt, 'w')
#     errorFile.write(tracback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')
