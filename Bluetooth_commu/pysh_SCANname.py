import os
import subprocess

def run_cmd2file(cmd):
    fout = open("cmd_out.log",'w')
    #fout = open("cmd_out_bltctl.log",'w')
    ferr = open("cmd_err.log",'a')
    # a for append, w for overwrite
    cmd_outf = subprocess.Popen(cmd, stdout=fout, stderr=ferr, shell=True)
    if cmd_outf.poll():
        return
    cmd_outf.wait()
    return

#run_cmd2file('bluetoothctl scan on')
run_cmd2file('hcitool scan')
