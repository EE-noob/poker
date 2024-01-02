from calculate_probability import calu_prob
import time

# 记录程序开始时间
start_time = time.time()

# 运行您的程序代码
# ...
[win_probability,splitPot_probability]=calu_prob(["As","9c"],5,int(1e6))

# 记录程序结束时间
end_time = time.time()

# 计算运行时间
execution_time = end_time - start_time

# 输出运行时间
print("程序执行时间：", execution_time/60, "min")

