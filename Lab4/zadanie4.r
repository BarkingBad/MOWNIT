setwd("/home/andrzej/Dokumenty/Mownit/Lab4")

results = read.csv("csv.csv", sep=";")

avg_results = aggregate( TIME ~ N:TYPE, data=results, FUN=mean)
avg_results$sd = aggregate( TIME ~ N:TYPE, data=results, FUN=sd)$TIME

naive_r = avg_results[avg_results$TYPE == 'naive',]
better_r = avg_results[avg_results$TYPE == 'better',]
blas_r = avg_results[avg_results$TYPE == 'blas',]

fit1 = lm(naive_r$TIME ~ poly(naive_r$N, 3, raw=TRUE), data=data.frame(naive_r$N, naive_r$TIME))
fit2= lm(better_r $TIME ~ poly(better_r $N, 3, raw=TRUE), data=data.frame(better_r $N, better_r $TIME))
fit3= lm(blas_r$TIME ~ poly(blas_r$N, 3, raw=TRUE), data=data.frame(blas_r$N, blas_r$TIME))

ggplot(avg_results, aes(N,TIME,color=TYPE)) + 
  geom_point() + 
  geom_errorbar(aes(ymin = TIME - sd, ymax = TIME + sd, width=5)) +
  geom_line(data=naive_r, aes(naive_r$N, predict(fit1, naive_r))) +
  geom_line(data=better_r, aes(better_r$N, predict(fit2, better_r))) +
  geom_line(data=blas_r, aes(blas_r$N, predict(fit3, blas_r)))  +
  xlab("N [size of matrix]") +
  ylab("Time [ms]")

