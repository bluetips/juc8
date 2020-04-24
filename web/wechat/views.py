from web.wechat import wechat


@wechat.route('/share')
def share():
    return "share page"
