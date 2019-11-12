clear;
clc;
close all;

%initialize the values
D = 1.2672 * 10^-6; %in m2/s
C0 = 0;
CR = 0;

%max values
xmax = 0.225; %in meters
tmax = 7200; %in seconds

%the delta (change values)
dx = 0.0225;
dt = 1800;

%the iteration
number_of_iterations = 3;

%the CL values and the titles
titles = {
    'Source of fuel for frying with kerosene at CL = 0.921 mol/m3'
    'Source of fuel for frying with LPG at CL = 0.817 mol/m3'
    
    'Source of fuel for stewing with kerosene at CL = 0.896 mol/m3'
    'Source of fuel for stewing with LPG at CL = 0.71 mol/m3'
    
    'Source of fuel for boiling with kerosene at CL = 0.856 mol/m3'
    'Source of fuel for boiling with LPG at CL = 0.654 mol/m3'
    
    'Source of fuel with firewood at CL = 4.797 mol/m3'
};

CL = [0.921, 0.817, 0.896, 0.71, 0.856, 0.654, 4.797]; %in mol/m3

%get value of C
for i=1:length(titles)
    
    %get a figure
    figure;
    
    %hold the current figure
    hold on;
    
    for t=0:dt:tmax
%         if CL(i) ~= 0.921 || t ~= 0
%             continue
%         end
        %the variation of x along xmax
        x = 0:dx:xmax;
        
        %the equation
        iteration_solution = iteration(D, C0, CR, CL(i), xmax, x, t, number_of_iterations);

        %the C solutions
        C = CL(i) + (x * (CR - CL(i)) / xmax) + iteration_solution;
        
        %generate plot for x varition at current t
        plot(x, C)
        
        %set the title
        title(titles(i));
        
        xlabel('Concentration (mol/m3)');
        ylabel('distance meters');
    end
       
    %add legend to graph
    legend('t = 0s', 't = 1800s', 't = 3600s', 't = 5400s', 't = 7200s')
    
    %release the graph for another graph
    hold off;
    
end

