clear all; clc;%清空%
p=imread('Problem4.bmp');
[orow ocol]=size(p);
nearest=zeros(400,400);
[nrow ncol]=size(nearest);
p=im2double(p);
%--------最近臨補差-----%
gridx=(orow-1)/(nrow-1);
gridy=(ocol-1)/(ncol-1);
% for  i=1:nrow
%     for j=1:ncol
%        nearest(i,j)=p(round(1+(i-1)*gridx),round(1+(j-1)*gridy));
%     end
% end
% 
% imtool(nearest)
% ---------------------%
% ceil(x) 進
% floor(x) 退
% for  i=1:nrow
%     for j=1:ncol
%        lu=p(floor(1+(i-1)*gridx),floor(1+(j-1)*gridy));    %左上(x1,y2)   x2=ceil(1+(j-1)*gridy)
%        ru=p(floor(1+(i-1)*gridx),ceil(1+(j-1)*gridy));     %右上(x2,y2)   x1=floor(1+(j-1)*gridy)
%        ld=p(ceil(1+(j-1)*gridx),floor(1+(j-1)*gridy));     %左下(x1,y1)   y2=floor(1+(i-1)*gridx)
%        rd=p(ceil(1+(i-1)*gridx),ceil(1+(j-1)*gridy));      %右下(x1,y2)   y1=ceil(1+(i-1)*gridx)
%        x1=floor(1+(j-1)*gridy);
%        x2=ceil(1+(j-1)*gridy);
%        y1=ceil(1+(i-1)*gridx);
%        y2=floor(1+(i-1)*gridx);
%        x=(1+(j-1)*gridy);
%        y=(1+(i-1)*gridx);
%        f1=((x2-x)/(x2-x1))*lu+((x-x1)/(x2-x1))*ru;
%        f2=((x2-x)/(x2-x1))*ld+((x-x1)/(x2-x1))*rd;
%        nearest(i,j)=((y2-y)/(y2-y1))*f2+((y-y1)/(y2-y1))*f1;
%     end
% end
% imtool(nearest)
%-------------------%
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
imtool(nearest)



