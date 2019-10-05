clear;
clc;
close all;

% initialize variable
% heat co-efficents
h = 0.3143;K = 0.4246;

% geometric variables
L = 0.8;A_c = 1.6;
P = 5.6;

% electronic params
I = 6; %A
R = 1.557; 

T_h = 25;% initial temp
Q_h = 56.0472;%heat

% other
alpha = 0.435;

x = 0.1:0.1:L;
m = sqrt((h * P * (L^2)) / (K * A_c));

e1 = ((I^2) * R) + (alpha * I * T_h) + Q_h;
e2 = ((tanh(m) * cosh(m) * (x/L)) - (sinh(m) * (x/L)));
T = (e1 * e2 * L) / (K * m);

plot(x, T);
title('Graph of Temperature against Length');
ylabel('Temperature/degree celcius');
xlabel('Length/m');