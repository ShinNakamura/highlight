# -*- coding: utf-8 -*-
# SRC(download from Wordpress, part of HTML)
# KWS(keywords, separated by LF)
# Find kw in src, and highlight kw.
# OUTPUT is HTML

import sys
from functools import reduce
import html

def readfile_as_list(fname):
    '''
    just read a file. return lines as list.
    '''
    with open(fname, "rt", encoding="utf-8") as f:
        for line in f:
            yield line

def readfile(fname):
    '''
    just read a file. one file -> one string
    '''
    return "".join(readfile_as_list(fname))

def highlight_kw(src, kw):
    return src.replace(kw, '<span class="highlight">{}</span>'.format(kw))

def main():
    _, output_template_fname, src_fname, kws_fname = sys.argv

    output_template = readfile(output_template_fname)
    src = html.escape(readfile(src_fname)).replace("\n", "<br />")
    kws = (html.escape(kw) for kw in (kw.strip() for kw in readfile_as_list(kws_fname)) if kw)
    dst = reduce(highlight_kw, kws, src)

    # title and article -- as place holder -- are in OUTPUT template.
    output_template = output_template.format(title="src:{} <- kws:{}".format(src_fname, kws_fname), article=dst)

    print(output_template)

if __name__=='__main__':
    main()

