letter_cases = "abcdefghjkmnpqrstuvwxy"
TOKEN_163= 'zy1991'

exclude_path=[
    '/blog_user/login_page.html',
    '/blog_user/register.html',
    '/blog_user/register/',
    '/blog_user/login/',
    '/blog_user/logout/',
    '/blog_user/send_check_num/',
    '/blog_user/del_num/',
    '/blog_user/is_name_valid/',

    '/likes/like_btn/',

    '/read_num/all_read_num/',
    '/read_num/read_num/',

    '/blog_article/sub_article/',
    '/read_num/all_read_num/',
]

article_page = 5
comment_page = 2
bbs_page = 5


'''python manage.py celery worker -c 4 --loglevel=info'''
'''激活虚拟环境   source virtualenvwrapper.sh'''

'''wel_email'''
SEND_HTML_MESSAGE = '<h1>包含 html 标签且不希望被转义的内容</h1>'
SEND_TITLE = '欢迎'
SEND_MESSAGE = '谢谢您注册我的网站，祝你愉快'