clc
clear
clf


data = csvread('D:\prihodko\RT-11M\data.csv');

data = data(1:end-1,:);

ind = data(:,1)+ 1j*data(:,2);


gamma = z2gamma(ind,50);

smithplot(gamma,'*');
