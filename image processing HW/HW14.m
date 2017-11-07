clear all; clc;%睲%
p=imread('Problem4.bmp');
[orow ocol]=size(p);
nearest=zeros(400,400);
[nrow ncol]=size(nearest);
p=im2double(p);
%--------程羬干畉-----%
gridx=(orow-1)/(nrow-1);
gridy=(ocol-1)/(ncol-1);
for  i=1:nrow
    for j=1:ncol
       nearest(i,j)=p(round(1+(i-1)*gridx),round(1+(j-1)*gridy));
    end
end
figure(1);imshow(nearest)
figure(1);title('程羬干畉')
% ------bilinear----------%
for  i=1:nrow
    for j=1:ncol
       x=1+(i-1)*gridx;
       y=1+(j-1)*gridy;
       x1=floor(x);
       x2=ceil(x);
       y1=floor(y);
       y2=ceil(y);
       lu=p(x1,y1);%g1   
       ru=p(x1,y2);%g2   
       ld=p(x2,y1);%g3    
       rd=p(x2,y2);%g4    
       a=ld-lu;
       b=ru-lu;
       c=rd-ru-ld+lu;
       d=lu;
       nearest(i,j)=a*(x-x1)+b*(y-y1)+c*(x-x1)*(y-y1)+d;
    end
end
figure(2);imshow(nearest)
figure(2);title('蛮絬┦础干')



