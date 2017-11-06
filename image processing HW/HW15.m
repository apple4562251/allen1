clear all; clc;%清空%
p=imread('Problem3.bmp');
q=imread('Problem3.bmp');
%--------3X3---------%
[m n]=size(p);
mg=sum(sum(p))/m/n;                  %整體平均值
og=(sum(sum((p-mg).^2))/m/n)^0.5 ;    %整體標準差
E=100.0;
k0=0.5;   %0.2 0.01 0.2
k1=0.01;
k2=0.2;
k5=0;
for a=1:m-14
    for b=1:n-14
        ml=sum(sum(p(a:a+14,b:b+14)))/225;            %局部平均值
        o=(sum(sum((p(a:a+14,b:b+14)-ml).^2)))^0.5; %局部標準差
        for aa=a:a+14
            for bb=b:b+14
               if (ml<k0*mg)&(k1*og<=o<=k2*og);
                   p(aa,bb)=E*p(aa,bb);
               end
            end
        end
        k5=k5+2
    end
end
imshow(p)