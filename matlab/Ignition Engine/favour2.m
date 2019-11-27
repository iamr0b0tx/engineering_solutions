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
sie1_T_3 = T_3;

%solve for values
T_1 = 0.4 * T_3;
sie1_W_net = sie_W_net_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

T_1 = 0.0687*T_3;
sie1_eff = sie_efficiency_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

%-----------------------------for plot of Temperature exhaust and net work
T_3 = 945;
T_1 = 0.362*T_3;
W_ac = 1:1:4;
sie2_W_ac = W_ac;

sie2_W_net = sie_W_net_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);
sie2_T_exh = sie_T_exh_f(C_v, T_1, R_v, gamma, W_ac, C_p, T_3);

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
cie1_T_3 = T_3;

%solve for values
T_1 = 0.1*T_3;
cie1_W_net = cie_W_net_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);

T_1 = 0.0687*T_3;
cie1_eff = cie_efficiency_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);


%-----------------------------for plot of Temperature exhaust and net work
T_3 = 945;
W_ac = 1:1:4;
cie2_W_ac = W_ac;

T_1 = 0.362*T_3;
cie2_T_exh = cie_T_exh_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);

T_1 = 0.1*T_3;
cie2_W_net = cie_W_net_f(C_v, T_1, gamma, T_3, R_v, beta, W_ac, C_p);

%===================================
%plot values
figure
plot(sie1_T_3, sie1_W_net, 'Color', 'blue');
title('Graph of net work done against Temperature');
ylabel('Work done');
xlabel('Temperature');

hold on

%plot values
plot(cie1_T_3, cie1_W_net, 'Color', 'red');
legend('spark ignition engine', 'compression ignition engine');
hold off

%==================================

figure
plot(sie1_T_3, sie1_eff, 'Color', 'blue');
title('Graph of efficiency against Temperature');
ylabel('Efficiency');
xlabel('Temperature');
hold on

plot(cie1_T_3, cie1_eff, 'Color', 'red');
legend('spark ignition engine', 'compression ignition engine');
hold off

%=============================
figure
plot(sie2_W_ac, sie2_W_net, 'Color', 'blue');
title('Graph of net work done against Work Ac');
xlabel('Work Ac');
ylabel('Net Work done');
hold on

plot(cie2_W_ac, cie2_W_net, 'Color', 'red');
legend('spark ignition engine', 'compression ignition engine');
hold off

%================
figure
plot(sie2_W_ac, sie2_T_exh, 'Color', 'blue');
title('Graph of Exhaust Temperature against Work Ac');
hold on

plot(cie2_W_ac, cie2_T_exh, 'Color', 'red');
title('Graph of Exhaust Temperature against Work Ac in ');
xlabel('Work Ac');
ylabel('Temperature of Exhaust');

legend('spark ignition engine', 'compression ignition engine');
hold off
