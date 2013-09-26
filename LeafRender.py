import misaka as m

import houdini as h
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Create a custom renderer
class LeafRenderer(m.HtmlRenderer, m.SmartyPants):
    """
    Define a new 'render'
    """
    def __init__(self, **options):
        super(LeafRenderer, self).__init__()
        # pass additional optionss to HtmlFormatter
        self.options = options
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                h.escape_html(text.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter(**self.options)
        return highlight(text, lexer, formatter)
    def doc_header(self):
        head = """
<html>
<head>
  <meta charset="utf-8">
  <!--[if IE]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
  <link rel="stylesheet" type="text/css" href="all.css">
  <style type="text/css" ></style>
</head>"""
        return head

    def doc_footer(self):
        footer = """
</html>"""
        return footer
