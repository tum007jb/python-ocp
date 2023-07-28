# ใช้ base image ของ Python
FROM python:3.9

# ติดตั้ง openshift และ kubernetes libraries ผ่าน pip
RUN pip install openshift kubernetes

# ทำการคัดลอกโค้ด Python ของคุณไปยังตำแหน่งที่ต้องการใน container
COPY openshift.py /app/openshift.py

# ตั้ง working directory ให้เป็น /app
WORKDIR /app

# รันคำสั่ง Python ของคุณ
CMD ["python", "openshift.py"]