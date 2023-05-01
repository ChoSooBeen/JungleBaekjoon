import sys

N, K = map(int, sys.stdin.readline().split())
elec = list(map(int, sys.stdin.readline().split()))

plug = []
count = 0

for i in range(K) :
    if elec[i] in plug : # 이미 꽂여있을 경우
        continue
    elif len(plug) < N : # 꽂여있지 않고 멀티탭 사용 가능할 때
        plug.append(elec[i])
    else : # 꽂여있지 않고 멀티탭도 다 사용중일 때
        flag = True # 현재 플러그에 꽂여있는 모든 것들이 다음에 사용된다 = True
        for p in plug :
            # 현재 플러그에 꽂여있는 것이 다음에 사용될 일이 없으면 뽑는다.
            if p not in elec[i:] :
                plug.remove(p)
                count += 1
                plug.append(elec[i])
                flag = False
                break
        # 만약 플러그에 꽂인 모든 번호가 나중에 다 사용하는 것이라면
        if flag :
            last = 0 # 플러그에 있는 것 중 가장 나중에 사용될 번호의 인덱스
            for p in plug :
                tmp = elec[i:].index(p)
                if tmp > last :
                    last = tmp
            # elec[i:]를 기준으로 인덱스를 찾았기에 elec에 접근할 때 last+i 로 접근한다.
            plug.remove(elec[i+last])
            count += 1
            plug.append(elec[i])
                 
print(count)