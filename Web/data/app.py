import os,subprocess 
from flask import Flask, render_template, abort, request
from flask_bootstrap import Bootstrap
from subprocess import Popen

app = Flask(__name__)
Bootstrap(app)

@app.route("/manual", methods=["get","post"])
def shell():
    cmd=''
    if request.method=="POST": 
        cmd=request.form.get("cmd")
        #path_to_output_file=request.form.get("path")
        path_to_output_file='/tmp/myoutput.txt'
        try:
            command=cmd.split()

            print(command) # debug
            
            # Saving for report
            myoutput = open(path_to_output_file,'w+')
            p = subprocess.Popen(cmd.split(), stdout=myoutput, stderr=subprocess.PIPE, universal_newlines=True) 
            output, errors = p.communicate()
            
            #pid = p.pid()
            
            t='' # Save output into array 
            # stdout has been written to this file
            with open(path_to_output_file,"r") as f:
                t+=f.read()
                print(f.read())
                out = t.splitlines()
                return render_template("shell.html",cmd=cmd, command=command[0], out=out, path=path_to_output_file)    
            out = t.splitlines()
        except :
            return render_template("error.html",error="No puedo realizar la operación")

        return render_template("shell.html",cmd=cmd, command=command[0], out=out, path=path_to_output_file)    
    else:
        return render_template("shell.html", cmd=cmd)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html",error="Página no encontrada..."), 404

