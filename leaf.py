import misaka as m
import io

import houdini as h
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Create a custom renderer
class BleepRenderer(m.HtmlRenderer, m.SmartyPants):
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                h.escape_html(text.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
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

# And use the renderer
renderer = BleepRenderer()
md = m.Markdown(renderer,
    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS | m.EXT_TABLES )

with io.open('out.html', 'w') as file:
    with io.open('template.md', 'r') as file1:
        file.write(md.render(file1.read()))
