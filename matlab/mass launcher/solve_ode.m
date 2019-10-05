function velocity = solve_ode(x, tf, with_event)
    % the parameters x: [m1 m2 m3 k1 k2 k3]
    m1 = x(1);m2 = x(2);m3 = x(3);
    k1 = x(4);k2 = x(5);k3 = x(6);
    c = 0.2;
    
    g = 9.81; %acceleration due to gravity m/s2
    h = 0.5; %meter
    
    % the mass matrix
    M = [
        m1,  0, 0;
        0,  m2, 0;
        0,  0,  m3;
    ];

    % the k matrix
    K = [
        k1+k2, -k2,    0;
        -k2,   k2+k3, -k3;
        0,     -k3,    k3;
    ];
   
    % the c matrix
    C = [
        2*c, -c,   0;
        -c,  2*c, -c;
        0,   -c,   c;
    ];
    
    % the ordinary differential equation (ODE)
    dy_dt = @(t, y) [y(4:6);
        -(M \ C) * y(4:6) - (M \ K) * y(1:3)];
        
    %drop velocity
    v = (2 * g * h)^0.5;

    % initial values
    y0 = [0 0 0 v v v];
    
    % the ode options
    if with_event
        odeopt = odeset ('RelTol', 0.00001, 'AbsTol', 0.00001, 'InitialStep', 0.5, 'MaxStep', 0.5, 'Events', @launchEventsFcn);
        
        % the results
        [t, velocity, te,ye,ie] = ode45(dy_dt, [0 tf], y0, odeopt);
        
    else
        odeopt = odeset ('RelTol', 0.00001, 'AbsTol', 0.00001, 'InitialStep', 0.5, 'MaxStep', 0.5);
        
        % the results
        [t, velocity] = ode45(dy_dt, [0 tf], y0, odeopt);
    end 
end


function [position,isterminal,direction] = launchEventsFcn(t, y)
    position = y(3); % The value that we want to be zero
    isterminal = 1;  % Halt integration 
    direction = 0;   % The zero can be approached from either direction
end
