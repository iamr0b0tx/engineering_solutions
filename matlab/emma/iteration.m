function iteration_solution = iteration(D, C0, CR, CL, xmax, x, t, number_of_iterations)
    %holds the solution of the iteraation
    iteration_solution = 0;
    
    %the summation iteration
    for m=1:number_of_iterations
        %get the lambda m value
        lambda_m = lambda(m ,xmax);
        
        %get the value of Cm
        Cm = CM(C0, CR, CL, m);
        
        %calculate for the iteration
        iteration_solution = iteration_solution + (Cm * ((exp(1) ^ (-(lambda_m^2) * D * t)) * sin(lambda_m * x)));
    end

end

function Cm = CM(C0, CR, CL, m)
    if(mod(m, 2) == 0)
        Cm = 2 * (CR - CL) / (m*pi);
    else
        Cm = ((4*(C0 - CL)) - (2 * (CR - CL))) / (m * pi);
    end
end

function lambda_m = lambda(m, xmax)
    %calculate lambda m
    lambda_m = (m * pi) / xmax;
end