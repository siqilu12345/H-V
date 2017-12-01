function plothv
leftfreq=1;
rightfreq=20;
%{
start=zeros(9,4);
last=zeros(9,4);
start(1,:)¡¢=[161,401,561,721];
last(1,:)=[480,560,800,961];
start(2,:)=[161,401,561,721];
last(2,:)=[400,560,800,960];
start(3,:)=[161,401,561,721];
last(3,:)=[400,560,800,960];
start(4,:)=[161,401,561,721];
last(4,:)=[480,560,800,961];
start(5,:)=[161,401,561,721];
last(5,:)=[400,560,800,960];
start(6,:)=[161,401,561,721];
last(6,:)=[400,560,800,960];
start(7,:)=[161,401,561,721];
last(7,:)=[400,560,800,960];
start(8,:)=[161,401,561,801];
last(8,:)=[400,560,1120,1440];
start(9,:)=[161,401,561,721];
last(9,:)=[400,560,800,960];
x=cell(9,4);
y=cell(9,4);
for i=1:9
    filen=i;
    for j=1:4
        [x{i,j},y{i,j}]=computehv(filen,j,start(i,j),last(i,j));
    end
end
for i=1:4
    figure(i)
    for j=1:9
        plot(x{j,i},y{j,i});
        a=x{j,i};
        [M,b]=max(y{j,i});
        text(a(b),M,num2str(j));
        hold on
    end
    hold off
end
%}
%{
for j=1:9
    f2=mod(j-1,3);
    f3=floor((j-1)/3);
    subplot(3,3,j);
    for i=0:17
        [x,y]=trycomputehv(i,f2,f3);
        plot(x,y,'--','LineWidth',0.5);
        xx(i+1,:)=x;
        yy(i+1,:)=y;
        hold on
    end
    plot(xx,mean(yy,1),'LineWidth',2)
    xlim([0.1,3]);
    ylim([0,50]);
    hold off
end
%}
%{
for i=0:17
    [x,y]=trycomputehv(i,0,0);
    plot(x,y,'--','LineWidth',0.5);
    xx(i+1,:)=x;
    yy(i+1,:)=y;
    hold on
end
plot(xx,mean(yy,1),'LineWidth',2)
xlim([0.1,3]);
%}
[x1,y1]=trycomputehv(1);
%{
[x2,y2]=trycomputehv(6);
[x3,y3]=trycomputehv(7);
[x4,y4]=trycomputehv(8);
[x5,y5]=trycomputehv(9);
[x6,y6]=trycomputehv(10);
plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
%}
figure(1)
plot(x1,1./y1)
xlim([leftfreq,rightfreq]);
xlabel({'Frequency/Hz'});
title({'H/V ratio'});
ylabel({'H/V Amplitude'});
%saveas(gcf,'/Users/siqilu/Desktop/HV_figures/enhance','epsc');
%save('/Users/siqilu/Desktop/HV_figures/enhance.fig');
%{
figure(2)
findpeaks(y1,'MinPeakProminence',1.6)
[pks,locs]=findpeaks(y1,'MinPeakProminence',1.6);
d=x1(locs)
figure(3)
plot(d)
%}