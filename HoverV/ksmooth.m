function y=ksmooth(trans,k)
n=length(trans);
f=[0:n-1];
f=f';
sm=konno_ohmachi_matrix(f,k);
y=sm*trans;