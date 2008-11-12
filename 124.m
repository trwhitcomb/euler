% Project Euler
% Problem 124
clear all;
close all;

n = 1:100000;
for ii = n
	rad(ii) = prod(unique(factor(ii)));
end
E = [n.' rad.'];
sortE = sortrows(E, [2 1]);
sortE(10000,:);
