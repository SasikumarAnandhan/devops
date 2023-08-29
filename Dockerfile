#FROM emindsguardians/ubuntu-python37-octave-basepack:v3

#Docker Image with nano editor and requirements.txt
FROM emindsguardians/ubuntu18-python37-octave-req-basepack:v2

WORKDIR /home/eminds
#multiprocess/em-dt-backend/FenceGraph/SG_Fence_Core/

ADD em-dt-backend /home/eminds/em-dt-backend


# Install FastAPI and other dependencies
#RUN pip install -r /home/eminds/em-dt-backend/requirements.txt


# Expose ports for FastAPI (8666) and MLflow (5000)


ENV TZ=Asia/Kolkata

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata


WORKDIR /home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core
ADD main.py /home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core/main.py
ADD s3_filedownload_trash.py /home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core/s3_filedownload_trash.py
RUN mkdir CSV_s3
RUN sed -i 's#/Users/geet/Documents/DigitalTwin/Github/MVP1.5/em-dt-backend/FenceGraph/SG_Fence_Core/StatsEngine/model/bearing_failure_prediction.pkl#/home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core/StatsEngine/model/bearing_failure_prediction.pkl#g' /home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core/StatsEngine/statsengineclass.py
ENTRYPOINT ["python3.7", "main.py"]
