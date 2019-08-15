import csv


def write_position(path, rec_time, lon, lat, alt, satellites_used):
    """
    csvに測位結果を書き込みます．
    :param path: 書き込み先
    :type path: str
    :param rec_time: 測位時刻 YYYYMMDD HH:mm:ss
    :type rec_time: str
    :param lon: 経度 世界測地系 度数
    :type lon: float
    :param lat: 緯度 世界測地系 度数
    :type lat: float
    :param alt: 海抜 メートル
    :type alt: float
    :param satellites_used: 測位衛星番号
    :type satellites_used: list
    """

    # 衛星番号の整形
    satellites_str = '-'.join(satellites_used)

    # 書き込み
    with open(file=path, mode='a') as f:
        writer = csv.writer(f)
        writer.writerow(
            [rec_time, lon, lat, alt, satellites_str]
        )
