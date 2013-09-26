import io
import misaka as m
from LeafRender import LeafRenderer

def md2html(infile, outfile=None, **options):
    """
    Render md to html.
    infile: The input md file name
    outfile: The output html file name
    options: Additional options to HtmlFormatter function in LeafRenderer
    usage: md2html("template.md",linenos="inline")
           md2html("template.md",linenos="table")
    """
    leafRender = LeafRenderer(**options)
    md = m.Markdown(leafRender, 
                    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS | m.EXT_TABLES)
    if outfile is None:
        outfile = infile.split('.')[0] + '.html'
    with io.open(outfile, 'w') as outfile:
        with io.open(infile, 'r') as infile:
            outfile.write(md.render(infile.read()))
