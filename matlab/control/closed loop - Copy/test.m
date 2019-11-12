clear all;
close all;
clc;

%controller;
K = 1;
s = tf('s');

G = 1 / (s-1);
H = (s+2)/ ((s+1)^2 + 1);

%open loop
open_loop = G * H * K;

% the feed back
closed_loop = feedback(K * G, H);

%margin value
margin(closed_loop)

%the stable K
% rlocus(open_loop);
% rlocus(closed_loop);

% nyquist(closed_loop);

