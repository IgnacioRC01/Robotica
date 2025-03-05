function R = euler2rotMat(euler, secuencia)
%euler2rotMat Convierte la orientación en ángulos de Euler en una matriz de rotación.
%
% Ejemplo de uso:
% euler = [pi/2; -pi/4; pi/6]
% secuencia = "XYZ"
% R = euler2rotMat(euler, secuencia)

phi = euler(1,:);      % phi:   rotación alrededor del eje X
theta = euler(2,:);    % theta: rotación alrededor del eje Y
psi = euler(3,:);      % psi:   rotación alrededor del eje Z

%phi = euler(1)
%theta = euler(2)
%psi = euler(3)

if secuencia == "XYZ"
    R1 = Rx(phi);
    R2 = Ry(theta);
    R3 = Rz(psi);
    R = (R1 * R2 * R3);
end

