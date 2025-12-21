anuary_precipitation = [float(input()) for _ in range(31)]
march_precipitation = [float(input()) for _ in range(31)]
sum_january = sum(january_precipitation)
sum_march = sum(march_precipitation)
print("Больше осадков в январе" if sum_january > sum_march else "Больше осадков в марте") 
