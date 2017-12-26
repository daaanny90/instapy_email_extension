from instapy import InstaPy
from extension.instapy_email_extension import instapyEmailExtension

try:

    insta_username = ''
    insta_password = ''

    # if you want to run this script on a server, 
    # simply add nogui=True to the InstaPy() constructor
    session = InstaPy(username=insta_username, password=insta_password)
    session.login()

    # send email after login
    email_send_start()

    # set up all the settings
    session.set_upper_follower_count(limit=2500)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
    session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza', 'girl'])

    # do the actual liking
    session.like_by_tags(['natgeo', 'world'], amount=100)

    # end the bot session
    session.end()

    # send email when finished
    email_send_end()

except Exception as e:
    
    #send email if something goes wrong
    send_email_err(e)