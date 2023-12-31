import subprocess
import requests

def run_linux_command_and_get_columns(command):
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

def send_message_to_teams_webhook(webhook_url, message):
    try:
        data = {
            "text": message
        }

        response = requests.post(webhook_url, json=data)

        if response.status_code == 200:
            print("Send Message to Microsoft Teams Complete")
        else:
            print(f"Have a Error: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"Have a Error: {e}")

if __name__ == "__main__":
    # แทนที่ command ด้วยคำสั่ง Linux ที่คุณต้องการรัน
    linux_command = "oc get co"
    teams_webhook_url = ""
    result = run_linux_command_and_get_columns(linux_command)
    if result is not None:
        message_summary = "<h1>Summary Operator OCP DSO</h1>"
        message_summary += "<table border=\"0\">"
        for col1, col3, col4, col5 in result:
            if col3 == "True":
                message_summary += f"<tr><td> {col1} </td><td style=\"color:green;\">{col3}</td><td style=\"color:green;\">{col4}</td><td style=\"color:green;\">{col5}</td></tr>"
            else:
                message_summary += f"<tr><td> {col1} </td><td style=\"color:red;\">{col3}</td></td><td style=\"color:red;\">{col4}</td></td><td style=\"color:red;\">{col5}</td></tr>"
        message_summary += "</table>"
        send_message_to_teams_webhook(teams_webhook_url, message_summary)
        #print(message_summary)
    #if result is not None:
    #    print("ผลลัพธ์:")
    #    for col1, col3 in result:
    #        print(f"คอลัมน์ที่ 1: {col1}, คอลัมน์ที่ 3: {col3}")
