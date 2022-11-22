# 최대공약수는 유클리드 호제법으로 구하고
# 최소공배수는 두 수의 곱/최대공약수의 값으로 구한다
# 유클리드 호제법 = a, b가 주어질 때, (a > b) a b의 최대 공약수는 b와 a%b의 최대공약수와 같다.

a, b = map(int, input().split())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
