# _*_ coding:UTF-8 _*_
"""
__title__=''
__author__='wukeke'
__mtime__='2021/5/20'
# code is far away from bugs with the god animal protecting
  I love animals. They taste delicious. 

"""
import math

import flask
from flask import render_template, g, request, jsonify, abort

from flask import Flask

from roll_controller import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)


@app.route('/index.html')
def index():
    """
    主页
    :return:
    """
    return render_template("index.html")


@app.route('/case.html')
def case():
    """
    用例
    :return:
    """
    return render_template("case.html")


@app.route('/monitoring.html')
def monitoring():
    return render_template("monitoring.html")


@app.route('/conclusion.html')
def conclusion():
    return render_template("conclusion.html")


# ######## version 1.1 #########
@app.route('/conclusion_bak.html')
def conclusion_bak():
    return render_template("conclusion_bak.html")


@app.route('/index_bak.html')
def index_bak():
    return render_template("index_bak.html")


# ######## version 1.1 #########

@app.route('/page')
def page():
    page = flask.request.args.get('page')
    return render_template(page)


@app.route('/side.html')
def side():
    return render_template("common/side.html")


@app.route('/header.html')
def header():
    return render_template("common/header.html")


@app.route('/footer.html')
def footer():
    return render_template("common/footer.html")


@app.errorhandler(404)
def page_not_found(e):
    print("444444444444444444444")
    return render_template('common/404.html'),404


@app.route("/user_list", methods=['POST', 'GET'])
def user_list():
    pageNo = flask.request.args.get('p')
    print("--------------pageNo:", pageNo)
    # p = g.args.get("p", '')  # 页数
    p = pageNo
    show_shouye_status = 0  # 显示首页状态

    if p == '':
        p = 1
    else:
        p = int(p)
        if p > 1:
            show_shouye_status = 1

    # mdb = db_session()
    limit_start = (int(p) - 1) * 1  # 起始

    sql = "select * from page_text limit {0},10".format(limit_start)
    print(sql)
    # 此处是查询语句查出的数据
    user_list = ["张三" + str(p)]

    sql = "select count(id) as total from page_text"
    # # 此处是查询语句查出的数据
    # count = mdb.getOne(sql)['total'] #总记录
    count = 100  # 总记录
    total = int(math.ceil(count / 1.0))  # 总页数

    dic = get_page(total, p)
    datas = {
        'user_list': user_list,
        'p': int(p),
        'total': total,
        'show_shouye_status': show_shouye_status,
        'dic_list': dic

    }
    return render_template("user_list.html", datas=datas)
    # return '<h1>Hello World</h1>'


def get_page(total, p):
    show_page = 10  # 显示的页码数
    pageoffset = 2  # 偏移量
    start = 1  # 分页条开始
    end = total  # 分页条结束

    if total > show_page:
        if p > pageoffset:
            start = p - pageoffset
            if total > p + pageoffset:
                end = p + pageoffset
            else:
                end = total
        else:
            start = 1
            if total > show_page:
                end = show_page
            else:
                end = total
        if p + pageoffset > total:
            start = start - (p + pageoffset - end)
    # 用于模版中循环
    dic = range(start, end + 1)
    return dic


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=80)
