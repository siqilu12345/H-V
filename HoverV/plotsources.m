function plotsources
fname1=['/Users/siqilu/Desktop/crfl/crfl1.txt'];
fileid=fopen(fname1);
data=textscan(fileid,'%f %f %*[^\n]',100,'HeaderLines',10);
x=data{1};
y=data{2};
plot(x,y,'Marker','o','LineStyle','none');
hold on
plot([50,100,150,200],[0,0,0,0],'LineStyle','none',...
    'Marker','p','MarkerEdgeColor','r','MarkerSize',10);
xlim([-100,200]);
ylim([-150,150]);
hold off
xlabel({'x/km'});
title({'Position of Sources and receivers'});
ylabel({'y/km'});
saveas(gcf,'/Users/siqilu/Desktop/HV_figures/sources','epsc');
save('/Users/siqilu/Desktop/HV_figures/sources.fig');