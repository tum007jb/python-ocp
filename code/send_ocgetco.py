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
    teams_webhook_url = "https://mfeconcloud.webhook.office.com/webhookb2/2eaf140e-1c4c-4a55-b630-67337eafd809@74105ed9-72ff-4685-9154-75f7408b6f67/IncomingWebhook/890b4931533941af9d9adb974966662b/76686ac9-1a87-4a33-a0e4-ce4f4f0031da"
    message1 = run_oc_get_co_command()
    send_message_to_teams_webhook(teams_webhook_url, message1)
