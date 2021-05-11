from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

# class EmployeesConfig(AppConfig):
#     name = 'employees'
#     verbose_name = '人员管理'


class SuitConfig(DjangoSuitConfig):
    # name = 'employees'
    menu = (
        ParentItem('人员信息超级管理', children=[
            ChildItem(model='employees.activity'),
            # ChildItem(model='employees.employee'),
            ChildItem(model='employees.comment'),
            ChildItem(model='employees.trainingexperience'),
            ChildItem(model='employees.resume'),
            ChildItem(model='employees.workexperience'),
            ChildItem(model='employees.skill'),
            ChildItem(model='employees.education'),
            ChildItem(model='employees.contactperson'),
            ChildItem(model='employees.certification'),
            ChildItem(model='employees.idcard'),
            ChildItem(model='employees.card'),
            # ChildItem(model='employees.interview'),
            ChildItem(model='employees.project')
        ]),
        ParentItem('面试管理', children=[
            ChildItem(model='employees.interviewresume'),
            ChildItem(model='employees.interview')
        ], icon='fa fa-leaf'),
        ParentItem('员工管理', children=[
            ChildItem(model='employees.employee')
        ]),
        ParentItem('项目管理', children=[
            ChildItem(model='employees.workproject')
        ]),
        ParentItem('工资管理', children=[
            ChildItem(model='employees.salary')
        ]),
        ParentItem('人员报表', children=[
            ChildItem(model='employees.dailyreport')
        ]),
        ParentItem('技术分享', children=[
            ChildItem(model='employees.regularmeeting')
        ]),
        ParentItem('用户与权限', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group'),
        ], icon='fa fa-users'),
    )
    # verbose_name = 'test'

