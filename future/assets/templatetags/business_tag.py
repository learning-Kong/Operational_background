# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

import ast
from django import template
register = template.Library()

@register.filter(name='str_to_list')
def str_to_list(info):
    return ast.literal_eval(info)

