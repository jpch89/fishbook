from . import web




@web.route('/')
def index():
    return 'hello'


@web.route('/personal')
def personal_center():
    pass
