# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1432403990.8276632
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        hidden_categories = context.get('hidden_categories', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        hidden_categories = context.get('hidden_categories', UNDEFINED)
        def content():
            return render_content(context)
        title = context.get('title', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagindex">\n    <header>\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n')
        if cat_items:
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\n')
            __M_writer('        <ul class="postlist">\n')
            for text, link in cat_items:
                if text and text not in hidden_categories:
                    __M_writer('                <li><a class="reference" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('        <ul class="postlist">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('                <li><a class="reference listtitle" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "tags.tmpl", "line_map": {"64": 7, "65": 9, "66": 10, "67": 11, "68": 11, "69": 11, "70": 13, "71": 14, "72": 15, "73": 16, "74": 16, "75": 16, "76": 16, "77": 16, "78": 19, "79": 20, "80": 21, "81": 21, "82": 21, "83": 24, "84": 25, "85": 26, "86": 27, "87": 28, "88": 28, "89": 28, "26": 0, "91": 28, "92": 31, "90": 28, "99": 93, "39": 2, "44": 34, "93": 33, "50": 4, "62": 4, "63": 7}, "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/tags.tmpl"}
__M_END_METADATA
"""
