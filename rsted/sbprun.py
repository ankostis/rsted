import subprocess as sbp
import logging


def run_cmd(cmd, cwd):
    ret = sbp.run(cmd, cwd=cwd, stdout=sbp.PIPE, stderr=sbp.PIPE)
    msg = ("Cmd '%s' failed with %s:\n  STDOUT: %s\n  STDERR: %s" %
           (cmd, ret.returncode, ret.stdout, ret.stderr))
    if ret.returncode:
        return  msg
    else:
        logging.error(msg, stack_info=1)

