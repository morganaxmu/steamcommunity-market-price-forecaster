library(readr)
library(fGarch)
library(rugarch)
library(forecast)
library(tseries)
#载入数据
data <- read_csv("data.csv", col_names = FALSE, 
                 col_types = cols(X1 = col_datetime(format = "%b %d %Y %H")))
data_all <- read_csv("data_all.csv", col_names = FALSE, 
                 col_types = cols(X1 = col_datetime(format = "%b %d %Y %H")))
#先看一眼数据长什么样
plot(data$X1,data$X2, type='l',xlab='time',ylab = 'price')
#开始处理成时间序列数据
pricedata <- ts(data$X2, frequency = 365, start = c(2014,12))
plot.ts(pricedata)
plot.ts(diff(pricedata))
acf(pricedata)
pacf(pricedata)
#运用ARIMA模型
price.forecast = auto.arima(pricedata)
price.forecast
#adf检验,p-value<=0.1,stationary，则继续
adf.test(diff(pricedata))
#预测一下
price.forecast.30 = forecast(pricedata, h=30)
plot(price.forecast.30)
#残差检验，如果黑点均在红线以下，残差显著，继续
lmresult = McLeod.Li.test(y=residuals(price.forecast))
#GARCH，armaorder那边记得填autorima出来的(p,i,q)中的(p,q)
myspec = ugarchspec(variance.model = list(model='sGARCH', 
                                          garchOrder = c(1,1)),
                    mean.model = list(armaOrder = c(5,5), 
                                      include.mean = T),
                    distribution.model = 'std'
)
price.myfit = ugarchfit(myspec, data=diff(pricedata))
acf(residuals(price.myfit))
price.forecast2 = ugarchforecast(price.myfit, n.ahead = 10, data = diff(pricedata[1:(length(pricedata)-10)]))
price.forecast3 = ugarchforecast(price.myfit, data = diff(pricedata))
plot(price.forecast2) #输入1得到图形
plot(price.forecast3) #输入1得到图形
plot(data_all$X1[1814:2533],data_all$X2[1814:2533], type='l',xlab='time',ylab = 'price')