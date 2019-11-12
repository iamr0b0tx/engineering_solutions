clear all;
close all;
clc;

%controller and plant;
K = 1;
s = tf('s');

G = 1 / (s^2 + 2*s - 1);
H = 1/ (s+1);

%open loop transfer function OLTF
open_loop = G * K;

%the feed back %closed loop transfer function CLTF
closed_loop = feedback(K * G, H);

%margin value
margin(closed_loop)

%the stable K 
%remove the percentage symbol from the rlocus to print the root locus graph
%rlocus(open_loop);
%rlocus(closed_loop);

%remove the percentage symbol from the nyquist to print the nyquist graph
%nyquist(closed_loop);

