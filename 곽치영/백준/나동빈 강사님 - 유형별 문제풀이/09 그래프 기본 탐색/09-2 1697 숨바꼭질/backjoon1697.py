def log(string):
    #print(string)
    pass

def solve(N, K, teleport=None, cnt=0):
    if teleport is None:
        # K가 N이하이면 그냥 걸어간다.
        if K <= N:
            steps = N - K
            cnt += steps
            log(f'{cnt:>3}: -{steps}')
            return cnt
        
        # divide by zero를 피하기 위해 N = 0일때 미리 한 걸음 간다.
        if N == 0:
            N += 1
            cnt += 1
            log(f'{cnt:>3}: +{1}')

        # K를 넘어가지 않는 횟수의 텔레포트는 무조건 이득이다.
        min_teleport = (K // N).bit_length() - 1

        return min(solve(N, K, min_teleport, cnt), solve(N, K, min_teleport+1, cnt))
    else:
        log(f'{teleport} teleport case:')

        # 텔레포트 하기 전의 1걸음은 텔레포트 후에는 2**(남은 텔레포트 수)의 크기이다.
        step_size = 1 << teleport
        N <<= teleport

        sign = 1 if K > N else -1
        sign_str = {1: '+', -1:'-'}
        
        # K를 넘어가지 않는 만큼 먼저 걸음하고 시작한다.
        steps_before_teleport = sign * (K-N) // step_size
        N += steps_before_teleport * sign * step_size

        # K까지 남은 거리가 걸음의 3/4이상이면 걸음한다.
        # (+1 x2 x2 -1 = x4 +3), (x2 +1 x2 +1 = x4 +3)이
        # (+1 x2 x2 = x4 +4)의 3/4 지점이고 횟수가 같다.
        if sign * (K-N) > (step_size * 3 / 4):
            steps_before_teleport += 1
            N += sign * step_size
        
        cnt += steps_before_teleport
        log(f'{cnt:>3}: {sign_str[sign]}{steps_before_teleport}')
    
        for _ in range(teleport):
            # 텔레포트한다.
            step_size >>= 1
            cnt += 1
            log(f'{cnt:>3}: x2')
            
            sign = 1 if K > N else -1

            # K까지 남은 거리가 걸음의 3/4이상이면 걸음한다.
            if sign * (K-N) > (step_size * 3 / 4):
                N += sign * step_size
                cnt += 1
                log(f'{cnt:>3}: {sign_str[sign]}{1}')
        
        return cnt

N, K = map(int, input().split())
print(solve(N, K))
