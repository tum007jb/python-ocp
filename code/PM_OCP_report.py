import subprocess
import requests
from datetime import datetime

def run_linux_command_ocadm(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            lines = stdout.strip().split('\n')
            result = []
            for line in lines:
                columns = line.split()
                if len(columns) >= 5:
                    col1 = columns[0]
                    col2 = columns[1]
                    col3 = columns[2]
                    col4 = columns[3]
                    col5 = columns[4]
                    result.append((col1, col2, col3, col4, col5 ))
            return result
        else:
            print(f"เกิดข้อผิดพลาดในการรันคำสั่ง: {stderr}")
            return None

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None

def reportadm(result):
    if result is not None:
        message_summary = '<figure class="text-center"><blockquote class="blockquote"><h3>Summary Performance OCP</h3></blockquote></figure>'
        message_summary += '<div class="container d-flex justify-content-center align-items-center"><table class="table table-sm text-center">'
        for col1, col2, col3, col4, col5 in result[0:1]:
                message_summary += f"<thead><tr><td> {col1} <td>{col2} </td><td>{col3}</td><td>{col4}</td><td>{col5}</td></tr></thead><tbody>"
        for col1, col2, col3, col4, col5 in result[1:]:
                message_summary += f"<tr><td> {col1} <td>{col2} </td><td>{col3}</td><td>{col4}</td><td>{col5}</td></tr>"
        message_summary += "</tbody></table></div>"
        return message_summary

def run_linux_command_ocgetco(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            lines = stdout.strip().split('\n')
            result = []
            for line in lines:
                columns = line.split()
                if len(columns) >= 3:
                    col1 = columns[0]
                    col3 = columns[2]
                    col4 = columns[3]
                    col5 = columns[4]
                    result.append((col1, col3, col4, col5 ))
            return result
        else:
            print(f"เกิดข้อผิดพลาดในการรันคำสั่ง: {stderr}")
            return None

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None
def reportco(result):
   if result is not None:
        message_summary = '<figure class="text-center"><blockquote class="blockquote"><h3>Summary Operator</h3></blockquote></figure>'
        message_summary += '<div class="container d-flex justify-content-center align-items-center"><table class="table table-sm text-center">'
        for col1, col3, col4, col5 in result[0:1]:
                message_summary += f"<thead><tr><td> {col1} <td>{col3}</td><td>{col4}</td><td>{col5}</td></tr></thead><tbody>"
        for col1, col3, col4, col5 in result[1:]:
            if col3 == "True":
                message_summary += f"<tr><td> {col1} </td><td style=\"color:green;\">{col3}</td><td style=\"color:green;\">{col4}</td><td style=\"color:green;\">{col5}</td></tr>"
            else:
                message_summary += f"<tr><td> {col1} </td><td style=\"color:red;\">{col3}</td></td><td style=\"color:red;\">{col4}</td></td><td style=\"color:red;\">{col5}</td></tr>"
        message_summary += "</tbody></table></div>"
        return message_summary

def run_linux_command_ocgetpo(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            lines = stdout.strip().split('\n')
            result = []
            for line in lines:
                columns = line.split()
                if len(columns) >= 5:
                    col1 = columns[0]
                    col2 = columns[1]
                    col3 = columns[2]
                    col4 = columns[3]
                    col5 = columns[4]
                    result.append((col1, col2, col3, col4, col5 ))
            return result
        else:
            print(f"เกิดข้อผิดพลาดในการรันคำสั่ง: {stderr}")
            return None

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None

def reportpod(result,subject):
    if result is not None:
        message_summary = f'<figure class="text-center"><blockquote class="blockquote"><h3>Summary Pod {subject} </h3></blockquote></figure>'
        message_summary += '<div class="container d-flex justify-content-center align-items-center"><table class="table table-sm text-center">'
        for col1, col2, col3, col4, col5 in result[0:1]:
                message_summary += f"<thead><tr><td> {col1} <td>{col2} </td><td>{col3}</td><td>{col4}</td><td>{col5}</td></tr></thead><tbody>"
        for col1, col2, col3, col4, col5 in result[1:]:
                message_summary += f"<tr><td> {col1} <td>{col2} </td><td>{col3}</td><td>{col4}</td><td>{col5}</td></tr>"
        message_summary += "</tbody></table></div>"
        return message_summary

def run_linux_command_ocgetcluster(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            lines = stdout.strip().split('\n')
            result = []
            for line in lines:
                columns = line.split()
                if len(columns) >= 5:
                    col1 = columns[0]
                    col2 = columns[1]
                    col3 = columns[2]
                    col4 = columns[3]
                    col5 = columns[4]
                    col6 = columns[5]
                    result.append((col1, col2, col3, col4, col5, col6))
            return result
        else:
            print(f"เกิดข้อผิดพลาดในการรันคำสั่ง: {stderr}")
            return None

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None

def reportocgetcluster(result,subject):
    if result is not None:
        message_summary = f'<figure class="text-center"><blockquote class="blockquote"><h3>Summary Pod {subject} </h3></blockquote></figure>'
        message_summary += '<div class="container d-flex justify-content-center align-items-center"><table class="table table-sm text-center">'
        for col1, col2, col3, col4, col5, col6 in result[0:1]:
                message_summary += f"<thead><tr><td> {col1} <td>{col2} </td><td>{col3}</td><td>{col4}</td><td>{col5}</td><td>{col6}</td></tr></thead><tbody>"
        for col1, col2, col3, col4, col5, col6 in result[1:]:
                message_summary += f"<tr><td> {col1} <td>{col2} </td><td>{col3}</td><td>{col4}</td><td>{col5}</td><td>{col6}</td></tr>"
        message_summary += "</tbody></table></div>"
        return message_summary


if __name__ == "__main__":
    webintro = ""
    webintro = '<html><head><title>PM Report </title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"></head><body><figure class="text-center"><blockquote class="blockquote"><h1>PM Report Openshift</h1></blockquote><figcaption class="blockquote-footer">By MFEC Infosec Team</figcaption></figure>'
    webfoot = "</body></html>"
       # Get OC get clusterversion
    linux_command = "oc get clusterversion"
    result = run_linux_command_ocgetcluster(linux_command)
    table0 = reportocgetcluster(result,"Cluster Version OCP")
     # Get OC get co
    linux_command = "oc get co"
    result = run_linux_command_ocgetco(linux_command)
    table1 = reportco(result)
    # get OC adm top node
    linux_command = "oc adm top node"
    result = run_linux_command_ocadm(linux_command)
    table2 = reportadm(result)
    # get OC get node
    linux_command = "oc get no"
    result = run_linux_command_ocadm(linux_command)
    table3 = reportadm(result)
     # get pod dns
    linux_command = "oc get po -n openshift-dns"
    result = run_linux_command_ocgetpo(linux_command)
    table4 = reportpod(result,"OpenShift-DNS")

     # get pod console
    linux_command = "oc get po -n openshift-console"
    result = run_linux_command_ocgetpo(linux_command)
    table5 = reportpod(result,"OpenShift-Web Console")

     # get pod monitor
    linux_command = "oc get po -n openshift-monitoring"
    result = run_linux_command_ocgetpo(linux_command)
    table6 = reportpod(result,"OpenShift-Monitor")

     # get pod ingress
    linux_command = "oc get po -n openshift-ingress"
    result = run_linux_command_ocgetpo(linux_command)
    table7 = reportpod(result,"OpenShift-Ingress")
    
    fullweb = f"{webintro}{table0}{table1}{table2}{table3}{table4}{table5}{table6}{table7}{webfoot}"
    
    #Create file html 
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    file_name = f"result_{date_string}.html"

    file_path = "/var/www/html/" + file_name

    with open(file_path, "w") as file:
            file.write(fullweb)