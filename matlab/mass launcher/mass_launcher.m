%of mass in lb
m1 = 2;
m2 = 2;
m3 = 0.5;

%of stiffness k
k1 = 23.7;
k2 = 23.7;
k3 = 23.7;

% acceleration due to gravity
g = 9.81; %m/s2

% design values (in lb and lb/in)
x0i = [m1 m2 m3 k1 k2 k3];

% convert inches to m
k1 = inch_to_meter(k1);k2 = inch_to_meter(k2);k3 = inch_to_meter(k3);

% convert to kg
m1 = pound_to_kilogram(m1);m2 = pound_to_kilogram(m2);m3 = pound_to_kilogram(m3);

% optimization: involving maximization of velocity and maneuver
objfunction = @(x) -objective_function(x);

% ------------------------------------prepare constraints---------
% unequality constraint
A = [1 1 1 0 0 0]; B = pound_to_kilogram(7); %kg

% equality constraint
Aeq = []; Beq = [];

% bounds
m_lb = pound_to_kilogram(0.1);
m_ub = pound_to_kilogram(6);

k_lb = inch_to_meter(14);
k_ub = inch_to_meter(1310);
ub = [m_ub m_ub m_ub k_ub k_ub k_ub]; lb = [m_lb m_lb m_lb k_lb k_lb k_lb];

% --------------------optimization initial guess------------------
x0 = [m1 m2 m3 k1 k2 k3];

% objective_function(x0)

% ------------------optimization options-----------------------
opt_algo = 'interior-point'; %optimization algorithm
options = optimoptions('fmincon','Algorithm', opt_algo,'Display','iter');

% ------------------------call optimization function-----------------
[x_optimal, fval, exitflag, output] = fmincon(objfunction, x0, A, B, Aeq, Beq, lb, ub);

% the solution after otpimization
z = solve_ode(x_optimal, .25, 0);

% the data plot
displacement = z(:, 1:3);
velocity = z(:, 4:6);

figure
subplot(2,1,1);
plot(displacement)
title('displacement against time');
legend('x1', 'x2', 'x3');

subplot(2,1,2);
plot(velocity)
title('velocity against time');
legend('v1', 'v2', 'v3');

% the launch velocity of topmost mass
launch_velocity = abs(fval);

max_height = (launch_velocity^2)/(2 * g);

% the parameters x: [m1 m2 m3 k1 k2 k3]
m1 = x_optimal(1);m2 = x_optimal(2);m3 = x_optimal(3);
k1 = x_optimal(4);k2 = x_optimal(5);k3 = x_optimal(6);

% convert inches to m
k1 = meter_to_inch(k1);k2 = meter_to_inch(k2);k3 = meter_to_inch(k3);

% convert to kg
m1 = kilogram_to_pound(m1);m2 = kilogram_to_pound(m2);m3 = kilogram_to_pound(m3);

% design results
x = [m1 m2 m3 k1 k2 k3];

form = 'm1 = %.2f lb, m2 = %.2f lb, m3 = %.2f lb, k1 = %.2f lb/in, k2 = %.2f lb/in, k3 = %.2f lb/in, launch_velocity = %.2f m/s2, max_height = %.4f m \n\n';
fprintf(form, x, launch_velocity, max_height)
