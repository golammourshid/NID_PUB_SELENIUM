import redis
import time

r = []


def redis_config():
    global r
    r.append(redis.Redis(host='192.168.5.223', port=6379))
    r.append(redis.Redis(host='192.168.5.223', port=6380))
    r.append(redis.Redis(host='192.168.5.223', port=6381))
    r.append(redis.Redis(host='192.168.5.224', port=6379))
    r.append(redis.Redis(host='192.168.5.224', port=6380))
    r.append(redis.Redis(host='192.168.5.224', port=6381))
    r.append(redis.Redis(host='192.168.5.225', port=6379))
    r.append(redis.Redis(host='192.168.5.225', port=6380))
    r.append(redis.Redis(host='192.168.5.225', port=6381))

# re = redis.Redis(host='redis-mig', port=6379)
# redis_config()
# length = r.llen("appointment-station:nrb:stationId:242:NEW_VOTER:2023-05-20:count")

# with open("out.txt", "w") as file:
#     for i in range(0, length):
#         strr = str(re.lindex("redis-migration-test", i))
#         strr = strr[2:(len(strr) - 1)]
#         file.write(strr + '\n')


def get_count_value():
    for i in range(9):
        try:
            length = r[i].llen("appointment-station:nrb:stationId:242:NEW_VOTER:2023-05-20")
            for i in range(0, length):
                strr = str(r[i].lindex("appointment-station:nrb:stationId:242:NEW_VOTER:2023-05-20", i))
                strr = strr[2:(len(strr) - 1)]
                print(strr)
        except:
            pass



redis_config()

get_count_value()

# with open("out.txt", "r") as file:
#     for strr in file:
#         strr = strr.strip()
#         flag = 0
#         init_val()
#         for ch in strr:
#             if ch == 'N' or ch == 'U' or ch == 'L':
#                 continue
#             if ch == '#':
#                 flag += 1
#                 continue
#             if flag == 0:
#                 said += ch
#             elif flag == 1:
#                 voter_no += ch
#             elif flag == 2:
#                 pin += ch
#             elif flag == 3:
#                 nid += ch
#
#         print(strr)
#
#         if len(nid) > 5:
#             del_nid10_value()
#         if len(pin) > 5:
#             del_nid17_value()
#         if len(voter_no) > 5:
#             del_voter_no_value()
#
# request_time = time.perf_counter() - start
# print("total time takes: " + str(request_time/60) + "Minutes")