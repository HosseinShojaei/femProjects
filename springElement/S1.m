% Analysis of Spring System using Finite Element Method

clc
clear
close all

%% Nodes
Nn = 4;

%% Elements
Elements = [1 3; 3 4; 4 2];
Ne = size(Elements,1);

k =[1000; 2000; 3000];

nDofs=Nn;              % total system dofs
F = zeros(nDofs,1);
U = zeros(nDofs,1);

%% computation of the system stiffness matrix
K = zeros(nDofs);
for i=1:Ne
    eNodes=Elements(i,:);
    
    Ke = k(i)*[1 -1; -1 1];
    
    K(eNodes,eNodes) = K(eNodes,eNodes) + Ke;
end

%% Loading
F(4) = 5000;

%% Boundary Conditions
FixedDofs = [1 2];

%% Solution
FreeDofs = setdiff( (1:nDofs)', FixedDofs);
UF = K(FreeDofs,FreeDofs) \ F(FreeDofs) ;
U(FreeDofs) = UF;

%% Global Nodal Forces
Fn = K*U;

%% Local Element Forces
Fe = zeros(Ne,2);
for i=1:Ne
    eNodes=Elements(i,:);
    
    Fe(i,:) = k(i)*[1 -1; -1 1]*U(eNodes);
end

uNodes=[(1:Nn)' U];
fprintf('\n\nDisplacements on Nodes\n')
fprintf('--------------------------\n')
fprintf('  Node         u \n')
fprintf('--------------------------\n')
fprintf('%5d %13.5f \n',uNodes')

fNodes=[(1:Nn)' Fn];
fprintf('\n\nGlobal Nodal Forces\n')
fprintf('--------------------------\n')
fprintf('  Node         F \n')
fprintf('--------------------------\n')
fprintf('%5d %13.2f \n',fNodes')

fElements=[(1:Ne)' Fe(:,1) Fe(:,2)];
fprintf('\n\nForces in Elements\n')
fprintf('-------------------------------------------\n')
fprintf('  Element        f(1)          f(2) \n')
fprintf('-------------------------------------------\n')
fprintf('%6d %15.2f %14.2f\n',fElements')

