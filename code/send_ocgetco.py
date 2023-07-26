import requests
import subprocess

def run_oc_get_co_command():
    try:
        # รันคำสั่ง "oc get co" บนระบบปฏิบัติการและรับผลลัพธ์
        process = subprocess.Popen(['oc', 'get', 'co'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            message1 = stdout.strip()
            return message1
        else:
            print(f"Have a Error to run command: {stderr}")
            return None

    except Exception as e:
        print(f"Have a Error: {e}")
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
            print(f"Have a Error to send message: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"Have a Error: {e}")

if __name__ == "__main__":
    # แทนที่ webhook_url ด้วย URL ของ Microsoft Teams webhook ที่คุณได้รับมา
    teams_webhook_url = ""
    message1 = run_oc_get_co_command()
    send_message_to_teams_webhook(teams_webhook_url, message1)
