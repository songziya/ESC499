x = linspace(0,10);
y = linspace(0,10);
%% Rules:
%  1. x > b (x - b > 0)
%  S(16(x-b))
%  
%  2. x < b [~(x > b)]
%  (1): S(-16(x-b))
%  (2): 1-S(16(x-b))
%  
%  3. cond A & cond B
%  (1): S(16*A)*S(16*B)
% 
%  4. cond A | cond B  [~((~cond A) & (~cond B))]
%  (1): 1-S(-16*A)*S(-16*B)
%  (2): 1-(1-S(16*A))*(1-S(16*B))
%% x > 4
z = zeros(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= sigm(x(j),4,16);
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;
%% x < 6
z = zeros(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= sigm(x(j),6,-16);
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;
%% x > 4 AND x < 6
z = zeros(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= sigm(x(j),4,16)*sigm(x(j),6,-16);
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;
%% x > 5 OR y > 5
z = ones(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= z(i,j)-sigm(y(i),5,-16)*sigm(x(j),5,-16);
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;
%% x > 5 OR y > 5
z = ones(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= z(i,j)-(1-sigm(y(i),5,16))*(1-sigm(x(j),5,16));
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;
%% x < 4 OR x > 6 OR y < 4 OR y > 6
z = ones(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= z(i,j)-sigm(y(i),6,-16)*sigm(y(i),4,16)*sigm(x(j),6,-16)*sigm(x(j),4,16);
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;
%% (x-5)^2 + (y-5)^2 > 9
z = ones(100,100);
for i=1:100
    for j = 1:100
        z(i,j)= sigm((y(i)-5)^2+(x(j)-5)^2,9,16);
    end
end
figure();surf(x,y,z);xlabel('x');ylabel('y');shading interp;