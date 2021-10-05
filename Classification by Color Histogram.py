import cv2
import numpy as np
import sklearn.neighbors as sn
import os
import tqdm as t

def train():
    feature_train = [];
    label_train = [];
    totalFiles = 0
    lists = ["Apple Braeburn", "Apple Crimson Snow", "Apple Golden 1", "Apple Golden 2",
             "Apple Golden 3", "Apple Granny Smith", "Apple Pink Lady", "Apple Red 1",
             "Apple Red 2", "Apple Red 3", "Apple Granny Smith", "Apple Red Delicious",
             "Apple Red Yellow 1", "Apple Red Yellow 2", "Banana", "Banana Lady Finger",
             "Banana Red", "Orange"]

    for name in lists:
        paths = 'E:/Github/Color-Histogram-by-Python/fruits-360/Training/'+name+'/'
        for bases, dirs, files in os.walk(paths):
            for Files in files:
                totalFiles += 1

        for count in t.tqdm(range(1, totalFiles+1)):
            path = "E:/Github/Color-Histogram-by-Python/fruits-360/Training/%s/%02d.jpg" % (name, count)
            image = cv2.imread(path)
            # แปลงภาพให้อยู่บนปริภูมิสี HSV
            out = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            # แปลงข้อมูลจาก Martrix ให้อยู่ในเรื่องเวกเตอร์เฉพาะ Hue
            out = out[:, :, 0].reshape(1, -1)
            # สร้างฮิสโตแกรมจาก Hue, กำหนด range ของ bin โดยค่าที่ต้องการจะอยู่ใน range นั้นๆ
            hist, bins = np.histogram(out, bins = np.arange(-0.5, 180.5, 1))
            # เนื่องจากตอนแรกเป็นการทำทั้งก้อนของ feature train เราจึงเปลี่ยนวิธี แทนที่จะคิดทั้งห้อน ก็แบ่งออกมาคิดทีละอัน
            # แล้วค่อยนำเข้าไปรวมใน feature train
            train_data = hist/np.sum(hist)
            label_train.append("Apple Braeburn")
            train_data = np.array(train_data)
            train_data = np.reshape(train_data, (-1, 180))
            feature_train.append(*train_data)
            label_train.append(name)
        totalFiles = 0
    print(np.shape(feature_train))
    password = input()
    if password == "1":
        keepintofolder(feature_train, label_train)
train()
