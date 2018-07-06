import os
import tempfile
import shutil
from .sbprun import run_cmd

def rst2pdf(rst_txt):
    if not rst_txt.strip():
        return "<html/>"

    with tempfile.TemporaryDirectory() as tmpdir:
        conf_src = os.path.join(os.path.dirname(__file__), '..', 'sphinx')
        rst_dst = os.path.join(tmpdir, 'sphinx')
        rst_fname = os.path.join(rst_dst, 'index.rst')
        tex_dst = os.path.join(tmpdir, 'latex')
        tex_fname = os.path.join(tex_dst, 'sphinxed.tex')
        cmd1_args = "sphinx-build -b latex  sphinx latex".split()
        pdf_fname = os.path.join(tex_dst, 'sphinxed.pdf')
        cmd2_args = ["pdflatex", tex_fname]

        shutil.copytree(conf_src, rst_dst)
        with open(rst_fname, "w", encoding="utf-8") as fout_rst:
            fout_rst.write(rst_txt)

        os.mkdir(tex_dst)
        err = run_cmd(cmd1_args, tmpdir)
        if err:
            return err

        err = run_cmd(cmd2_args, tmpdir)
        if err:
            return err

        with open(pdf_fname, 'rb') as fin_pdf:
            pdf = fin_pdf.read()

        return pdf

