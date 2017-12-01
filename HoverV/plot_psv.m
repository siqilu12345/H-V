function plot_psv
i=11;
filen=1;
start=1;
last=4096;
dt=0.1;
fname1=['/Users/siqilu/Desktop/testcrfl/crflpsv_',num2str(filen),'.txt'];
fileid=fopen(fname1);
data=textscan(fileid,'%f %f');
rawdata=cell2mat(data(2));
rawdata_one=rawdata((2*i-2)*last+1:last*(2*i-1));
rawdata_two=rawdata((2*i-1)*last+1:last*2*i);
time=[start:last]*dt;
%{
[b,a] = butter(6,[1.7,1.8]/8,'bandpass');
freqz(b,a);
rawdata_one = filter(b,a,rawdata_one);
rawdata_two = filter(b,a,rawdata_two);
%}
subplot(3,1,1)
plot(time(start:last),rawdata_one(start:last))
title({'z component'});
%xlim([0,256]);
%saveas(gcf,'/Users/siqilu/Desktop/HV_figures/z_component.jpg');
hold on
subplot(3,1,2)
plot(time(start:last),rawdata_two(start:last))
title({'x component'});
ylabel({'Velocity/(m/s)'});
%xlim([0,256]);
%saveas(gcf,'/Users/siqilu/Desktop/HV_figures/x_component.jpg');
hold on
fclose(fileid);
fname2=['/Users/siqilu/Desktop/testcrfl/crflsh_',num2str(filen),'.txt'];
fileid=fopen(fname2);
data=textscan(fileid,'%f %f');
rawdata=cell2mat(data(2));
rawdata_three=rawdata((i-1)*last+1:last*i);
%rawdata_three = filter(b,a,rawdata_three);
subplot(3,1,3)
plot(time(start:last),rawdata_three(start:last))
title({'y component'});
xlabel({'Time/s'});
%xlim([0,256]);
%ylim([-0.1,0.1]);
%saveas(gcf,'/Users/siqilu/Desktop/HV_figures/y_component.jpg');
hold off
fclose(fileid);
%{
w=tukeywin(last,0.95);
rawdata_one=rawdata_one.*w;
rawdata_two=rawdata_two.*w;
rawdata_three=rawdata_three.*w;
spe1=abs(fft(rawdata_one));
spe2=abs(fft(rawdata_two));
spe3=abs(fft(rawdata_three));
figure(2)
plot(spe1);
figure(3)
plot(spe2);
figure(4)
plot(spe3);
%}
%saveas(gcf,'/Users/siqilu/Desktop/HV_figures/seismo','epsc');
%save('/Users/siqilu/Desktop/HV_figures/seismo.fig');
%{
figure(2)
spectrogram(rawdata_one,256,252,256,50,'yaxis');
ylim([0.1,20]);
figure(3)
spectrogram(rawdata_two,256,252,256,50,'yaxis');
ylim([0.1,20]);
figure(4)
spectrogram(rawdata_three,256,252,256,50,'yaxis');
ylim([0.1,20]);
%}