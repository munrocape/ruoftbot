import praw

def getpw():
    '''
        Gets the accounts pw cause TBH I'm too lazy to use environment variables
        right now. When I'm ready for production then I'll use oauth and do
        everything correctly
    '''

    f = open('pw.txt', 'r')
    pw = f.read().strip()
    f.close()
    return pw




if __name__ == '__main__':
    r = praw.Reddit('Custom bot for r/uoft by /u/ssjjawa')

    pw = getpw()
    r.login('ruoftbot', getpw())

    r.send_message('ssjjawa', 'Subject Line', 'You are awesome!')
