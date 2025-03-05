function euler = rotMat2euler(R, secuencia)
%rotMat2euler Convierte una matriz de rotación a la orientación en ángulos de Euler.
%
% Ejemplo de uso:
% R = [-1 0 0
%       0 0 1
%       0 1 0];
% secuencia = "XYZ"
% euler = rotMat2euler(R, secuencia)

% Obtén las ecuaciones de la imagen
if secuencia == "XYZ"
    euler = rad2deg(euler);
    phi = euler(1)      % phi:   rotación alrededor del eje X
    theta = euler(2)    % theta: rotación alrededor del eje Y
    psi = euler(3)      % psi:   rotación alrededor del eje Z
    euler = [phi;theta;psi];

end

