import os
tweet = "Tyneside toxic smog 'set to disappear by morning'  experts say http://t.co/r7Gi8mxiDJ #asthma"
os.chdir('/Users/aditimavalankar/Desktop/LastSem/IRE/Project/phase2/public_mm/bin/')
os.system('echo '+tweet+' | ./metamap')
