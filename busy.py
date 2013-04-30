import os
import random
import time
import sys
from pygments.style import Style
from pygments.lexers import guess_lexer, guess_lexer_for_filename, get_lexer_by_name, get_lexer_for_filename
from pygments import highlight
from pygments.lexers import PythonLexer, CheetahJavascriptLexer, CoffeeScriptLexer, RubyLexer, SassLexer, HtmlSmartyLexer, ErbLexer
from pygments.formatters import HtmlFormatter, Terminal256Formatter, TerminalFormatter, NullFormatter
from pygments.styles import get_all_styles

files = []
for dirname, dirnames, filenames in os.walk("ENTER YOUR PATH TO FILES HERE."):
    # print path to all subdirectories first.

    #for subdirname in dirnames:
    #    print os.path.join(dirname, subdirname)

    # print path to all filenames.
    for filename in filenames:
        dpath = os.path.join(dirname, filename)
        if dpath.endswith('.rb') or dpath.endswith('.coffee') or dpath.endswith('.sass') or dpath.endswith('.js') or dpath.endswith('.html'):
            files.append(dpath)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.01)

print len(files)
while True:
    fpath = files[random.randint(0, len(files))]
    daf = open(fpath, 'r')

    outputType = None
    lexer = False

    if fpath.endswith('html'):
        lexer_type = HtmlSmartyLexer()

    else:
        lexer = get_lexer_for_filename(fpath)

        if lexer.name == "Erb":
            lexer_type = ErbLexer()

        if lexer.name == "Ruby":
            lexer_type = RubyLexer()

        if lexer.name == "Python":
            lexer_type = PythonLexer()

        if lexer.name == "Sass":
            lexer_type = SassLexer()

        if lexer.name == "CoffeeScript":
            lexer_type = CoffeeScriptLexer()

        if lexer.name == "JavaScript":
            lexer_type = CheetahJavascriptLexer()

    for p in daf.readlines():
        p = p.strip('\n')
        if p != '':
            delay_print(highlight(p, lexer_type, Terminal256Formatter(style='monokai')))


