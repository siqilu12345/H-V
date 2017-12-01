function konno_ohmachi_smooth(data,b)
smooth_matrix=konno_ohmachi_matrix(data,b);
data=smooth_matrix*data;
data