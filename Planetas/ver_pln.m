% condiciones iniciales

x1 = 0.1;
y1 = 0.1;
xp1 = 5e-06;
yp1 = -5e-06;

x2 = 0;
y2 = 0;
xp2 = 5e-06;
yp2 = 0;

X = zeros(8,1);
X(1) = x1;
X(2) = y1;
X(3) = x2;
X(4) = y2;
X(5) = xp1;
X(6) = yp1;
X(7) = xp2;
X(8) = yp2;

h = 1000e-3;   % paso de integración
N = 50e3;    % iteraciones
m1 = 1;
m2 = 1;

t = ((1:N)'-1).*h;

p1 = zeros(N,2);
p2 = zeros(N,2);
for k = 1:N
    K1 = dos_planetas(X,m1,m2);
    K2 = dos_planetas(X+0.5.*h.*K1,m1,m2);
    K3 = dos_planetas(X+0.5.*h.*K2,m1,m2);
    K4 = dos_planetas(X+1.0.*h.*K3,m1,m2);

    X = X + (1/6).*h.*(K1+2.*K2+2.*K3+K4); 

    p1(k,1) = X(1);
    p1(k,2) = X(2);

    p2(k,1) = X(3);
    p2(k,2) = X(4);
end

for k = 1:100:N
    plot(p1(:,1),p1(:,2),'k', p2(:,1),p2(:,2),'b',...
        p1(k,1),p1(k,2),'ko',p2(k,1),p2(k,2),'bo')
    % axis([-1 1 -1 1])
    grid on
    set(gca,'TickLabelInterpreter','latex')
    xlabel('eje $x$' ,'Interpreter','latex')
    ylabel('eje $y$' ,'Interpreter','latex')
    title('Dos planetas ODE','interpreter','latex')
    pause(1e-9)
end