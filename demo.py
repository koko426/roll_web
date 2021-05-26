# _*_ coding:UTF-8 _*_
"""
__title__=''
__author__='Administrator'
__mtime__='2021/4/21'
# code is far away from bugs with the god animal protecting
  I love animals. They taste delicious. 

"""
import math

import flask
from flask import render_template, g, request, jsonify

from flask import Flask

app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template("index.html")


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


@app.route("/test_data", methods=['POST'])
def test_data():
    if request.method == 'POST':
        platform = request.form['platform']
        testDate = request.form['testDate']
    dataList = [{'case_num': '11111', 'case_name': '哈哈哈哈', 'env': '32', 'env_version': 'xxxxxxx', 'exec_num': '10',
                 'result': '通过', 'conclusion': '该版本延期测试'},
                {'case_num': '2222', 'case_name': '哈哈哈哈', 'env': '32', 'env_version': 'xxxxxxx', 'exec_num': '10',
                 'result': '通过', 'conclusion': '该版本延期测试'},
                {'case_num': '3333', 'case_name': '哈哈哈哈', 'env': '32', 'env_version': 'xxxxxxx', 'exec_num': '10',
                 'result': '不通过', 'conclusion': '该版本延期测试'},
                {'case_num': '4444', 'case_name': '哈哈哈哈', 'env': '32', 'env_version': 'xxxxxxx', 'exec_num': '10',
                 'result': '通过', 'conclusion': '该版本延期测试'},
                {'case_num': '5555', 'case_name': '哈哈哈哈', 'env': '32', 'env_version': 'xxxxxxx', 'exec_num': '10',
                 'result': '通过', 'conclusion': '该版本延期测试'},
                {'case_num': '66666', 'case_name': '哈哈哈哈', 'env': '32', 'env_version': 'xxxxxxx', 'exec_num': '10',
                 'result': '通过', 'conclusion': '该版本延期测试'}
                ]
    datas = {
        'dataList': dataList,
        'code': 200,

    }
    return jsonify(datas)


@app.route("/case_data", methods=['POST'])
def case_data():
    if request.method == 'POST':
        platform = request.form['platform']
        testDate = request.form['testDate']
    dataList = [
        {'id': 1, 'case_num': 'DSN_EzTS_5_1_3', 'case_name': '申报一批订单', 'exec_num': '10'},
        {'id': 2, 'case_num': 'DSN_EzTS_5_1_4', 'case_name': '哈哈哈哈', 'exec_num': '10'},
        {'id': 3, 'case_num': '3333', 'case_name': '哈哈哈哈', 'exec_num': '10'},
        {'id': 4, 'case_num': '4444', 'case_name': '哈哈哈哈', 'exec_num': '10'},
        {'id': 5, 'case_num': '5555', 'case_name': '哈哈哈哈', 'exec_num': '10'},
        {'id': 6, 'case_num': '6666', 'case_name': '哈哈哈哈', 'exec_num': '10'}
    ]
    datas = {
        'dataList': dataList,
        'code': 200,

    }
    return jsonify(datas)


@app.route("/scene_data", methods=['POST'])
def scene_data():
    if request.method == 'POST':
        id = request.form['id']
    sceneList = [
        {'scene_name': '场景' + str(id), 'scene_text': '申报一批订单，覆盖配置的业务，产品子类型及账户类型' + str(id)},
        {'scene_name': '场景' + str(id), 'scene_text': '哈哈哈哈' + str(id)},
        {'scene_name': '场景' + str(id), 'scene_text': '哈哈哈哈' + str(id)},
        {'scene_name': '场景' + str(id), 'scene_text': '哈哈哈哈' + str(id)},
        {'scene_name': '场景' + str(id), 'scene_text': '哈哈哈哈' + str(id)},
        {'scene_name': '场景' + str(id), 'scene_text': '哈哈哈哈' + str(id)}
    ]
    datas = {
        'sceneList': sceneList,
        'code': 200,

    }
    return jsonify(datas)


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
