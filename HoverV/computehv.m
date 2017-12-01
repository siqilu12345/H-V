function [x,y]=computehv(filen1,f2,f3)
%long=last-start+1;
start=1;
last=4000;
long=4000;
i=1;
n=2;
freqlen=floor(long/n);
cover=0.8;
%i=num;
fname1=['/Users/siqilu/Desktop/data/crflpsv_th',num2str(filen1),'r',...
    num2str(f2),'d',num2str(f3),'.txt'];
fileid=fopen(fname1);
data=textscan(fileid,'%f %f');
rawdata=cell2mat(data(2));
rawdata_one=rawdata((2*i-2)*4096+1:4096*(2*i-1));
rawdata_one=rawdata_one(start:last);
rawdata_two=rawdata((2*i-1)*4096+1:4096*2*i);
rawdata_two=rawdata_two(start:last);
fclose(fileid);
fname2=['/Users/siqilu/Desktop/data/crflsh_th',num2str(filen1),'r',...
    num2str(f2),'d',num2str(f3),'.txt'];
fileid=fopen(fname2);
data=textscan(fileid,'%f %f');
rawdata=cell2mat(data(2));
rawdata_three=rawdata((i-1)*4096+1:4096*i);
rawdata_three=rawdata_three(start:last);
fclose(fileid);
%{
[b,a] = butter(3,[0.1,6]/8,'bandpass');
freqz(b,a);
rawdata_one = filter(b,a,rawdata_one);
rawdata_two = filter(b,a,rawdata_two);
rawdata_three = filter(b,a,rawdata_three);
%}
trans_one=zeros(freqlen,1);
trans_two=zeros(freqlen,1);
trans_three=zeros(freqlen,1);
hv=zeros(floor(freqlen/2),1);
f=[0:freqlen-1];
f=f';
%sm=konno_ohmachi_matrix(f,1);
for i=1:(1-cover):n
    %data_one=taper(rawdata_one((i-1)*512+1:i*512));
    %data_two=taper(rawdata_two((i-1)*512+1:i*512));
    %data_three=taper(rawdata_three((i-1)*512+1:i*512));
    data_one=rawdata_one((i-1)*freqlen+1:i*freqlen);
    data_two=rawdata_two((i-1)*freqlen+1:i*freqlen);
    data_three=rawdata_three((i-1)*freqlen+1:i*freqlen);
    r1=smooth(abs(fft(data_one)/length(fft(data_one))),10);
    r2=smooth(abs(fft(data_two)/length(fft(data_two))),10);
    r3=smooth(abs(fft(data_three)/length(fft(data_three))),10);
    trans_one=r1+trans_one;
    trans_two=r2+trans_two;
    trans_three=r3+trans_three;
end
trans_one=trans_one./n;
trans_two=trans_two./n;
trans_three=trans_three./n;
trans_two=(trans_two.^2+trans_three.^2).^0.5;
trans_one=trans_one(1:freqlen/2);
trans_two=trans_two(1:freqlen/2);
%uf=((2*trans_one).^2+(2*trans_two).^2).^0.5
%uf(1)=uf(1)/2
hv=trans_two./trans_one;
%plot((8.0/freqlen*2).*(1:freqlen/2*0.75),log(hv(1:freqlen/2*0.75)))
x=(8.0/freqlen*2).*(1:freqlen/2*0.75);
y=hv(1:freqlen/2*0.75);

