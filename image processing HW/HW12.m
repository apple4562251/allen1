
clear all; clc;%清空%

c=imread('Problem2_1.bmp');
d=imread('Problem2_2.bmp');
%--------汽車----------%
[m n]=size(c);
[i j]=size(d);
x1=0:255;
y1=zeros(1,256);
for a=1:m
   for b=1:n
        y1(c(a,b)+1)=y1(c(a,b)+1)+1;
   end
end
%--------城市----------%
x2=0:255;
y2=zeros(1,256);
for a=1:i
   for b=1:j
          y2(d(a,b)+1)=y2(d(a,b)+1)+1;
   end
end
%------汽車直方圖等化----%
s=0:255;              %強度表範圍
s1=zeros(1,256);      %直方圖等化的轉換強度
y3=zeros(1,256);      %放轉換完強度(s1)的數量

for ss1=1:256         
    for ss2=1:ss1
      s1(ss1)=s1(ss1)+y1(ss2);
    end
    s1(ss1)=round(s1(ss1)*255/m/n);
end
for yy3=1:256
   for yyy3=1:256
      if(s1(yyy3)==s(yy3))
          y3(yy3)=y3(yy3)+y1(yyy3);
      end
   end
end
newc=c;
for a=1:m
    for b=1:n
        newc(a,b)=s1(newc(a,b)+1);
    end
end

%---------城市直方圖等化----------%
s2=zeros(1,256);      %直方圖等化的轉換強度
y4=zeros(1,256);      %放轉換完強度(s2)的數量
for ss1=1:256         
    for ss2=1:ss1
      s2(ss1)=s2(ss1)+y2(ss2);
    end
    s2(ss1)=round(s2(ss1)*255/i/j);
end
for yy3=1:256
   for yyy3=1:256
      if(s2(yyy3)==s(yy3))
          y4(yy3)=y4(yy3)+y2(yyy3);
      end
   end
end
newd=d;
for a=1:i
    for b=1:j
        newd(a,b)=s2(newd(a,b)+1);
    end
end
%----------顯示直方等化圖------%
% figure(3);
% subplot(2,2,1);bar(x1,y1)   %切上下兩部份顯示直方圖
% set(gca,'XLim',[0 255]);
%subplot(2,2,3);bar(x2,y2)
%set(gca,'XLim',[0 255]);
% subplot(2,2,2);bar(s,y3)
% set(gca,'XLim',[0 255]);
% subplot(2,2,4);bar(s,y4)
% set(gca,'XLim',[0 255]);
%----------顯示直方等化後的圖片------%
% figure(1);subplot(2,1,1);imshow(c);%Show出圖片%
% figure(1);subplot(2,1,2);imshow(newc)
% figure(2);subplot(2,1,1);imshow(d);%
% figure(2);subplot(2,1,2);imshow(newd)
%----------高斯分布Pz------------%
mmm=1;   % 1-0.5 0.502-0.25
ooo=0.502;
y=-1:(2/255):1;
for x=1:256
  f(x)=exp(-((y(x)-mmm)^2)/(2*(ooo^2)))/ooo/((pi*2)^0.5);
end
%--------汽車直方圖匹配-------%

g1=zeros(1,256);      %直方圖匹配的轉換強度
gy1=zeros(1,256);      %放轉換完強度(g1)的數量
for ss1=1:256         
    for ss2=1:ss1
      g1(ss1)=g1(ss1)+f(ss2);
    end
    g1(ss1)=round(g1(ss1)*255);
end
newgc=c;
for a=1:m
    for b=1:n
        for cc=1:256
           if(newgc(a,b)==s(cc))
              newgc(a,b)=g1(cc);
              break;
           end
        end
    end
end
% 
%---------figure;imshow(newgc) 城市直方圖匹配----------%
%----------高斯分布Pz------------%
mmm=1;   % 1-0.5 0.502-0.25
ooo=0.3;
y=-1:(2/255):1;
for x=1:256
  f(x)=exp(-((y(x)-mmm)^2)/(2*(ooo^2)))/ooo/((pi*2)^0.5);
end
f=f/sum(f);
total=sum(f);
figure(5);plot(y,f)

%------------------------%
g2=zeros(1,256);      %直方圖匹配的轉換強度
gy2=zeros(1,256);      %放轉換完強度(g2)的數量
for ss1=1:256         
    for ss2=1:ss1
      g2(ss1)=g2(ss1)+f(ss2);
    end
    g2(ss1)=round(g2(ss1)*255);
end
newgd=newd;
for a=1:i
    for b=1:j
        for cc=1:256
           if(newgd(a,b)==s(cc))
              newgd(a,b)=g2(cc);
              break;
           end
        end
    end
end
figure;imshow(newgd)   %直方圖匹配
%-----desired histogram-----%
yyg1=zeros(1,256);
for a=1:m
   for b=1:n
        yyg1(newgd(a,b)+1)=yyg1(newgd(a,b)+1)+1;
   end
end
figure(6);bar(x1,yyg1)
set(gca,'XLim',[0 255]);
%-----------指定直直方圖的Pz要自己Tune-----------%
% Iblur = imgaussfilt(d, 2);
% figure;imshow(Iblur)
    
    
    
    
    

        