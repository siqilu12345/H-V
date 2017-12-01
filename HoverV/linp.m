function m=linp(point)
pos=[point.Position];
a=pos(1:2:end);
a=sort(a);
a=a';
x=[1:length(a)];
X=[ones(length(a),1),x'];
m=X\a;
yCalc1=X*m;
scatter(x,a)
hold on
plot(x,yCalc1)
hold off