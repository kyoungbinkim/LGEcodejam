  GNU nano 7.2                                           ./LIS.p
from sys import stdin



def sol():
      n = int(stdin.readline())
      nums = list(map(int,stdin.readline().split()))
      ans = 0
      tmp = []

      for num in nums:
            cnt,idx = 0,0

            for (idx, comp) in enumerate(tmp):
                  if comp[0] >= num:
                        break

                  cnt = max(cnt, comp[1])

            if len(tmp) and tmp[-1][0] < num:
                  tmp.append([num, cnt+1])
            elif len(tmp) and tmp[idx][0] == num:
                  tmp[idx] = [num , max(tmp[idx][1], cnt+1)]
            else:
                  tmp.insert(idx, [num, cnt+1])

            ans = max(ans, cnt+1)
            # print(tmp)
      print(ans)

for _ in range(int(stdin.readline())):
      sol()
