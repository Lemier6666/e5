import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    print("专注时钟已启动！")
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
        print("\r剩余时间: {}".format(time_format), end="")
        time.sleep(1)

    print("\n专注时钟已完成！")

# 设置专注时长为25分钟
focus_timer(25)
