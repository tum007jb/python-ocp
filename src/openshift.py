from openshift.dynamic import DynamicClient
from kubernetes import config

def get_default_project_pods():
    try:
        # เชื่อมต่อกับ Kubernetes API server ในรูปแบบ InCluster
        config.load_incluster_config()
        openshift_client = DynamicClient()

        # เรียกใช้ API เพื่อดึงข้อมูล pod ของ project default
        pods = openshift_client.resources.get(api_version='v1', kind='Pod').get(namespace='demo')
        return pods.to_dict()

    except Exception as e:
        print('Error:', e)
        return None

def main():
    # เรียกใช้งานฟังก์ชันเพื่อดึงข้อมูล pod ของ project default
    pod_data = get_default_project_pods()

    if pod_data:
        print(pod_data)  # แสดงข้อมูล pod ของ project default

if __name__ == '__main__':
    main()
