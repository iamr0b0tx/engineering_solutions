clc;
clear;
close all;

%initial values
C_v = 0.718;
T_1 = 1200;
R_v = 8.5;
gamma = 1.4;
W_ac = 2000;
C_p = 1.005;

sie_T_exh_f = @(C_v, T_1, R_v, gamma, W_ac, C_p, T_3) (T_3 .* (R_v.^(1 - gamma))) - (W_ac ./ C_p);
sie_W_net_f = @(C_v, T_1, R_v, gamma, W_ac, C_p, T_3) C_v .* ((T_1 .* (1 - (R_v.^(gamma - 1)))) + (T_3 .* (1 - (R_v.^(1 - gamma)))) + (W_ac ./ C_p));
sie_efficiency_f = @(C_v, T_1, R_v, gamma, W_ac, C_p, T_3) 1 - (((T_3 .* (R_v.^(1 - gamma))) - (W_ac ./ C_p) - T_1) ./ (T_3 - (T_1 .* (R_v.^(gamma - 1)))));

%----------------------------for plot of efficiency and net work------
%the independent variable
T_3 = 700:100:1500;

%solve for values
W_net = sie_Wnet_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);
eff = sie_efficiency_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

%plot values
figure
plot(W_net, T_3);
title('Graph of Temperature against net work done');
xlabel('Work done');
ylabel('Temperature');

plot(eff, T_3);
title('Graph of Temperature against efficiency');
xlabel('Efficiency');
ylabel('Temperature');

%-----------------------------for plot of Temperature exhaust and net work
T_3 = 1000;
W_ac = 1000:100:4000;

W_net = sie_Wnet_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);
T_exh = sie_Texh_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

figure
plot(W_net, W_ac);
title('Graph of net work done against Work Ac');
xlabel('Work done');
ylabel('Work');

plot(T_exh, W_ac);
title('Graph of Exhaust Temperature against Work Ac');
xlabel('Work A c');
ylabel('Temperature of Exhaust');

cie_W_net_f = (C_v)