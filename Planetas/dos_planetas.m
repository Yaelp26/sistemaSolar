function XP = dos_planetas(X,m1,m2)
    % ODE dos planetas

    XP = zeros(8,1);
    G = 6.672e-11;      % constante gravitacional
    
    XP(1:4) = X(5:8);

    L = sqrt(  (X(3)-X(1))^2  +  (X(4)-X(2))^2  ) + 1e-9;

    XP(5) = (  G*m2*(X(3)-X(1))  )/(L^3);
    XP(6) = (  G*m2*(X(4)-X(2))  )/(L^3);
    XP(7) = (  G*m1*(X(1)-X(3))  )/(L^3);
    XP(8) = (  G*m1*(X(2)-X(4))  )/(L^3);
end