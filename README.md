# new-poem-generator

[15頁摘要v5](https://drive.google.com/file/d/17Q4Rq46o7qnyBht64y-QnraML8GGGDFj/view?usp=sharing)

[PPT](https://docs.google.com/presentation/d/1CRAjdlRe8n6JyQ4XPb9DHLlmWf2W-PpJ/edit?usp=sharing&ouid=100785420763067455802&rtpof=true&sd=true)

[模型權重 (大檔案，請注意你的流量，下載後請解壓縮到 GPT2 資料夾)](https://drive.google.com/file/d/1PQOpLjhOw38Jpxe8QjBa5RsxkK2IN3YL/view?usp=sharing)

# 環境架設 使用docker

## 0. 安裝WSL2

**顯卡裝驅動**

## 1. 安裝WSL2並確認WSL吃不吃的到顯卡

在系統管理員 PowerShell 或 Windows 命令提示字元中輸入此命令，然後重新開機電腦，並設定WSL

[問題參考](https://docs.microsoft.com/zh-tw/windows/wsl/install)
```
wsl --install
```
確認WSL吃不吃的到顯卡，請輸入以下指令

```
nvidia-smi
```
應顯示 (沒顯示代表顯卡驅動有問題，請LINE我)
```
Sun Mar 27 20:07:05 2022
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 510.60.02    Driver Version: 512.15       CUDA Version: 11.6     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:9E:00.0  On |                  N/A |
|  0%   47C    P8    11W / 215W |    329MiB /  8192MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

## 2. 安裝Docker
設定好WSL後，將Docker裝在WSL裡面，執行以下指令
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo service docker start
sudo docker run hello-world
```
應顯示 (沒顯示一樣請LINE我)
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## 3. 安裝NV Docker

Docker不能直接call GPU，所以要裝這個補丁，輸入以下指令
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo apt-key add - \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo service docker restart
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```
應顯示 (沒顯示一樣請LINE我)
```
Sun Mar 27 13:16:44 2022
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 510.60.02    Driver Version: 512.15       CUDA Version: 11.6     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:9E:00.0  On |                  N/A |
|  0%   47C    P8    12W / 215W |    330MiB /  8192MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
## 4. 拉鏡像and依賴套件安裝

pull image and run 

--rm 容器終止後刪除容器鏡像

-p 8888:8889 將主機的 8888 port 映射到容器的 8889 port

-v /home/uuu/pj:/workspace/pj 將主機的 /home/uuu/pj資料夾 掛到容器的 /workspace/pj位置

拉動的鏡像位置與名稱:
nvcr.io/nvidia/pytorch:22.02-py3

```
sudo docker run --gpus all -it --rm -p 8888:8888 -v /home/uuu/pj:/workspace/pj nvcr.io/nvidia/pytorch:22.02-py3
```

依賴套件安裝
```
!pip install zhon
!pip install opencc
!pip install Flask-Cors
!pip install transformers
!pip install sentencepiece
```