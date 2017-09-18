# em-login-bot
Cisco Spark bot to log a user in with UCM Extension Mobility Feature
(See [https://www.ciscospark.com/] to check out what Cisco Spark is, then see [https://developer.ciscospark.com/] on bots)

Just say "log me in into <number on the phone>" and the bot will do it's best to do so.
When you are done for the day, just say "log me out" ...

## disclaimer
EM Login BOT is a Proof of Concept, provided 'as is' without support. Suggestions or questions can be left here in the comments, but will not be monitored regularly.

## versions
*v0.1*
Proof of Concept, it works ... most of the time. It also give some useful errors back ... most of the time

## commands
- hello
- log me in into <8XXXXXX>
- log me out
- help

## limitation
- Uses your primary profile only (cannot choose profile yet)
- No EMCC
- not handling multiple logins (if enabled on ucm)