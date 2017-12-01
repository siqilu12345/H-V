function y=konno_ohmachi_window(b,center,data)
window=zeros(length(data),1);
if center==0
    window(1)=1;
else
    for i=1:length(data)
        if data(i)==center
            window(i)=1;
        elseif data(i)==0
            window(i)=0;
        else
            a=log10(data(i)./center).^b;
            a=sin(a)/a;
            a=a.^4;
            window(i)=a;
        end
    end
end
window=window./sum(window);
y=window;
