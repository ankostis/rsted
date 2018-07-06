import os
from os.path import join as J
import tempfile
import subprocess
import shutil
import re
import logging

regex_html = re.compile('<html.*</html>', re.DOTALL)

def rst2html(rst_txt):
    if not rst_txt.strip():
        return "<html/>"

    with tempfile.TemporaryDirectory() as tmpdir:
        #tmpdir = '/tmp/t1'
        conf_src = os.path.join(os.path.dirname(__file__), '..', 'sphinx')
        rst_dst = os.path.join(tmpdir, 'sphinx')
        rst_fname = os.path.join(rst_dst, 'index.rst')
        htm_dst = os.path.join(tmpdir, 'html')
        htm_fname = os.path.join(htm_dst, 'index.html')
        cmd_args = "sphinx-build -b singlehtml  sphinx html".split()

        shutil.copytree(conf_src, rst_dst)
        with open(rst_fname, "w", encoding="utf-8") as fout_rst:
            fout_rst.write(rst_txt)

        os.mkdir(htm_dst)
        out = subprocess.check_output(cmd_args, cwd=tmpdir)
        logging.log(logging.INFO, out.decode('utf-8'))

        with open(htm_fname, encoding="utf-8") as fin_html:
            html = fin_html.read()

        m = regex_html.search(html)
        if m:
            return m.group(0)
        return html
