A = zeros(5);  # create 5x5 matrix filled with zeros
B = ones(7);   # create 7x7 matrix filled with ones
I = eye(10);   # create 10x10 matrix filled with ones on diagonal and zeros elsewhere

E = [ 1, 2, 3;
       4, 5, 6;
       7, 8, 9 ];

F = [ 1, 2, 3;
      4, 5, 6;
      7,8, 9 ];

A[1,3] = 5 ;

ADD = E .+ F;
SUB = E .- F;
MUL = E .* F;
DIV = E ./ F;

print A;
print ADD, SUB;
print MUL;
