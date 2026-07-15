from cmath import sqrt
import time

# 全局變數
On = True
Running = False
sensor = 0.0
idle = False
idle_time = 0
idle_times = 0
cargo = 0
avg_production = 0
power = 0.0
init_time = time.time()
start_time = time.time() 
end_time = time.time() 
Voltage = 0.0
current = 0.0
powersec = 0.0
kwh = 0.0
wh_per_bag = 0.0

# 存儲數據的字典
data = {
    'On': On,
    'Running': Running,
    'sensor': sensor,
    'idle': idle,
    'idle_time': idle_time,
    'idle_times': idle_times,
    'cargo': cargo,
    'avg_production': avg_production,
    'power': power,
    'Voltage': Voltage,
    'current': current,
    'powersec': powersec,
    'kwh': kwh,
    'wh_per_bag': wh_per_bag
}
while On:
    #refresh voltage、current and display
    powersec = Voltage * current
    power += powersec
    if  sensor == 0.0:
        end_time = time.time() 
        Running = False
    if sensor >=5.0:
        Running = True
    avg_production = cargo / (time.time() - init_time)
    while(end_time - start_time >= 300): #預設5分
        idle = True
        if Running == True:
            idle = False
            #display idle_time、start_time、end_time
            idle_time = 0
            idle_times += 1
            start_time = time.time() 
            end_time = time.time()
    if On == False:
        kwh = power / (time.time() - init_time) * 3600
        wh_per_bag = kwh / cargo if cargo > 0 else 0
        break
        

