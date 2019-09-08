import cv2
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#https://qiita.com/l7u7ch/items/5f8796469322609429ad

import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture("sample.mp4")            # 動画を読み込む
    video_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
    video_fps = cap.get(cv2.CAP_PROP_FPS)           # FPS を取得する
    video_len_sec = video_frame / video_fps         # 長さ（秒）を計算する
    print(video_len_sec)                            # 長さ（秒）を出力する
