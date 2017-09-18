# Spark BOT
access_token=''
webhook_name = ''
webhook_url=''

# UCM AXL API
AXL_username=''
AXL_password=''

# UCM EMAPI
EMAPI_username=''
EMAPI_password=''

# UCM Clusters to query
# name (just a reference), server where AXL is running, server where EMAPI is running
clusters = [
    ["Cluster1","axlserver1.mydomain.org","emserver1.mydomain.org"],
    ["Cluster2","axlserver2.mydomain.org","emserver2.mydomain.org"],  
]

# Help message
help_message = """
# I can log you in into your phone
Just say "log me in into <number on the screen>" and I'll do my best to do so.
When you are done for the day, just say "log me out" ...

### commands
- hello
- log me in into <number>
- log me out
- help

### limitation
- no EMCC
- Uses your primary profile only (cannot choose profile yet)
"""
