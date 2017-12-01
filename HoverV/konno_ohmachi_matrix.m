function y=konno_ohmachi_matrix(data,b)
smooth_matrix=zeros(length(data),length(data));
for i=1:length(data)
    smooth_matrix(i,:)=konno_ohmachi_window(b,data(i),data)';
end
y=smooth_matrix;
    