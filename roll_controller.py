# _*_ coding:UTF-8 _*_
"""
__title__=''
__author__='wukeke'
__mtime__='2021/5/27'
# code is far away from bugs with the god animal protecting
  I love animals. They taste delicious. 

"""
import random

from flask import request, jsonify, Flask, Blueprint

simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route("/get_date_by_project", methods=['POST'])
def get_date_by_project():
    """
    查询该项目名下的所有测试日期
    :return:
    """
    # 此处创造缓存数据用来测试
    date_list_xzq = ['2021-05-01', '2021-05-20', '2021-05-27']
    date_list_bpc = ['2021-05-01', '2021-05-19', '2021-05-20', '2021-05-21']
    date_list_roll = ['2021-05-01', '2021-05-22', '2021-05-30']
    default = ['2021-05-01']

    dict_date = {'bpc': date_list_bpc, 'xzq': date_list_xzq, 'roll': date_list_roll, 'default': default}

    code = 200
    msg = 'success'
    if request.method == 'POST':
        project_name = request.form['project_name']
        if project_name is None:
            code = 500
            msg = "请选择一个项目"
            project_name = 'default'

        datas = {
            'date_list': dict_date[project_name],
            'code': code,
            'msg': msg
        }
    return jsonify(datas)


@simple_page.route("/reload_chart_data", methods=['POST'])
def reload_chart_data():
    """
    主页数据，根据选择的值，重新加载echart数据
    :return:
    """
    # 此处创造缓存数据用来测试
    series_list = []
    series_list04 = []

    series_list.append(random.randint(100, 600))
    series_list.append(random.randint(100, 600))
    series_list.append(random.randint(300, 600))
    series_list.append(random.randint(200, 600))
    series_list.append(random.randint(100, 600))
    series_list.append(random.randint(500, 600))
    series_list.append(random.randint(100, 600))

    series_list04.append(random.randint(1000, 1500))
    series_list04.append(random.randint(500, 800))
    series_list04.append(random.randint(100, 1500))
    series_list04.append(random.randint(1000, 1500))
    series_list04.append(random.randint(900, 1500))
    series_list04.append(random.randint(100, 200))
    series_list04.append(random.randint(1, 30))

    code = 200
    msg = 'success'
    if request.method == 'POST':
        project_name = request.form['project_name']
        test_date = request.form['test_date']
        if project_name is None or test_date is None:
            code = 500
            msg = "请选择一个项目或者测试日期"

        datas = {
            'series_list': series_list,
            'series_list04': series_list04,
            'code': code,
            'msg': msg
        }
    return jsonify(datas)


@simple_page.route("/reload_chart_conclusion", methods=['POST'])
def reload_chart_conclusion():
    """
    测试结论页面，根据选择的值，重新加载echart数据
    :return:
    """
    # 此处创造缓存数据用来测试
    # 饼图
    series_list = []

    dict_1 = {'value': random.randint(100, 600), 'name': '搜索引擎'}
    dict_2 = {'value': random.randint(40, 100), 'name': '直接访问'}
    dict_3 = {'value': random.randint(800, 1400), 'name': '邮件营销'}
    dict_4 = {'value': random.randint(100, 300), 'name': '联盟广告'}
    dict_5 = {'value': random.randint(400, 600), 'name': '视频广告'}

    series_list.append(dict_1)
    series_list.append(dict_2)
    series_list.append(dict_3)
    series_list.append(dict_4)
    series_list.append(dict_5)

    # 列表
    dataList = [
        {'case_num': '11111' + str(random.randint(100, 600)), 'case_name': '哈哈哈哈', 'env': str(random.randint(20, 50)),
         'env_version': 'xxxxxxx', 'exec_num': '10',
         'result': '通过', 'conclusion': '该版本延期测试'},
        {'case_num': '2222' + str(random.randint(100, 600)), 'case_name': '哈哈哈哈', 'env': str(random.randint(20, 50)),
         'env_version': 'xxxxxxx', 'exec_num': '10',
         'result': '通过', 'conclusion': '该版本延期测试'},
        {'case_num': '3333' + str(random.randint(100, 600)), 'case_name': '哈哈哈哈', 'env': str(random.randint(20, 50)),
         'env_version': 'xxxxxxx', 'exec_num': '10',
         'result': '不通过', 'conclusion': '该版本延期测试'},
        {'case_num': '4444' + str(random.randint(100, 600)), 'case_name': '哈哈哈哈', 'env': str(random.randint(20, 50)),
         'env_version': 'xxxxxxx', 'exec_num': '10',
         'result': '通过', 'conclusion': '该版本延期测试'},
        {'case_num': '5555' + str(random.randint(100, 600)), 'case_name': '哈哈哈哈', 'env': str(random.randint(20, 50)),
         'env_version': 'xxxxxxx', 'exec_num': '10',
         'result': '不通过', 'conclusion': '该版本延期测试'},
        {'case_num': '66666' + str(random.randint(100, 600)), 'case_name': '哈哈哈哈', 'env': str(random.randint(20, 50)),
         'env_version': 'xxxxxxx', 'exec_num': '10',
         'result': '通过', 'conclusion': '该版本延期测试'}]

    code = 200
    msg = 'success'
    if request.method == 'POST':
        project_name = request.form['project_name']
        test_date = request.form['test_date']
        if project_name is None or test_date is None:
            code = 500
            msg = "请选择一个项目或者测试日期"

        datas = {
            'series_list': series_list,
            'dataList': dataList,
            'code': code,
            'msg': msg
        }
    return jsonify(datas)


@simple_page.route("/case_data", methods=['POST'])
def case_data():
    if request.method == 'POST':
        project_name = request.form['project_name']
        test_date = request.form['test_date']

        dataList = [
            {'id': 1, 'case_num': 'DSN_EzTS_' + str(random.randint(1, 100)), 'case_name': '申报一批订单', 'exec_num': '10'},
            {'id': 2, 'case_num': 'DSN_EzTS_' + str(random.randint(1, 100)), 'case_name': '哈哈哈哈', 'exec_num': '10'},
            {'id': 3, 'case_num': '3333', 'case_name' + str(random.randint(1, 100)): '哈哈哈哈', 'exec_num': '10'},
            {'id': 4, 'case_num': '4444', 'case_name' + str(random.randint(1, 100)): '哈哈哈哈', 'exec_num': '10'},
            {'id': 5, 'case_num': '5555', 'case_name' + str(random.randint(1, 100)): '哈哈哈哈', 'exec_num': '10'},
            {'id': 6, 'case_num': '6666', 'case_name' + str(random.randint(1, 100)): '哈哈哈哈', 'exec_num': '10'}
        ]
        datas = {
            'dataList': dataList,
            'code': 200,

        }
    return jsonify(datas)


@simple_page.route("/test_data", methods=['POST'])
def test_data():
    if request.method == 'POST':
        project_name = request.form['project_name']
        test_date = request.form['test_date']
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


@simple_page.route("/scene_data", methods=['POST'])
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
