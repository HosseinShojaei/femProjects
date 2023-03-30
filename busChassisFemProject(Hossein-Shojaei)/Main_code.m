clc
clear
close all
%% Truss definition

Nodes = xlsread('Data_Table.xlsx',2,'B2:C13');

Elements = [xlsread('Data_Table.xlsx',1,'B2:C24') ...
    xlsread('Data_Table.xlsx',1,'K2:K24') ...
    xlsread('Data_Table.xlsx',1,'L2:L24')];

Fext = [2, 2500,-90;
    3, 5000, -90;
    4, 5000, -90;
    5, 3750, -90;
    6, 1250, -90;
    8, 5000, 180;
    9, 4000, -90;
    10, 15000, 225];

supports = [6 1 1;
    7 2 0];

%% Elements stiffness

for i = 1:size(Elements,1)

    n1 = Elements(i,1);
    n2 = Elements(i,2);

    x1 = Nodes(n1,1);
    x2 = Nodes(n2,1);
    Dx = x2 - x1;

    y1 = Nodes(n1,2);
    y2 = Nodes(n2,2);
    Dy = y2 - y1;

    L(i) = sqrt(power(Dx,2) + power(Dy,2))*1000;
    Th(i) = atan2(Dy,Dx);

    A = Elements(i,3);
    E = Elements(i,4)*10^3;

    s = sin(Th(i));
    c = cos(Th(i));

    k{i} = A*E/L(i)*[c^2 c*s -c^2 -s*c
        s*c s^2 -s*c -s^2
        -c^2 -c*s c^2 s*c
        -s*c -s^2 s*c s^2];
end
%% Global stiffness

K = zeros(2*size(Nodes,1));
K0 = K;

for i = 1:size(Elements,1)

    n1 = Elements(i,1);
    n2 = Elements(i,2);

    K0(2*n1-1:2*n1, 2*n1-1:2*n1) = k{i}(1:2,1:2);
    K0(2*n1-1:2*n1, 2*n2-1:2*n2) = k{i}(1:2,3:4);
    K0(2*n2-1:2*n2, 2*n1-1:2*n1) = k{i}(3:4,1:2);
    K0(2*n2-1:2*n2, 2*n2-1:2*n2) = k{i}(3:4,3:4);

    K = K + K0;
    K0(:,:) = 0;

end

%% External force

F0 = zeros(2*size(Nodes,1),1);

for i = 1:size(Fext,1)

    Fnode = Fext(i,1);
    Fmag = Fext(i,2);
    Fang = Fext(i,3)/180*pi;

    fx = Fmag * cos(Fang);
    fy = Fmag * sin(Fang);

    F0(2*Fnode-1 : 2*Fnode,1)= [fx;fy];
end

%% Applying supports

cnt = 0;

for i = 1:size(supports,1)
    Snode = supports(i,1);
    Stype = supports(i,2);
    Sorien = supports(i,3);

    if Stype == 1
        if Sorien == 1
            cnt = cnt + 1;
            uu_zero(cnt) = 2*Snode - 1;
        elseif Sorien == 2
            cnt = cnt + 1;
            uu_zero(cnt) = 2*Snode;
        end
    elseif Stype == 2
        cnt = cnt + 2;
        uu_zero(cnt-1 : cnt) = 2*Snode-1 : 2*Snode;
    end
end

%% Solving Eq.

Kc = K;
Fc = F0;

Kc(:, uu_zero) = [];
Kc(uu_zero, :) = [];

Fc(uu_zero, :) = [];

U0 = Kc^-1*Fc;

uu_all = 1:2*size(Nodes,1);
uu_nonzero = uu_all;
uu_nonzero(uu_zero) = [];

U(uu_all, 1) = 0;
U(uu_nonzero, 1) = U0;

F = K*U;

for i = 1:size(Elements,1)

    s = sin(Th(i));
    c = cos(Th(i));

    n1 = Elements(i,1);
    n2 = Elements(i,2);

    Delta = [-c -s c s]*[U(2*n1-1); U(2*n1); U(2*n2-1); U(2*n2)];

    A = Elements(i,3);
    E = Elements(i,4)*10^3;

    P = A*E/L(i)*Delta;

    El_result(i, 1) = Delta;
    El_result(i, 2) = P;
    El_result(i, 3) = P/A;
end

%% Display results

fprintf('\n')
fprintf('**************[ Nodes Displacement ]**************\n')

for i = 1:size(Nodes,1)

    fprintf('Node(%2g) X_disp:%8.5g um | Y_disp:%8.5g um\n',i,U(2*i-1)*1000, U(2*i)*1000)
end

fprintf('\n\n')
fprintf('**************[ Elements Force ]**************\n')
for i = 1:size(Elements,1)
    fprintf('Element (%2g) Force: %g N\n',i,El_result(i, 2)*1e3)
end

fprintf('\n\n')
fprintf('**************[ Elemennts Stress ]**************\n')
for i = 1:size(Elements,1)
    fprintf(' Element (%2g) Stress: %g MPa\n',i,El_result(i, 3))
end