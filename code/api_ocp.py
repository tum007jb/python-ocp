import requests
import subprocess

# กำหนดค่า URL ของ OpenShift API
api_url = 'https://your-openshift-api-url'

def login_to_openshift(username, password):
    # กำหนดข้อมูลสำหรับการ Login
    auth_data = {
        'kind': 'PasswordLogin',
        'apiVersion': 'login.openshift.io/v1',
        'metadata': {},
        'spec': {
            'username': username,
            'password': password
        }
    }

    # ทำ HTTP POST request เพื่อ Login เข้าสู่ระบบ OpenShift
    response = requests.post(f'{api_url}/apis/login.openshift.io/v1/tokenreviews', json=auth_data)
    if response.status_code == 200:
        return response.json().get('status', {}).get('token')
    else:
        print('Login failed:', response.text)
        return None

def get_default_project_pods(token):
    try:
        # เรียกใช้คำสั่ง oc เพื่อดึงข้อมูล pod ของ project default
        process = subprocess.Popen(['oc', 'get', 'pods', '-n', 'default', '--output=json', f'--token={token}'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            return stdout
        else:
            print('Error executing oc command:', stderr)
            return None

    except Exception as e:
        print('Error:', e)
        return None

def main():
    username = 'your-openshift-username'
    password = 'your-openshift-password'

    # Login เข้าสู่ระบบ OpenShift และเก็บ token
    token = login_to_openshift(username, password)
    if token:
        print('Login successful. Token:', token)

        # เรียกใช้งานฟังก์ชันเพื่อดึงข้อมูล pod ของ project default
        pod_data = get_default_project_pods(token)

        if pod_data:
            print(pod_data)  # แสดงข้อมูล pod ของ project default
    else:
        print('Login failed.')

if __name__ == '__main__':
    main()
