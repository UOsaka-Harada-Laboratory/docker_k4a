# プロジェクト概要
docker_k4a
Microsoft Azure Kinect (k4a) を用いたロボットビジョンおよび点群処理のためのDocker開発環境プロジェクト。ROS Melodicベースで構築されています。

## 1. ディレクトリ構造とコンテナの対応
本プロジェクトは、カメラドライバおよびSDKを含むDockerコンテナとホストPCのディレクトリマウントで構成されます。
- `dockerfile/k4a` (Dockerfile): Ubuntu 18.04およびROS Melodicをベースに、Azure Kinect Sensor SDK、ROS Driver、およびPython3ラッパーをビルドする環境。
- `./catkin_ws/src/k4a`: ホストマシン側のROSパッケージディレクトリ。コンテナ内の `/catkin_ws/src/k4a` にマウントされ、開発のメインディレクトリとなります。
- `build_wheel_rev.csh`: Python 3からAzure Kinectを扱うための `.whl` パッケージを作成・インストールする補助スクリプト。

## 2. 開発と運用の厳格なルール
### A. デバイスアクセスと表示の制約
- Azure KinectはUSB経由で接続されるため、`docker-compose.yml` において `/dev:/dev` のマウントと `privileged: true` の設定が必須です。
- GUI（`k4aviewer` や `rviz`）を利用するため、コンテナ起動前にホスト側で必ず `xhost +` を実行し、X11フォワーディングを有効化してください。

### B. Python 3とROS Melodicの混在環境
- ROS Melodicの標準はPython 2ですが、本環境では `python3.8` と `pip3` を用いて `open3d` や `opencv-contrib-python` をインストールしています。
- スクリプトを作成・実行する際は、Python 2とPython 3のどちらの環境で動かすべきか（例：`python3 disp_rgbd.py`）を明確に区別してください。

## 3. エージェントのルーティングルール（PMへの指示）
タスクのフェーズに応じて、以下の専門エージェントに的確に委譲してください。
- **アーキテクチャ設計・ビジョン処理パイプライン設計**: `architect` に依頼
- **ROSノード実装・Python3点群処理スクリプトの作成**: `developer` に依頼
- **コンテナビルド・ビューア起動・Launchテスト**: `tester` に依頼
- **カメラ認識エラー・ライブラリリンク（.so）エラーの解消**: `debugger` に依頼