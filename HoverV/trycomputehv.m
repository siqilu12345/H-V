function [x,y]=trycomputehv(filen1)
start=1;
last=2048;
l=2048;
i=1;
nyquistf=25;
%{
fname1=['/Users/siqilu/Desktop/data/crflpsv_th',num2str(filen1),'r',...
    num2str(f2),'d',num2str(f3),'.txt'];
%}
fname1=['/Users/siqilu/Desktop/data/crflpsv_',num2str(filen1),'.txt'];
fileid=fopen(fname1);
data=textscan(fileid,'%f %f');
rawdata=cell2mat(data(2));
rawdata_one=rawdata((2*i-2)*l+1:l*(2*i-1));
rawdata_one=rawdata_one(start:last);
rawdata_two=rawdata((2*i-1)*l+1:l*2*i);
rawdata_two=rawdata_two(start:last);
fclose(fileid);
%{
fname2=['/Users/siqilu/Desktop/data/crflsh_th',num2str(filen1),'r',...
    num2str(f2),'d',num2str(f3),'.txt'];
%}
fname2=['/Users/siqilu/Desktop/data/crflsh_',num2str(filen1),'.txt'];
fileid=fopen(fname2);
data=textscan(fileid,'%f %f');
rawdata=cell2mat(data(2));
fclose(fileid);
rawdata_three=rawdata((i-1)*l+1:l*i);
rawdata_three=rawdata_three(start:last);
w=tukeywin(last,0.95);
rawdata_one=rawdata_one.*w;
rawdata_two=rawdata_two.*w;
rawdata_three=rawdata_three.*w;
spe1=abs(fft(rawdata_one));
spe2=abs(fft(rawdata_two));
spe3=abs(fft(rawdata_three));
%{
f=[0:4000-1];
f=f';
sm=konno_ohmachi_matrix(f,80);
spe1=sm*spe1;
spe2=sm*spe2;
spe3=sm*spe3;
%}
spe1=smooth(spe1,15);
spe2=smooth(spe2,15);
spe3=smooth(spe3,15);
speh=(spe2.^2+spe3.^2).^0.5;
%{
raw2=(rawdata_two.^2+rawdata_three.^2).^0.5;
speh=abs(fft(raw2));
spe1=abs(fft(rawdata_one));
speh=speh(1:2000);
spe1=spe1(1:2000);
spe1=smooth(spe1,200);
%}
y=speh./spe1;
y=y(1:(last-start+1)/2+1);
x=nyquistf/((last-start+1)/2)*(0:(last-start+1)/2);