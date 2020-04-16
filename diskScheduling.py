from heapq import *
from handleFile import *


def SSTF(hp, reqs):
    requests = reqs.copy()
    time = 0
    position = hp
    heap = []
    distance = []
    distance.append(hp)
    while len(requests) > 0:
        for r in requests:
            heappush(heap, (abs(position-r), r))
        x = heappop(heap)[1]
        time += abs(position-x)
        position = x
        distance.append(x)
        requests.remove(x)
        heap = []

    # calculate average seek time
    save('total', time, 'distance', distance)


def SCAN(hp, reqs):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = 200
    start = 0
    distance = []
    distance.append(hp)
    for i in range(pos, end+1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)

    time += abs(pos-end)
    pos = end
    for i in range(end, start-1, -1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)

    save('total', time, 'distance', distance)


def FCFS(hp, requests):
    time = 0
    pos = hp
    distance = []
    distance.append(hp)
    for request in requests:
        time += abs(request-pos)
        pos = request
        distance.append(pos)

    # calculate average seek time
    save('total', time, 'distance', distance)


def C_SCAN(hp, reqs):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = 200
    start = 0
    distance = []
    distance.append(hp)
    # seek from curr_pos to end which is 200
    for i in range(pos, end+1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)
    time += abs(pos-end)
    pos = end
    # seek to hp from start
    for i in range(start, hp+1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)

    # calculate average seek time
    save('total', time, 'distance', distance)


def LOOK(hp, reqs):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = max(requests)
    start = min(requests)
    distance = []
    distance.append(hp)
    # seek from curr_pos to end which is 200
    for i in range(pos, end+1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)

    # seek back to start
    for i in range(end, start-1, -1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)
    # calculate average seek time
    save('total', time, 'distance', distance)


def C_LOOK(hp, reqs):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = max(requests)
    start = min(requests)
    distance = []
    distance.append(hp)
    # seek from curr_pos to max of list
    for i in range(pos, end+1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)

    time += abs(pos-start)
    pos = start
    # seek to hp from start
    for i in range(start, hp+1):
        if i in requests:
            time += abs(pos-i)
            pos = i
            distance.append(i)
            requests.remove(i)

    # calculate average seek time
    save('total', time, 'distance', distance)
