# -*- coding: utf-8 -*-
# SRC(download from Wordpress, part of HTML)
# KWS(keywords, separated by LF)
# Find kw in src, and highlight kw.
# OUTPUT is HTML

import sys
from functools import reduce

def readfile(fname):
    '''
    just read file. one file -> one string
    '''
    with open(fname, "rt", encoding="utf-8") as f:
        return "".join([line for line in f])

def escape_html(html):
    '''
    escape html tag
    '''
    return html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def highlight_kw(src, kw):
    return src.replace(kw, '<span class="highlight">{}</span>'.format(kw))

def main():
    _, output_template_fname, src_fname, kws_fname = sys.argv

    output_template = readfile(output_template_fname)
    src = escape_html(readfile(src_fname)).replace("\n", "<br />")
    kws = (escape_html(kw) for kw in (kw.strip() for kw in readfile(kws_fname).split("\n")) if kw)
    dst = reduce(highlight_kw, kws, src)

    # title and article -- as place holder -- are in OUTPUT template.
    output_template = output_template.format(title="src:{} <- kws:{}".format(src_fname, kws_fname), article=dst)

    print(output_template)

if __name__=='__main__':
    main()

