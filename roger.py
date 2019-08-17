import threading
import time
import os

from micropy_gps import micropyGPS
import serial

from output_csv import write_position

gps = micropyGPS.MicropyGPS()  # MicroGPSオブジェクトを生成する。
gps.coord_format = 'dd'


# 引数はタイムゾーンの時差と出力フォーマット

def rungps():  # GPSモジュールを読み、GPSオブジェクトを更新する
    s = serial.Serial('/dev/serial0', 9600, timeout=10)
    s.readline()  # 最初の1行は中途半端なデーターが読めることがあるので、捨てる
    while True:
        sentence = s.readline().decode('utf-8')  # GPSデーターを読み、文字列に変換する
        if sentence[0] != '$':  # 先頭が'$'でなければ捨てる
            continue
        for x in sentence:  # 読んだ文字列を解析してGPSオブジェクトにデーターを追加、更新する
            gps.update(x)


gpsthread = threading.Thread(target=rungps, args=())  # 上の関数を実行するスレッドを生成
gpsthread.daemon = True
gpsthread.start()  # スレッドを起動

# 結果ファイル作成
output_dir = "./data"
os.makedirs(path=output_dir, exist_ok=True)

while True:
    if gps.clean_sentences > 20:  # ちゃんとしたデーターがある程度たまったら出力する
        h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
        print('%2d:%02d:%04.1f' % (h, gps.timestamp[1], gps.timestamp[2]))
        print('緯度経度: %2.8f, %2.8f' % (gps.latitude[0], gps.longitude[0]))
        print('海抜: %f' % gps.altitude)
        print('スピード: %f' % gps.speed[2])
        print('測位利用衛星: %s' % gps.satellites_used)
        print('衛星番号: (仰角, 方位角, SN比)')
        for k, v in gps.satellite_data.items():
            print('%d: %s' % (k, v))
        print('')

        # 時刻の変換
        time_str = (
                '20%02d/%02d/%02d %02d:%02d:%02d' %
                (
                    gps.date[2], gps.date[1], gps.date[0],
                    h, gps.timestamp[1], gps.timestamp[2]
                )
        )

        write_position(
            path="./data/log.csv",
            rec_time=time_str,
            lat=gps.latitude[0],
            lon=gps.longitude[0],
            alt=gps.altitude,
            speed=gps.speed[2],
            satellites_used=gps.satellites_used
        )

    time.sleep(1.0)
