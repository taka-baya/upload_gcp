import os
import cv2
import numpy
import imutils
from google.cloud import storage
import time

class upload_gcs(object):
    """docstring for file_treatment"""
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket('my_first_test')
    
    def upload_imagefile(self, filename, folder_path):
        blob = self.bucket.blob(filename)
        blob.upload_from_filename(folder_path+"/"+filename)

def capture_camera(base_image_path, save_image_name, save_image_path, mirror=False, size=None):
    u_gcs = upload_gcs()
    
    # 背景となる画像
    base_image = cv2.imread(base_image_path)
    print(base_image.shape) #720 ,1280

    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    # 時間計測開始
    time_start = time.time()

    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        frame = cv2.resize(frame, (base_image.shape[1],base_image.shape[0]))
        blurred_img = cv2.blur(frame,ksize=(3,3))
        frame_edge = cv2.Canny(blurred_img, 100, 50)
        backtorgb = cv2.cvtColor(frame_edge,cv2.COLOR_GRAY2RGB)

        blended = cv2.addWeighted(src1=base_image,alpha=0.8,src2=backtorgb,beta=1.9,gamma=0)

        if (time.time() - time_start) > 5:
            cv2.imwrite(save_image_path + "/" + save_image_name,blended)
            u_gcs.upload_imagefile(save_image_name,save_image_path)
            time_start = time.time()

        # フレームを表示する
        cv2.imshow('camera capture', blended)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    base_image_path = "../image/camera_capture_0.jpg"
    save_image_name = "edge_image.jpg"
    save_image_path = "../image"
    capture_camera(base_image_path,save_image_name,save_image_path)
