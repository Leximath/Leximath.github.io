# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1432409615.8817596
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/comments_helper_googleplus.tmpl'
_template_uri = 'comments_helper_googleplus.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_form', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<div class="g-commentcount" data-href="')
        __M_writer(str(link))
        __M_writer('"></div>\n<script src="https://apis.google.com/js/plusone.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<script src="https://apis.google.com/js/plusone.js"></script>\n<div class="g-comments"\n    data-href="')
        __M_writer(str(url))
        __M_writer('"\n    data-first_party_property="BLOGGER"\n    data-view_type="FILTERED_POSTMOD">\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "comments_helper_googleplus.tmpl", "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/comments_helper_googleplus.tmpl", "line_map": {"32": 11, "33": 12, "34": 12, "40": 2, "44": 2, "45": 5, "46": 5, "15": 0, "20": 9, "21": 14, "22": 17, "56": 16, "52": 16, "28": 11, "62": 56}}
__M_END_METADATA
"""
