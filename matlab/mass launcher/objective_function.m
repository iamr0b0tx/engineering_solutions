function max_velocity = objective_function(x)
    % the parameters x: [m1 m2 m3 k1 k2 k3]
    velocity = solve_ode(x, 5, 1);
    max_velocity = velocity(end);
end
