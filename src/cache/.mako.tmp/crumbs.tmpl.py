# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1432409615.8966093
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/crumbs.tmpl'
_template_uri = 'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if crumbs:
            __M_writer('<nav class="breadcrumbs">\n<ul class="breadcrumb">\n')
            for link, text in crumbs:
                if text != index_file:
                    if link == '#':
                        __M_writer('                <li>')
                        __M_writer(str(text))
                        __M_writer('</li>\n')
                    else:
                        __M_writer('                <li><a href="')
                        __M_writer(str(link))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
            __M_writer('</ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "crumbs.tmpl", "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/crumbs.tmpl", "line_map": {"32": 3, "33": 4, "34": 5, "35": 7, "36": 8, "37": 9, "38": 10, "39": 10, "40": 10, "41": 11, "42": 12, "43": 12, "44": 12, "45": 12, "46": 12, "15": 0, "47": 16, "20": 2, "21": 19, "27": 3, "53": 47}}
__M_END_METADATA
"""
