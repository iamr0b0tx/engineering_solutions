%clear variable work space
clear
clc;

%load the data
load('inital_data.mat')

t = data(:,1)*60;
T_db = data(:,2);
T_wb = data(:,3);
PHI1 = data(:,4);
P_w = data(:,5);
P_vs = data(:,6);

% inital values
P_atm = 1.01325;

% cal values
P_v = P_w - ((P_atm - P_w).*(T_db - T_wb) ./ (1547 - (1.44*T_wb)));
w = (0.622*P_v) ./ (P_atm - P_v);
Y = w ./ (w + 1);
PHI2 = 100 * P_v ./ P_vs;
muo = PHI1 .* ((P_atm - P_vs) ./ (P_atm - P_v));

dx = [data P_v w Y PHI2 muo];

filename = 'data.xlsx';
xlswrite(filename, dx)

%plot graph
figure

%hold the figure
hold on

%RH against t
plot(t, PHI1, '-', t, PHI2, '--', 'LineWidth', 2.5);

% axis label
xlabel('t/s');
ylabel('Relative Humidity/%');

% the key map
legend('Experimental Relative Humidity', 'Calculated Relative Humidity');

% a second figure
figure

%RH against log t
plot(log10(t), PHI1, '-', log10(t), PHI2, '--', 'LineWidth', 2.5);

% axis label
xlabel('Log t/s');
ylabel('Relative Humidity/%');

% the key map
legend('Experimental Relative Humidity', 'Calculated Relative Humidity');

%third figure
figure

%Humidity Ratio (W) against t
plot(t, PHI2, 'LineWidth', 2.5);

% axis label
xlabel('t/s');
ylabel('Calculated Relative Humidity/%');

% fourth figure
figure

%RH against log t
plot(log10(t), PHI2, 'LineWidth', 2.5);

% axis label
xlabel('Log t/s');
ylabel('Calculated Relative Humidity/%');

% fifth figure
figure

%T against t
plot(t, T_wb, '-', t, T_db, '--', 'LineWidth', 2.5);

legend('Temperature of wet bulb', 'Temperature of dry bulb');

% axis label
xlabel('t/s');
ylabel('Temperature/°C');

% sixth figure
figure

%T against log t
plot(log10(t), T_wb, '-', log10(t), T_db, '--', 'LineWidth', 2.5);

legend('Temperature of wet bulb', 'Temperature of dry bulb');

% axis label
xlabel('Log t/s');
ylabel('Temperature/°C');