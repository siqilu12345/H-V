function y=taper(x)
for i=1:512
    if i<=20
        x(i)=x(i)*cos((i-1-20)/20*pi/2);
    else if i>=492
        x(i)=x(i)*cos((i-492)/20*pi/2);
        end
    end
end
y=x;