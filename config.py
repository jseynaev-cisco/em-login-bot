# Spark BOT
access_token=''
webhook_name = 'thehook'
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
    ["Server1","axlserver.myorg.net","emserver.myorg.net"],
    ["Server2","axlserver2.myorg.net","emserver2.myorg.net"],
]

# Help message
help_message = """
# I can log you in into your phone
Just say "log me in into <number>" and I'll do my best to do so.
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
