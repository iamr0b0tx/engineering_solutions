clc;
clear;
close all;

%initial values
C_v = 0.718;
R_v = 8.5;
gamma = 1.4;
W_ac = 2;
C_p = 1.005;

sie_T_exh_f = @(C_v, T_1, R_v, gamma, W_ac, C_p, T_3) (T_3 .* (R_v.^(1 - gamma))) - (W_ac ./ C_p);
sie_W_net_f = @(C_v, T_1, R_v, gamma, W_ac, C_p, T_3) C_v .* ((T_1 .* (1 - (R_v.^(gamma - 1)))) + (T_3 .* (1 - (R_v.^(1 - gamma)))) + (W_ac ./ C_p));
sie_efficiency_f = @(C_v, T_1, R_v, gamma, W_ac, C_p, T_3) 1 - (((T_3 .* (R_v.^(1 - gamma))) - (W_ac ./ C_p) - T_1) ./ (T_3 - (T_1 .* (R_v.^(gamma - 1)))));

%----------------------------for plot of efficiency and net work------
%the independent variable
T_3 = 700:100:1500;

%solve for values
T_1 = 0.4 * T_3;
W_net = sie_W_net_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

T_1 = 0.0687*T_3;
eff = sie_efficiency_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

%plot values
figure
plot(T_3, W_net);
title('Graph of net work done against Temperature in spark ignition engine');
ylabel('Work done');
xlabel('Temperature');

figure
plot(T_3, eff);
title('Graph of efficiency against Temperature in spark ignition engine');
ylabel('Efficiency');
xlabel('Temperature');

%-----------------------------for plot of Temperature exhaust and net work
T_3 = 945;
T_1 = 0.362*T_3;
W_ac = 1:1:4;

W_net = sie_W_net_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);
T_exh = sie_T_exh_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

figure
plot(W_ac, W_net);
title('Graph of net work done against Work Ac in spark ignition engine');
xlabel('Work Ac');
ylabel('Net Work done');

figure
plot(W_ac, T_exh);
title('Graph of Exhaust Temperature against Work Ac in spark ignition engine');
xlabel('Work Ac');
ylabel('Temperature of Exhaust');

%-------------------------compression Ignition engine--------
cie_W_net_f = @(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p) (C_v .* T_1) .* (gamma + ((T_1./T_3) .* (1 - (gamma.*(R_v.^(gamma-1))))) - ((gamma - ((beta./R_v).^(gamma-1)))/((gamma.*(R_v.^(gamma-1))) - (beta.^(gamma-1)))) - (W_ac./(T_3.*C_p)));
cie_T_exh_f = @(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p) ((T_3.*(gamma - ((beta./R_v).^(gamma-1)))) ./ ((gamma.*(R_v.^(gamma-1))) - (beta.^(gamma - 1)))) - (W_ac./C_p);
cie_efficiency_f = @(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p) ((T_3.*gamma) + (T_1.*(1 - (gamma.*(R_v.^(gamma-1))))) - cie_T_exh_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p)) ./ (gamma.*(T_3 - (T_1.*(R_v.^(gamma-1)))));

%initial values
R_v = 16.3;
beta = 2;
gamma = 1.4;
W_ac = 2;
C_p = 1.005;

%----------------------------for plot of efficiency and net work------
%the independent variable
T_3 = 700:100:1500;

%solve for values
T_1 = 0.4*T_3;
W_net = cie_W_net_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);

T_1 = 0.0687*T_3;
eff = cie_efficiency_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);

%plot values
figure
plot(T_3, W_net);
title('Graph of net work done against Temperature in compression ignition engine');
ylabel('Work done');
xlabel('Temperature');

figure
plot(T_3, eff);
title('Graph of efficiency against Temperature in compression ignition engine');
ylabel('Efficiency');
xlabel('Temperature');

%-----------------------------for plot of Temperature exhaust and net work
T_3 = 945;
W_ac = 1:1:4;

T_1 = 0.362*T_3;
W_net = cie_W_net_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);
T_exh = cie_T_exh_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);

figure
plot(W_ac, W_net);
title('Graph of net work done against Work Ac in compression ignition engine');
xlabel('Work Ac');
ylabel('Net Work done');

figure
plot(W_ac, T_exh);
title('Graph of Exhaust Temperature against Work Ac in compression ignition engine');
xlabel('Work Ac');
ylabel('Temperature of Exhaust');
