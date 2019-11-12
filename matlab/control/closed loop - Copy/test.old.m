close all;
clc;

K = realp('k', 1);
s = tf('s');

G = 1 / (s-1);
H = (s+2)/ ((s+1)^2 + 1);

for K=1:1:10
    T = feedback(G*K, H);
    
    figure
    margin(T);
end

%T = feedback(G*K, H);
% 
% figure
% step(T);
% 
% figure
% rlocus(T);
